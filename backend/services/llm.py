"""
LLM 모델 관련 로직을 처리하는 모듈
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
GEMINI_APIKEY = os.getenv('GEMINI_APIKEY')
OPENAI_API = os.getenv('OPENAI_API')

class LLMService:
    def __init__(self):
        # LLM 모델 초기화
        self.gemini = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro", 
            temperature=0.2, 
            google_api_key=GEMINI_APIKEY,
            convert_system_message_to_human=True
        )
        self.gpt = ChatOpenAI(
            model='gpt-4o-mini', 
            temperature=0.2, 
            api_key=OPENAI_API
        )
        
        # 프롬프트 템플릿 정의
        self.human_prompt = ChatPromptTemplate.from_messages([
            ("system",
             "너는 전문적인 웹 크롤링 전략 설계 엔진이다.\n"
             "사용자가 입력한 목표를 달성하기 위해 필요한 크롤링 대상 사이트와 수집 항목, 분석 방향을 설계하라.\n\n"
             "출력은 반드시 JSON 형식으로 하며, 키 이름은 아래와 같이 고정한다:\n"
             "{{\n"
             '  "목표": "...",\n'
             '  "크롤링_추천_사이트": ["사이트명1", "사이트명2", "사이트명3"],\n'
             '  "수집할_항목": ["항목1", "항목2", "항목3"],\n'
             '  "추천_방법": ["requests+BeautifulSoup", "selenium", "API"],\n'
             '  "분석_방향": ["키워드 추출", "감정 분석", "불편 유형 분류"]\n'
             "}}\n\n"
             "⚠️ JSON 외의 다른 설명이나 문장은 출력하지 말라."
            ),
            ("human", "{user_input}")
        ])
        
        # 체인 구성
        self.human_chain = self.human_prompt | self.gemini
        
    async def generate_response(self, prompt: str) -> str:
        """
        프롬프트를 받아서 LLM 모델의 응답을 생성
        """
        print(f"llm.py: Received user input: {prompt}")
        try:
            # LLM 체인 실행
            response = await self.human_chain.ainvoke({"user_input": prompt})
            print(f"llm.py: LLM response: {response.content}")
            return response.content
        except Exception as e:
            raise Exception(f"LLM 처리 중 오류 발생: {str(e)}")

# 서비스 인스턴스 생성
llm_service = LLMService()