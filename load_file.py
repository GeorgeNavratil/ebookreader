from tkinter import *
from tkinter import filedialog
import PyPDF2
from tika import parser

root = Tk()
root.title('loudim jak pan')
root.geometry("500x500")

#Create text box
my_text = Text(root, height=50, width=60)
my_text.pack(pady=10)

#clear text box
def clear_text_box():
    my_text.configure(state=NORMAL)
    my_text.delete(1.0, END)

#open pdf file
def open_pdf():
    my_text.delete(1.0, END)

    '''
    #grab the filename of the pdf file
    open_file = filedialog.askopenfilename(
            initialdir = "D:\Kódování\ebook-reader", 
            title = "Open PDF file",
            filetypes = (("pdf file", "*.pdf"), 
                        ("All files", "*.*"))
            )
    '''

    new_file = parser.from_file("D:\Kódování\ebook-reader\pdf3.pdf")
    new_file = str(new_file)

    safe_text = new_file.encode('utf-8', errors='ignore')
    safe_text = str(safe_text).replace('\n', '').replace('\\', '')

    my_text.insert(1.0, safe_text)

    
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


#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add dropdown menus
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open file", command = open_pdf)
file_menu.add_command(label="Clear", command = clear_text_box)
file_menu.add_command(label="Exit", command = root.quit)




root.mainloop()