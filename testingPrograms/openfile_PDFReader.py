
'''#check to see if there is a file
if open_file:
    # open the pdf file
    pdf_file = PyPDF2.PdfFileReader(open_file)
    #set the page to read
    page = pdf_file.getPage(0)
    #extract the text from the pdf file
    page_stuff = page.extractText()
    # add text to text box
    my_text.insert(1.0, page_stuff)'''

