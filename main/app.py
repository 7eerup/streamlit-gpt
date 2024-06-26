import streamlit as st
import openai
import time
import os

# API key 설정
openai.api_key = os.environ["OPENAI_API_KEY"]


def chat_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        max_tokens=500,     # 텍스트 제한
        n=1,                # 응답 수 
        temperature=0.7,    # 창의력
    )
    return response.choices[0].message['content'].strip()


# ------------ 메인(Main) 화면 구성 ------------
image_url = "https://cdn.pixabay.com/photo/2024/03/12/09/28/ai-generated-8628373_1280.png"
st.image(image_url, width=350)



# ------------ 사이드바(Side bar) 화면 구성 ------------
st.sidebar.caption(':house: Home')
st.sidebar.title('Anyounghaseyo(안녕하세요) :bow:')
st.sidebar.header('Hello:wave: streamlitGPT🧑‍💻')

# 검색어 입력
search_query = st.sidebar.text_input('🔍 검색어를 입력해 주세요')


if st.sidebar.button("🔍 검색"):
    if search_query:
        with st.spinner('RUNNING...⏳'):      # 1. 로딩 상태 구현
            result = chat_gpt(search_query)
        st.write(result)
        st.success("streamlitGPT 이용해 주셔서 감사합니다🙏")
        # st.balloons()   # 2. 검색 완료 알림 - 풍선 효과
    else:
        st.error("검색어를 입력해 주세요")


st.sidebar.caption(':copyright: 2024 streamlitGPT')