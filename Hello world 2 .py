import streamlit as st




st.title("Hello world")

name = st.text_input("Hello friend what's your name?", font = 'helvetica,16')
if name == 'Ruben':
    st.write(f'Nice to meet you, {name}!')
else st.write(f'access denied')
