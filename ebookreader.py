from tkinter import *
from tkinter import filedialog
import fitz #PyMuPDF
import os

root = Tk()
root.title('Ebook Reader')
root.state('zoomed')
root.iconbitmap('pixel_book_logo.ico')
root.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
root.rowconfigure(0, weight=1)

#inits
button_forward = None
button_back = None
button_forward = Button()
button_back = Button()
page_label = Label()
label_text = StringVar()
number_of_pages = 1
page_number_label = 1

#Create text box
my_text = Text(root)
my_text.pack(pady=10)
my_text.grid(row=0, column=0, columnspan=7, sticky=W+E+S+N)
my_text.config(bg="#fff5c5")
my_text.configure(font=("Calibri", 12))


#open pdf file
def openFile():
    global doc
    global number_of_pages
    global button_forward
    global button_back
    global page_label
    global label_text
    global page_number_label
    global open_file

    #grab the filename of the pdf file
    open_file = filedialog.askopenfilename(
            initialdir = os.getcwd(), 
            title = "Open Pdf file",
            filetypes = (("pdf file", "*.pdf"), 
                        ("epub file", "*.epub"),
                        ("txt file", "*.txt"),
                        ("All files", "*.*"))
            )
    
    if open_file.endswith('.txt'):
        
        clearTextBut()
        
        form_txt = open(open_file)
        my_text.config(state = 'normal')
        my_text.insert(INSERT, form_txt.read())
        my_text.config(state = 'disable')

        number_of_pages = 1

    else:
        
        clearTextBut()
        
        doc = fitz.open(open_file)
    
        number_of_pages = doc.pageCount

        loadSetPage(0)

    #indentation instead of .pack() which isnt working for some reason
    indentation_label = Label(text=" ")
    indentation_label.grid(row=1)
    indentation_label = Label(text=" ")
    indentation_label.grid(row=3)

    #reset page counter
    page_number_label = 1

    #page number init
    updateLabel(page_number_label)

    #forward, back buttons
    button_forward = Button(root, text=">>", height=2, width=10, command=lambda: forward(1))
    if open_file.endswith('.txt'):
        button_forward.configure(state=DISABLED)
    button_forward.grid(row=2, column=5)

    button_back = Button(root, text="<<", height=2, width=10, state=DISABLED)
    button_back.grid(row=2, column=1)

    #page number
    page_label = Label(root, textvariable=label_text)
    page_label.grid(row=2, column=3)


#clear text box
def clearTextBut():
    global doc

    #init doc
    doc = None

    #delete text in textbox
    deleteTextboxContent()

    #delete buttons and label with page numbers
    button_forward.destroy()
    button_back.destroy()
    page_label.destroy()


#allows to edit currently opened page 
#(disables after clicking next or previouos page and doesnt save changes)
def editTextbox():
    my_text.configure(state=NORMAL)


def saveThisFile():
    created_file = filedialog.asksaveasfilename(
                        defaultextension=".*", 
                        initialdir=os.getcwd(),
                        title = "Save file",
                        filetypes = (("txt file", "*.txt"), 
                                    ("All files", "*.*"))
                    )
    
    #if a file creation is wanted then create said file
    if created_file:
        saved_file = open(created_file, 'w')

        #for every page insert coresponding text
        for i in range(0,number_of_pages):
            
            #if a change was made in a speciffic page, include it in a save
            if i == page_number_label-1:
                saved_file.write(my_text.get(1.0, END))
            else:
                page_content = doc.loadPage(i)
                page_text = page_content.getText("text")
                saved_file.write(page_text)

        saved_file.close()


def deleteTextboxContent():
    #set textbox to edit mode and delete content inside
    my_text.configure(state=NORMAL)
    my_text.delete(1.0, END)


def updateLabel(current_page):
    global label_text

    #add page tracker
    label_text.set("Page: " + str(current_page) + "/" + str(number_of_pages))


#forward button
def forward(page_number):
    global my_text
    global page_number_label
    global button_forward
    global button_back

    #function to call correct page
    loadSetPage(page_number)

    #update button functions
    updateButtons(page_number)

    #check for last page
    if page_number == number_of_pages-1:
        button_forward.configure(state=DISABLED)

    #add to page number
    page_number_label = page_number_label + 1
    updateLabel(page_number_label)


#backwards button
def back(page_number):
    global my_text
    global page_number_label
    global button_forward
    global button_back

    #function to call correct page
    loadSetPage(page_number)

    #update button functions
    updateButtons(page_number)
    
    #check for first page
    if page_number == 0:
        button_back.configure(state=DISABLED)

    #subtract from page number
    page_number_label = page_number_label - 1
    updateLabel(page_number_label)


def loadSetPage(this_page):
    #delete text in textbox
    deleteTextboxContent()

    #get text from specific page
    page_content = doc.loadPage(this_page)
    page_text = page_content.getText("text")
    my_text.insert(1.0, page_text)

    #disable editing of textbox
    my_text.configure(state=DISABLED)


#updates commands of buttons
def updateButtons(page_adder):
    button_forward.configure(command=lambda: forward(page_adder+1))
    button_forward.configure(state=NORMAL)
    button_back.configure(command=lambda: back(page_adder-1))
    button_back.configure(state=NORMAL)



#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add dropdown menus
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open file", command=openFile)

file_menu.add_command(label="Save file", command = saveThisFile)

file_menu.add_command(label="Edit", command=editTextbox)
file_menu.add_command(label="Clear", command=clearTextBut)
file_menu.add_command(label="Exit", command=root.quit)


root.mainloop()