import streamlit as st

col1, col2, col3, col4 = st.columns(4)

st.title("Hello world")

name = st.text_input("Hello friend what's your name?")


if name == 'Ruben':
   st.write(f'Nice to meet you, {name}!')
else :
   st.write(f'access denied')
with col1:
   if st.button('happy'):
    st.balloons()
with col2:
   if st.button('sad'):
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3a25oYzl3Z3BxNzJpaWh0MTRyd3R4OXQ4bzI5NHlwMzByejRyOTY1ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Yle9Yz9izeVRyiwavn/giphy.gif")
