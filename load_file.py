from tkinter import *
from PIL import ImageTk,Image, 
from tkinter import filedialog
from PyPDF2 import PdfFileReader

root = Tk()
root.title('loudim jak pan')

def open():
    global my_file
    root.filename = filedialog.askopenfilename(initialdir="D:\Kódování\ebook-reader", title = "Find a file",filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_file = PdfFileReader()

root.mainloop()