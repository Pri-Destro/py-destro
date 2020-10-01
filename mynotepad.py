from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os


def newfile():
    global file
    file = None
    TextArea.delete(1.0, END)



def openfile():
    global file
    file = askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + 'Notepad')
        TextArea.delete(1.0,END)
        f = open(file,'r')
        TextArea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        if file == ' ':
            file = None
        else:
            f = open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + ' - Notepad')    
def cut():
    TextArea.event_generate(('<<Cut>>'))

def copy():
    TextArea.event_generate(('<<Copy>>'))

def paste():
    TextArea.event_generate(('<<Paste>>'))

def about():
    pass

def darkmode():
    TextArea.config(foreground="white", background='black')

def lightmode():
    TextArea.config(foreground="black", background='white')



if __name__ == '__main__':

    root = Tk()

    root.geometry('1000x1000')
    root.title('my notepad')

    TextArea = Text(root,font='lucida 13')
    TextArea.pack(expand=True,fill=BOTH)
    file=None

    Menubar = Menu(root)
    Filemenu = Menu(Menubar,tearoff=0)
    Filemenu.add_command(label='New',command = newfile)
    Filemenu.add_command(label='Open',command=openfile)
    Filemenu.add_command(label='Save',command=savefile)
    Menubar.add_cascade(label = 'File',menu=Filemenu)
    
    Editmenu = Menu(Menubar,tearoff=0)
    Editmenu.add_command(label='Cut',command = cut)
    Editmenu.add_command(label='Copy',command=copy)
    Editmenu.add_command(label='Paste',command=paste)
    Menubar.add_cascade(label = 'Edit',menu = Editmenu)

    Viewmenu = Menu(Menubar,tearoff=0)
    Viewmenu.add_command(label='darkmode',command=darkmode)
    Viewmenu.add_command(label='lightmode',command=lightmode)
    Menubar.add_cascade(label='View',menu = Viewmenu)
    

    Helpmenu = Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label='About',command = about)
    Menubar.add_cascade(label = 'Help',menu = Helpmenu)


    root.config(menu=Menubar)



    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT,fill = Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)






    root.mainloop()