from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from pydantic import BaseModel
from datetime import datetime
import aiosqlite
import sqlite3
from typing import List
import os
from contextlib import asynccontextmanager

# Django WSGI app import
from config.wsgi import application as django_app

app = FastAPI()

# Mount Django admin
app.mount("/admin", WSGIMiddleware(django_app))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","*"],
    allow_credentials = True, allow_methods = ["*"], allow_headers = ["*"],
)

# Database setup
DATABASE_URL = "conversations.db"

def init_db():
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS conversations
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         prompt TEXT NOT NULL,
         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
         response TEXT,
         metadata TEXT)
    ''')
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()

class PromptIn(BaseModel):
    prompt: str

class Conversation(BaseModel):
    id: int
    prompt: str
    timestamp: str
    response: str = None
    metadata: str = None

@app.on_event("startup")
async def startup_event():
    init_db()

def save_conversation(prompt: str, db: sqlite3.Connection):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO conversations (prompt) VALUES (?)",
        (prompt,)
    )
    db.commit()
    return cursor.lastrowid

from services.llm import llm_service

@app.post("/api/submit")
async def submit(payload: PromptIn, db: sqlite3.Connection = Depends(get_db)):
    prompt = payload.prompt
    
    try:
        print(f"받은 프롬프트: {prompt}")  # 디버깅 로그
        
        # Save initial conversation to database
        conversation_id = save_conversation(prompt, db)
        print(f"대화 ID 생성됨: {conversation_id}")  # 디버깅 로그
        
        try:
            # Generate response using LLM
            print("LLM 응답 생성 시작...")  # 디버깅 로그
            llm_response = await llm_service.generate_response(prompt)
            print(f"LLM 응답 받음: {llm_response}")  # 디버깅 로그
            
            # Update conversation with response
            cursor = db.cursor()
            cursor.execute(
                "UPDATE conversations SET response = ? WHERE id = ?",
                (llm_response, conversation_id)
            )
            db.commit()
            print("DB에 응답 저장됨")  # 디버깅 로그
            
        except Exception as llm_error:
            print(f"LLM 에러 발생: {str(llm_error)}")  # 디버깅 로그
            # LLM 에러가 발생해도 기본 응답은 반환
            llm_response = f"LLM 처리 중 오류 발생: {str(llm_error)}"
            cursor = db.cursor()
            cursor.execute(
                "UPDATE conversations SET response = ? WHERE id = ?",
                (llm_response, conversation_id)
            )
            db.commit()
        
        # Get the updated conversation
        cursor = db.cursor()
        cursor.execute("SELECT * FROM conversations WHERE id = ?", (conversation_id,))
        conv = cursor.fetchone()
        print(f"최종 대화 데이터: {conv}")  # 디버깅 로그
        
        return {
            "ok": True,
            "message": f"LLM 응답이 생성되었습니다 (ID: {conversation_id})",
            "data": {
                "id": conv[0],
                "prompt": conv[1],
                "timestamp": conv[2],
                "response": conv[3],
                "metadata": conv[4]
            }
        }
    except Exception as e:
        db.rollback()
        return {
            "ok": False,
            "message": f"오류 발생: {str(e)}"
        }

@app.get("/api/conversations")
def get_conversations(db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        
        # 테이블 존재 여부 확인
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='conversations'
        """)
        if not cursor.fetchone():
            # 테이블이 없으면 생성
            init_db()
            
        cursor.execute("SELECT * FROM conversations ORDER BY timestamp DESC")
        conversations = cursor.fetchall()
        
        if not conversations:
            return {
                "message": "대화 내역이 없습니다.",
                "data": []
            }
            
        return {
            "message": "대화 내역을 불러왔습니다.",
            "data": [
                {
                    "id": row[0],
                    "prompt": row[1],
                    "timestamp": row[2],
                    "response": row[3],
                    "metadata": row[4]
                }
                for row in conversations
            ]
        }
    except Exception as e:
        return {
            "error": f"데이터베이스 오류: {str(e)}"
        }