import streamlit as st
count = 0

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('카운트 증가'):
    st.session_state.count += 1
    count = st.session_state.count

st.write(f'현재 카운트: ', count)   