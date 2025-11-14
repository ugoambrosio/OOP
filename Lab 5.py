import tkinter as tk
from tkinter import *


class Queue:
    def __init__(self):
        self.elementQueue = []

    def enqueu(self):
        x = valuetxt.get(1.0, "end-1c")
        self.elementQueue.append(x)

    def dequeue(self):
        self.elementQueue.remove(0)

    def displayQueue(self):
        print('Elements in Queue')
        for i in self.elementQueue:
            print(i)

class Stack:
    def __init__(self):
        self.elementStack = []
    def push(self):
        x = self.elementStack.append(valuetxt.get(1.0, "end-1c"))
    def pop(self):
        self.elementStack.pop()
    def displayStack(self):
        print('Elements in Stack:')
        for i in self.elementStack:
            print(i)

def show(n):
    try:
        if n == 'Create_Stack':
            s1 = Stack()
        else:
            valuetxt.insert(tk.INSERT, n)
        if n == 'Push':
            s1.push()
        else:
            valuetxt.insert(tk.INSERT, n)

        if n == 'Pop':
            s1.pop()
        else:
            valuetxt.insert(tk.INSERT, n)
        if n == 'Display_Stack':
            s1.displayStack()
        else:
            valuetxt.insert(tk.INSERT, n)
        if n == 'Create_Queue':
            q1 = Queue()
        else:
            valuetxt2.insert(tk.INSERT, n)
        if n == 'Enqueue':
            q1.enqueu()
        else:
            valuetxt2.insert(tk.INSERT, n)
        if n == 'Dequeue':
            q1.dequeue()
        else:
            valuetxt2.insert(tk.INSERT, n)
        if n == 'Display_Queue':
            q1.displayQueue()
        else:
            valuetxt2.insert(tk.INSERT, n)

    except:
        valuetxt.delete(1.0, END)




top = Tk ()
top.geometry('800x700')

valuetxt = Text(width=20, height=2)
valuetxt.place(x=80, y=90)

valuetxt2 = Text(width=20, height=2)
valuetxt2.place(x=400, y=90)

label1 = Label(width=20, height=2,text='Queue')
label1.place(x=90, y=50)

label2 = Label(width=20, height=2,text='Stack')
label2.place(x=420, y=50)

B1 = Button(top,text='Create Queue',width=10,height=5,command=lambda:show('Create_Queue'),background='blue')
B1.place(x=120,y=150)

B2 = Button(top,text='Enqueue',width=10,height=5,command=lambda:show('Enqueue'),background='red')
B2.place(x=120,y=250)

B3 = Button(top,text='Dequeue',width=10,height=5,command=lambda:show('Dequeue'),background='pink')
B3.place(x=120,y=350)

B4 = Button(top,text='Display Queue',width=10,height=5,command=lambda:show('Display_Queue'),background='orange')
B4.place(x=120,y=450)

B5 = Button(top,text='Create Stack',width=10,height=5,command=lambda:show('Create_Stack'),background='brown')
B5.place(x=450,y=150)

B6 = Button(top,text='Push',width=10,height=5,command=lambda:show('Push'),background='green')
B6.place(x=450,y=250)

B7 = Button(top,text='Pop',width=10,height=5,command=lambda:show('Pop'),background='gray')
B7.place(x=450,y=350)

B8 = Button(top,text='Display Stack',width=10,height=5,command=lambda:show('Display_Stack'),background='white')
B8.place(x=450,y=450)



top.mainloop()