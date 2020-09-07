#A simple spelling corrector python program using tkinter module

from tkinter import *
from textblob import TextBlob
from tkinter.messagebox import *

def select(event):
    inputword.get()

def clearall():
    inputword.delete(0,END)
    correctedword.delete(0,END)

def correction():
    input_word = inputword.get()
    blob_obj = TextBlob(input_word)
    corrected_word = str(blob_obj.correct())
    correctedword.insert(10,corrected_word)

    if input_word == '' :
        correctedword.delete(0,END)


def exit():

    res = askyesno('Confirm', 'Are you sure you want to exit?')
    if res:
        root.destroy()
    else:
        pass


root =Tk()

root.configure(bg = 'BLACK')
root.title("spell corrector")
root.resizable()
root.geometry("500x450+0+0")


headlabel =Label(root, text ="Welcome to spell corrector application",font=("arial",12,"bold"),bd=2,bg ='whitesmoke',fg='black')
headlabel.grid(row=0,column=1,padx=10,pady=10)

fakelabel = Label(root,bg ='black',width =40)
fakelabel.grid(row=1,column = 1,padx=10,pady=10)

inputlabel = Label(root,text = "Input word",bg='white',fg="black",font=("arial",10,"bold"),bd=2,relief = "flat")
inputlabel.grid(row=2,column = 0,padx=5,pady=5)

correctedwordlabel = Label(root, text ="corrected word",bg="white",fg="black",font=("arial",10,"bold"),bd = 2, relief = "flat")
correctedwordlabel.grid(row=4,column=0,padx=10,pady=5)

inputword = Entry(root, font=('arial', 18, 'bold'), bd=8, relief= 'flat', width=10)
inputword.grid(row=2,column = 1,padx=10,pady=10)

correctedword = Entry(root, font=('arial', 18, 'bold'), bd=8, relief= 'flat', width=10)
correctedword.grid(row=4,column = 1,padx=10,pady=10)

buttoncorrection = Button(root,text = "correction",fg="black",bg = "red",relief = GROOVE,width=12,command = correction)
buttoncorrection.grid(row=3,column =1,padx=5,pady=5)

buttonclear = Button(root,text = "clear",fg="black",bg = "red",relief = GROOVE,width=10,command = clearall)
buttonclear.grid(row=5,column =1,padx=5,pady=5)

buttonexit = Button(root,text = "exit",fg="black",bg = "red",relief = GROOVE,width=8,command = exit)
buttonexit.grid(row=6,column =1,padx=5,pady=5)

def enter_function(event):
    buttoncorrection.invoke()

def enter_delete(event):
    buttonclear.invoke()

root.bind('<Return>', enter_function)
root.bind('<Delete>', enter_delete)

root.mainloop()
