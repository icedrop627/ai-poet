"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from langchain_openai import ChatOpenAI

# Streamlit Secrets에서 API 키 가져오기
openai_api_key = st.secrets.get("OPENAI_API_KEY")

#ChatOpenAI 초기화
llm = ChatOpenAI(
    model="gpt-4o-mini",   # 또는 사용 중인 모델
    temperature=0.7,
    api_key=openai_api_key
)


#프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helpful assistant."),
  ("user", "{input}")
])


#문자열 출력 파서
output_parser = StrOutputParser()


#LLM 체인 구성
chain = prompt | llm | output_parser


#제목
st.title("인공지능 시인")


#시 주제 입력 필드
content = st.text_input("시의 주제를 제시해주세요")
st.write("시의 주제는", content)

#시 작성 요청하기
if st.button("시 작성 요청하기"):
  with st.spinner('Wait for it...'):
      result = chain.invoke({"input": content + "에 대한 시를 써줘"})
      st.write(result)
"""
import streamlit as st

# ===== 테스트용 코드 (확인 후 삭제) =====
st.write("Secrets 키 목록:", list(st.secrets.keys()))

if "OPENAI_API_KEY" in st.secrets:
    st.success("✅ OPENAI_API_KEY가 설정되어 있습니다!")
    # 키 앞 8자리만 보여주기 (보안상 전체 노출 X)
    st.write("키 미리보기:", st.secrets["OPENAI_API_KEY"][:8] + "...")
else:
    st.error("❌ OPENAI_API_KEY가 없습니다!")

st.stop()  # 여기서 멈춤 (아래 원래 코드 실행 안 함)
# ===== 테스트용 코드 끝 =====


