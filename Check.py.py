activeplayer=1
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
activerplayer=1
p1=[]
p2=[]
layout=Tk()
layout.title('Tic Tac Toy: Player 1')
layout.resize(False, False)
but1=ttk.Button(layout, text='')
but1.grid(row=0,column=0,sticky='snew')
but1.config(command=lambda: Buclick(1))

but2=ttk.Button(layout, text='')
but2.grid(row=0,column=1,ipadx=20,ipady=20)
but2.config(command=lambda: Buclick(2))

but3=ttk.Button(layout, text='')
but3.grid(row=0,column=2,ipadx=20,ipady=20)
but3.config(command=lambda: Buclick(3))

but4=ttk.Button(layout, text='')
but4.grid(row=1,column=0,ipadx=20,ipady=20)
but4.config(command=lambda: Buclick(4))

but5=ttk.Button(layout, text='')
but5.grid(row=1,column=1,ipadx=20,ipady=20)
but5.config(command=lambda: Buclick(5))

but6=ttk.Button(layout, text='')
but6.grid(row=1,column=2,ipadx=20,ipady=20)
but6.config(command=lambda: Buclick(6))

but7=ttk.Button(layout, text='')
but7.grid(row=2,column=0,ipadx=20,ipady=20)
but7.config(command=lambda: Buclick(7))

but8=ttk.Button(layout, text='')
but8.grid(row=2,column=1,ipadx=20,ipady=20)
but8.config(command=lambda: Buclick(8))

but9=ttk.Button(layout, text='')
but9.grid(row=2,column=2,ipadx=20,ipady=20)
but9.config(command=lambda: Buclick(9))
def selayout(id,Playersymbol):
    if id==1:
        but1.config(text=Playersymbol)
        but1.state(['disabled'])
    elif id==2:
        but2.config(text=Playersymbol)
        but2.state(['disabled'])
    elif id==3:
        but3.config(text=Playersymbol)
        but3.state(['disabled'])
    elif id==4:
        but4.config(text=Playersymbol)
        but4.state(['disabled'])
    elif id==5:
        but5.config(text=Playersymbol)
        but5.state(['disabled'])
    elif id==6:
        but6.config(text=Playersymbol)
        but6.state(['disabled'])
    elif id==7:
        but7.config(text=Playersymbol)
        but7.state(['disabled'])
    elif id==8:
        but8.config(text=Playersymbol)
        but8.state(['disabled'])
    elif id==9:
        but9.config(text=Playersymbol)
        but9.state(['disabled'])

def Buclick(id): 
    global activeplayer
    global p1
    global p2
    if (activeplayer==1):
        selayout(id,"X")
        p1.append(id)
        layout.title("Tic Tac Toy: Player 2")
        activeplayer=2
        Autoplay()
    elif (activeplayer==2):
        selayout(id,"0")
        p2.append(id)
        layout.title("Tic Tac Toy: Player 1")
        activeplayer=1  
    checkwinner()
def checkwinner():
    winner=-1
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winner=1
    if ((1 in p2) and(2 in p2) and (3 in p2)):
        winner=2
    if ((4 in p1) and(5 in p1) and (6 in p1)):
        winner=1
    if ((4 in p2) and(5 in p2) and (6 in p2)):
        winner=2
    if ((7 in p1) and(8 in p1) and (9 in p1)):
        winner=1
    if ((7 in p2) and(8 in p2) and (9 in p2)):
        winner=2
    if ((1 in p1) and(4 in p1) and (7 in p1)):
        winner=1
    if ((1 in p2) and(4 in p2) and (7 in p2)):
        winner=2
    if ((2 in p1) and(5 in p1) and (8 in p1)):
        winner=1
    if ((2 in p2) and(5 in p2) and (8 in p2)):
        winner=2
    if ((3 in p1) and(6 in p1) and (9 in p1)):
        winner=1
    if ((3 in p2) and(6 in p2) and (9 in p2)):
        winner=2
    if ((1 in p1) and(5 in p1) and (9 in p1)):
        winner=1
    if ((1 in p2) and(5 in p2) and (9 in p2)):
        winner=2
    if ((3 in p1) and(5 in p1) and (7 in p1)):
        winner=1
    if ((3 in p2) and(5 in p2) and (7 in p2)):
        winner=2
        
    if winner==1:
        messagebox._show(title='Winner !',message='Player 1 wins')
    elif winner==2:
        messagebox._show(title='Winner 2',message='Player 2 wins')

def Autoplay():
    global p1
    global p2
    Emptycell=[]
    for cell in range(0,9):
        if (not((cell+1 in p1) or (cell+1 in p2))):
            Emptycell.append(cell+1)
    randindex=randint(0,(len(Emptycell))-1)
    Buclick(Emptycell[randindex])

            
layout.mainloop()