import random as ran
import streamlit as st

# La tua funzione originale rimane identica
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'mandare bacetti a fra'
    elif answerNumber == 2:
        return 'abbraccio virtuale'
    elif answerNumber == 3:
        return 'how i met your mother'
    elif answerNumber == 4:
        return 'preparare biscotti'
    elif answerNumber == 5:
        return 'mandare tanti bacetti pt 2'

# Invece di window.title(), usiamo st.title()
st.title('random relax')

# Invece di tk.Button, usiamo st.button all'interno di un "if"
# Quando il tuo amico clicca, il programma entra in questo blocco di codice
if st.button('generate'):
    
    # Generiamo il numero e prendiamo la risposta, esattamente come prima
    r = ran.randint(1, 5)
    fortune = getAnswer(r)
    
    # Invece di tk.Label, usiamo st.write() per stampare il testo sullo schermo
    st.write(fortune)
