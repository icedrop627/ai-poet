from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from langchain_openai import ChatOpenAI

# Streamlit Cloud Secrets 자동 주입됨
# os.environ["OPENAI_API_KEY"] 는 이미 설정된 상태

#ChatOpenAI 초기화
llm = ChatOpenAI(
    model="gpt-4o-mini",   # 또는 사용 중인 모델
    temperature=0.7
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
