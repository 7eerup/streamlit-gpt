import streamlit as st
import openai
import os

# API key set up
openai.api_key = os.environ["OPENAI_API_KEY"]

def chat_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()


# ------------ 메인(Main) 화면 구성 ------------
st.title('StreamlitGPT')


# 텍스트 입력 받기
st.sidebar.header('Hello Streamlit :sunny::cloud::umbrella::snowman:')
search_query = st.sidebar.text_input('🔍 검색어를 입력해 주세요 🙂')


if st.sidebar.button("🔍 검색"):
    if search_query:
        result = chat_gpt(search_query)
        st.write(result)




