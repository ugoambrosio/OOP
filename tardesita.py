import tkinter as tk
from tkinter import *


class Queue:
    def __init__(self):
        self.element = []
    def enqueu(self):
        x = valuetxt.get(1.0, "end-1c")
        self.element.append(x)
        
    def dequeue(self):
        self.element.remove(0)
    def displayqueue(self):
        print('Elements in Queue')
        for i in self.element:
            print(i)

top = Tk ()
top.geometry('700x700')

valuetxt = Text(width=35, height=2)
valuetxt.place(x=200, y=100)

def show(n):
    try:
        if n == 'Create':
            q1 = Queue()
        else:
            valuetxt.insert(tk.INSERT, n)
        if n == 'Enqueue':
            q1.enqueu()

        if n == 'Dequeue':
            q1.dequeue()
    except:
        valuetxt.delete(1.0, END)






B1 = Button(top,text='Queue',width=10,height=5,command=lambda:show(),background='blue',)
B1.place(x=100,y=350)

B2 = Button(top,text='Dequeue',width=10,height=5,command=lambda:show('2'),background='red')
B2.place(x=200,y=350)

B3 = Button(top,text='Display',width=10,height=5,command=lambda:show('3'),background='pink')
B3.place(x=300,y=350)



top.mainloop()