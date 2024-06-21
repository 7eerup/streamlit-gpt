import streamlit as st
import openai
import os

# API 키 설정
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

st.title('StreamlitGPT')

search_query = st.sidebar.text_input('🔍 검색어를 입력해 주세요 🙂')

if st.sidebar.button("검색"):
    if search_query:
        result = chat_gpt(search_query)
        # print(result)
        st.write(result)
