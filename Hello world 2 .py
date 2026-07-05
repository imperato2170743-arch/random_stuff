import streamlit as st




st.title("Hello world")

name = st.text_input("Hello friend what's your name?")
if name:
    st.write(Nice to meet you, {name}!)
