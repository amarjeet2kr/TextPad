# 1.Save As Menu to be corrected.
# 2.when the mouse cursor is placed on the scrollbar, it should change the cursor.

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename,asksaveasfile
import os


def newFile():
    global file
    root.title("Untitled - Textpad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt",
                            filetypes = [("All Files", "*.*"),
                            ("Text DOcuments", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Textpad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfile(initialfile = 'Untitled.txt', defaultextension = ".txt",
                                filetypes = [("All Files", "*.*"), 
                                ("Text Documents", "*.txt")])
            
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Textpad")
            print("File saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

'''
def saveasFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt",
                                filetypes = [("All Files", "*.*"), 
                                ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f1 = open(file, "w")
            f1.write(TextArea.get(1.0, END))
            f1.close()

            root.title(os.path.basename(file) + " - Textpad")
            print("File saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()  
'''

def quitApp():
    root.destroy()         

def copy():
    TextArea.clipboard_clear()
    TextArea.clipboard_append(TextArea.selection_get())

def cut():
    copy()
    TextArea.delete("sel.first", "sel.last")
    
def paste():
    TextArea.insert(INSERT, TextArea.clipboard_get())

def about():
    showinfo("Textpad", "Textpad by Amarjeet")
    

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Textpad")
    # root.wm_iconbitmap("Textpad.ico")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font ="lucida 13")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    #Creating menubar
    menubar = Menu(root)

    #FileMenu starts
    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "New", command = newFile)
    filemenu.add_command(label = "Open", command = openFile)
    filemenu.add_command(label = "Save", command = saveFile)
    #filemenu.add_command(label = "Save as...", command = saveasFile)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = quitApp)
    menubar.add_cascade(label ="File", menu = filemenu)
    #File menu ends

    #Edit menu starts
    EditMenu = Menu(menubar, tearoff = 0)
    EditMenu.add_command(label ="Cut", command = cut)
    EditMenu.add_command(label ="Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    menubar.add_cascade(label = "Edit", menu = EditMenu)
    #Edit menu ends

    #help menu starts
    HeplMenu = Menu(menubar, tearoff = 0)
    HeplMenu.add_command(label = "About Textpad", command = about)
    menubar.add_cascade(label = "Help", menu = HeplMenu)
    #help menu ends

    #Adding scrollbar
    scroll_bar = Scrollbar(TextArea)
    scroll_bar.pack(side = RIGHT, fill = Y)
    scroll_bar.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = scroll_bar.set)
    #End of scrollbar

root.config(menu = menubar)
root.mainloop()