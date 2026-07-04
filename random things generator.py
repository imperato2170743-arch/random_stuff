import random as ran
import tkinter as tk

def command1():
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
   def again():
      text_Output.destroy()
      text_Output1 = tk.Label(window, text = getAnswer(ran.randint(1,5)), font = 'Helvetica, 16')
      text_Output1.place(relx=0.5, rely=0.5, anchor='center')
      
   first_button.destroy()
   r = ran.randint(1, 5)
   fortune = getAnswer(r)
   #print(fortune)
   text_Output = tk.Label(window, text = fortune, font = 'Helvetica, 16')
   text_Output.place(relx=0.5, rely=0.5, anchor='center')
   button_again = tk.Button(text = 'retry', command = again, font = 'Helvetica,16')
   button_again.place(relx=0.8, rely=0.5, anchor='center')


window = tk.Tk()
window.geometry("300x300")
window.title('random relax')


first_button = tk.Button(text = 'generate', command = command1, font = 'Helvetica, 16')
first_button.place(relx=0.5, rely=0.5, anchor='center')


