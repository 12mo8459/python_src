import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("메뉴")
    selected_menu = st.radio(
        "원하시는 게임을 선택하세요:",
        ["가위바위보게임", "숫자맞추기게임"]
    )

# 메인 컨텐츠 영역
def show_game1():
    st.header("가위바위보게임")
    st.write("환영합니다! 이곳은 가위바위보게임 페이지입니다.")

import random
def show_game2():
    st.header("숫자맞추기게임")
    st.write("환영합니다! 이곳은 숫자맞추기게임 페이지입니다.")

    if 'c_number' not in st.session_state:
        st.session_state.c_number = random.randint(1, 100)
    c_num = st.session_state.c_number
    st.write(f'컴퓨터가 선택한 숫자는 {c_num}입니다.')

    st.number_input('숫자를 입력하세요:', 0, 100, key='h_number') 
    h_number = st.session_state.h_number
    st.write(f'입력한 숫자는 {h_number}입니다.')

    if h_number != 0:
        if h_number > c_num:
            st.write("입력한 숫자가 컴퓨터의 숫자보다 큽니다.")
        elif h_number < c_num:
            st.write("입력한 숫자가 컴퓨터의 숫자보다 작습니다.")
        else:
            st.write("입력한 숫자와 컴퓨터의 숫자가 같습니다.")
            st.balloons()
            del st.session_state.c_number

# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "가위바위보게임":
    show_game1()
elif selected_menu == "숫자맞추기게임":
    show_game2()
