
#pip instal PyMuPDF

from tkinter import filedialog
import fitz
import os

open_file = filedialog.askopenfilename(
            initialdir = os.getcwd(), 
            title = "Open PDF file",
            filetypes = (("pdf file", "*.pdf"), 
                        ("All files", "*.*"))
            )

pdf_document = "D:\Pragraming\ebook_reader\ourfiletexts\pdf4.pdf"
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
#print(doc.metadata)

page1 = doc.loadPage(0)
page1text = page1.getText("text")
print(page1text)
