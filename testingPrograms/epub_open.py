
'''from tkinter import *
from tkinter import filedialog
import PyPDF2 #import PdfFileReader
import fitz
import os


open_file = filedialog.askopenfilename(
        initialdir = os.getcwd(), 
        title = "Open PDF file",
        filetypes = (("pdf file", "*.epub"), 
                    ("All files", "*.*"))
        )

doc = fitz.open(open_file) 
#print ("number of pages: %i" % doc.pageCount)
#print(doc.metadata)

#number_of_pages = doc.pageCount

#get text from file and add it to textbox
#loadSetPage(0)

print(doc)


open_file = filedialog.askopenfilename(
        initialdir = os.getcwd(), 
        title = "Open PDF file",
        filetypes = (("epub file", "*.epub"), 
                    ("All files", "*.*"))

#pdf_document = "D:\Pragraming\ebookreader\testingPrograms\maj.epub"

doc = fitz.open(open_file)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)

page1 = doc.loadPage(0)
page1text = page1.getText("text")
print(page1text)

'''

import ebooklib
from ebooklib import epub

book = epub.read_epub('D:\Pragraming\ebookreader\testingPrograms\maj.epub')

for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    print (image)