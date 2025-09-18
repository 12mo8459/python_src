# 터미널 실행 > pip install streamlit

import streamlit as st
st.title('Hello, Streamlit!')
st.write("This is my first Streamlit app.")

st.header('헤더입니다')
st.subheader('서브헤더입니다')
st.button('버튼입니다')
st.checkbox('체크박스입니다')
st.radio('라디오 버튼입니다', ('옵션 1', '옵션 2'))
st.selectbox('셀렉트 박스입니다', ('옵션 A', '옵션 B', '옵션 C'))
st.slider('슬라이더입니다', 0, 100, 50)
st.text_area('텍스트 상자입니다')

name = st.text_input('이름을 입력하세요:')
st.write(f'안녕하세요, {name}님!')