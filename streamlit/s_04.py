import random
datas = [random.randint(1, 100) for i in range(10)]
print(datas)

import streamlit as st
st.bar_chart(datas)
st.line_chart(datas)
st.area_chart(datas)
col1, col2, col3 = st.columns(3)
#col1.bar_chart(datas)
#col2.line_chart(datas)
#col3.area_chart(datas)
with col1:
    st.bar_chart(datas)
with col2:
    st.line_chart(datas)
with col3:
    st.area_chart(datas)