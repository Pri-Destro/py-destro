from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter.messagebox import showerror,showinfo

root = Tk()
root.title('Corona Meter')
root.geometry('455x455')
root.config(background = '#273746')
icon = PhotoImage(file = 'virus.png')
root.iconphoto(False,icon)

try:
    showinfo('info','Given information is in terms of world population ')

    def refresh():
        url = 'https://www.worldometers.info/coronavirus'
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent,'html.parser')

        datasource = soup.find_all('div',class_='maincounter-number')
        
        mydatastr = ''
        for data in datasource:
            mydatastr += data.get_text()
            datalist = mydatastr.split()
        
        # root.clear()
        no_of_cases = Label(root,text = datalist[0], foreground ='#F1C40F',font =('arial',20,'bold'),background = '#273746')
        no_of_cases.place(x=250,y=60)

        no_of_deaths = Label(root,text = datalist[1],foreground ='#F1C40F',font =('arial',20,'bold'),background = '#273746')
        no_of_deaths.place(x=255,y=150)
        
        no_of_recovered = Label(root,text = datalist[2],foreground ='#F1C40F',font =('arial',20,'bold'),background = '#273746')
        no_of_recovered.place(x=250,y=240)

    refresh()       # this will display noumbers for the first time
    
    Label(root,text = 'TOTAL CASES : ',foreground = '#2ECC71',font =('arial',20,'bold'),background = '#273746').place(x=30,y=60)
    Label(root,text = 'DEATHS : ',foreground = '#2ECC71',font =('arial',20,'bold'),background = '#273746').place(x=110,y=150)
    Label(root,text = 'RECOVERED : ',foreground = '#2ECC71',font =('arial',20,'bold'),background = '#273746').place(x=50,y=240)

    Button(root,text = 'refresh',height = 2,width = 7,background = '#34495E',foreground='#ECF0F1',font ='bold',relief=FLAT,activebackground='#7FB3D5',command=refresh).place(x=200,y=300)
    root.mainloop()
        
except Exception as e:
    showerror('error','enable your INTERNET connection and restart software')

