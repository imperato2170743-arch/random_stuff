import random as ran
import streamlit as st

# La tua funzione originale rimane identica
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'program'
    elif answerNumber == 2:
        return 'crochet'
    elif answerNumber == 3:
        return 'watch movie'
    elif answerNumber == 4:
        return 'read'
    elif answerNumber == 5:
        return 'watch a video'

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
