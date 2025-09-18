import streamlit as st
import random

if 'c_num' not in st.session_state:
    st.session_state['c_num'] = random.randint(0, 100)
c_num = st.session_state.c_num

human_num = st.number_input('숫자를 입력하세요:', min_value=0, max_value=100, value=50) 
st.write(f'입력한 숫자는 {human_num}입니다.')   

computer_num = random.randint(0, 100)

if st.button('입력값비교'):
    if human_num > computer_num:
        st.write('입력한 숫자가 컴퓨터의 숫자보다 큽니다.')
    elif human_num < computer_num:
        st.write('입력한 숫자가 컴퓨터의 숫자보다 작습니다.')
    else:
        st.write('입력한 숫자와 컴퓨터의 숫자가 같습니다.')
        st.balloons()