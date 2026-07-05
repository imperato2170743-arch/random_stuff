import streamlit as st

st.title("Hello world")

name = st.text_input("Hello friend what's your name?")


if name == 'Ruben':
   st.write(f'Nice to meet you, {name}!')
else :
   st.write(f'access denied')

happy_click = False
fine_click = False
sad_click = False
tired_click= False

col1, col2, col3, col4 = st.columns(4)
with col1:
   if st.button('happy'):
    happy_click = True
   if st.button('fine'):
    fine_click = True
with col2:
   if st.button('sad')
    sad_click =  True
   if st.button('tired'):
    tired_click = True

if happy_click = True :
    st.balloons()
if fine_click = True :
    st.image('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGFtaXlvMHFiMjE5b2RpOGZ3ZXYzdHVtYmRkZWFhbmVwdTlhN2FlcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1FkCqpyObTuo0/giphy.gif',width= 500)

if sad_click =  True:
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3a25oYzl3Z3BxNzJpaWh0MTRyd3R4OXQ4bzI5NHlwMzByejRyOTY1ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Yle9Yz9izeVRyiwavn/giphy.gif",width=500)
if tired_click = True:
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MnQxNzcyNzNibWFpOWY5d3RoNXluMmo4enk1Znc1dmkzenR3cHl5MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/A8ReUjJdMCNOM/giphy.gif"width=500)
