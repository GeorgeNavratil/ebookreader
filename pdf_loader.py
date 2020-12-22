
#pip instal PyMuPDF

import fitz
import os

pdf_document = os.getcwd() + '/ourfiletexts/pdf4.pdf'
doc = fitz.open(pdf_document)
#print ("number of pages: %i" % doc.pageCount)
#print(doc.metadata)

page1 = doc.loadPage(0)
page1text = page1.getText("text")
print(page1text)