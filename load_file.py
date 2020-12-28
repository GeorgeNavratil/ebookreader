from tkinter import *
from tkinter import filedialog
import PyPDF2 #import PdfFileReader
import fitz
import os

root = Tk()
root.title('Ebook Reader')
root.geometry("1400x700")

#page number init
page_number_label = 1

#Create text box
my_text = Text(root, height=30, width=120)
my_text.pack(pady=10)
my_text.grid(row=0, column=0, columnspan=7)

#clear text box
def clear_text_box():
    my_text.configure(state=NORMAL)
    my_text.delete(1.0, END)

#open pdf file
def open_pdf():
    clear_text_box()

    #grab the filename of the pdf file
    open_file = filedialog.askopenfilename(
            initialdir = os.getcwd(), 
            title = "Open PDF file",
            filetypes = (("pdf file", "*.pdf"), 
                        ("All files", "*.*"))
            )
    
    global doc
    doc = fitz.open(open_file)
    #print ("number of pages: %i" % doc.pageCount)
    #print(doc.metadata)

    page_content = doc.loadPage(0)
    page_text = page_content.getText("text")
    my_text.insert(1.0, page_text)

    '''
    #check to see if there is a file
    if open_file:
        # open the pdf file
        pdf_file = PyPDF2.PdfFileReader(open_file)
        #set the page to read
        page = pdf_file.getPage(0)
        #extract the text from the pdf file
        page_stuff = page.extractText()
        # add text to text box
        my_text.insert(1.0, page_stuff)
    '''

    my_text.configure(state=DISABLED)


    #indentation instead of .pack() which isnt working for some reason
    indentation_label = Label(text=" ")
    indentation_label.grid(row=1)

    #page number init
    updateLabel(page_number_label)

    #forward, back buttons
    button_forward = Button(root, text=">>", height=1, width=10, command=lambda: forward(1))
    '''button_forward.pack(pady=10)'''
    button_forward.grid(row=2, column=5)

    button_back = Button(root, text="<<", height=1, width=10, state=DISABLED)
    '''button_back.pack(pady=10)'''
    button_back.grid(row=2, column=1)


def updateLabel(current_page):
    number_of_pages = doc.pageCount
    
    #page number
    page_label = Label(text="Page: " + str(current_page) + "/" + str(number_of_pages))
    page_label.grid(row=2, column=3)


def forward(page_number):
    global my_text
    global page_number_label
    global button_forward
    global button_back

    my_text.configure(state=NORMAL)
    my_text.delete(1.0, END)

    page_content = doc.loadPage(page_number)
    page_text = page_content.getText("text")
    my_text.insert(1.0, page_text)

    my_text.configure(state=DISABLED)

    button_forward = Button(root, text=">>", height=1, width=10, 
                            command=lambda: forward(page_number+1))
    button_back = Button(root, text="<<", height=1, width=10, 
                            command=lambda: back(page_number-1))
    
    '''if'''

    button_forward.grid(row=2, column=5)
    button_back.grid(row=2, column=1)

    page_number_label = page_number_label + 1
    updateLabel(page_number_label)

def back(page_number):
    global my_text
    global page_number_label
    global button_forward
    global button_back

    my_text.configure(state=NORMAL)
    my_text.delete(1.0, END)

    page_content = doc.loadPage(page_number)
    page_text = page_content.getText("text")
    my_text.insert(1.0, page_text)

    my_text.configure(state=DISABLED)

    button_forward = Button(root, text=">>", height=1, width=10, 
                            command=lambda: forward(page_number+1))
    button_back = Button(root, text="<<", height=1, width=10, 
                            command=lambda: back(page_number-1))
    
    '''if'''

    button_forward.grid(row=2, column=5)
    button_back.grid(row=2, column=1)
    
    page_number_label = page_number_label - 1
    updateLabel(page_number_label)


#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add dropdown menus
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open file", command = open_pdf)

'''file_menu.add_command(label="Save file", command = save_file)
file_menu.add_command(label="Edit", command = edit)'''

file_menu.add_command(label="Clear", command = clear_text_box)
file_menu.add_command(label="Exit", command = root.quit)



root.mainloop()