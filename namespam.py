import random
from tkinter import * 
from tkinter import ttk
from turtle import *

root = Tk()
root.title('Designer OP')
root.geometry('250x250')
root.maxsize(200,200)
root.wm_iconbitmap('birdOP.png')
root.config(background='#00FF80')



Label(root,text='Enter Name',bg = '#00FF80',font = 'bold').pack()

namevalue = StringVar()
name = Entry(root,width = 10,textvariable=namevalue)
name.pack(fill = BOTH)



def design():
    global namevalue
    screen = Screen()
    bgcolor('#ffffb3')
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray", "brown", "aqua", "sea green"]
    
    for  i in range(100):
        a= random.choice(colors)
        pencolor(f'{a}')
        penup()
        goto(random.randint(-200,200),random.randint(-200,200))
        write(f'{namevalue.get()}',True,font=('lucida',18,'bold'))
    
        hideturtle()
    mainloop()

    

    
    


Button(root,text = 'GO',background='#009999',command=design).pack()





root.mainloop()
