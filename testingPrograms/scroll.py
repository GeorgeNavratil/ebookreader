import socket, sys, threading, time
from tkinter import *

root = Tk()
text1 = Text(root, height=50, width=150)
scroll = Scrollbar(root, command=text1.yview, orient=VERTICAL )
scroll.config(command=text1.yview)
text1.configure(yscrollcommand=scroll.set)
entry = Entry(root, width = 200)
entry.pack(side = BOTTOM)
text1.pack(side=LEFT,fill=BOTH, expand='YES')
scroll.pack(side=RIGHT, fill=BOTH)

root.resizable(TRUE,TRUE)
root.mainloop()