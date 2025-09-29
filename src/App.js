// src/App.js
import React from "react";
import InputBar from "./components/InputBar";
import "./App.css";

export default function App() {
  const handleSubmit = async (text) => {
    // TODO: 이후 여기서 API 호출 or 상태 업데이트
    console.log("User input:", text);
  };

  return (
    <div className="app">
      <main className="hero">
        <h1 className="title">auto_crawl</h1>
        <p className="subtitle">원하는 수집/분석 목표를 입력해 시작하세요</p>

        {/* 하단 고정형 입력바 */}
        <div className="inputDock">
          <InputBar onSubmit={handleSubmit} />
          <p className="hint">Enter: 전송 · Shift+Enter: 줄바꿈</p>
        </div>
      </main>
    </div>
  );
}
