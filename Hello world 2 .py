import streamlit as st

st.title("Hello world")

name = st.text_input("Hello friend what's your name?")


if name == 'Ruben':
   st.write(f'Nice to meet you, {name}!')
else :
   st.write(f'access denied')

col1, col2, col3, col4 = st.columns(4)
with col1:
   if st.button('happy'):
    st.balloons()
   if st.button('fine'):
    st.image('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGFtaXlvMHFiMjE5b2RpOGZ3ZXYzdHVtYmRkZWFhbmVwdTlhN2FlcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1FkCqpyObTuo0/giphy.gif')
with col2:
   if st.button('sad'):
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3a25oYzl3Z3BxNzJpaWh0MTRyd3R4OXQ4bzI5NHlwMzByejRyOTY1ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Yle9Yz9izeVRyiwavn/giphy.gif")
   if st.button('tired'):
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MnQxNzcyNzNibWFpOWY5d3RoNXluMmo4enk1Znc1dmkzenR3cHl5MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/A8ReUjJdMCNOM/giphy.gif")
