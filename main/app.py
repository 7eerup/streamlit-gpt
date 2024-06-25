import streamlit as st
import openai
import time
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
        max_tokens=500, # 텍스트 제한
        n=1,            # 응답 수 
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

# ------------ 메인(Main) 화면 구성 ------------
image_url = "https://cdn.pixabay.com/photo/2024/03/12/09/28/ai-generated-8628373_1280.png" 
st.image(image_url, width=300)
# st.title(':wave:')

with st.spinner('RUNNING...'):
      time.sleep(7)

# 텍스트 입력 받기
st.sidebar.header('Hello StreamlitGPT :rocket:')
search_query = st.sidebar.text_input('🔍 검색어를 입력해 주세요')

if st.sidebar.button("🔍 검색"):
    if search_query:
        result = chat_gpt(search_query)
        st.write(result)
        st.success("답변이 마음에 드세요?")
    else:
        st.error("검색어를 입력해 주세요")