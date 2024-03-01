# PROJECT-1(1):
#from Tkinter import *
from tkinter import *
def add():
    if (e1.get().isdigit()):
        fries = int(e1.get())*30
    else:
        fries = 0
    if (e2.get().isdigit()):
        noodles = int(e2.get())*30
    else:
        noodles = 0
    if (e3.get().isdigit()):
        soup = int(e3.get())*10
    else:
        soup = 0
    if (e4.get().isdigit()):
        burger = int(e4.get())*25
    else:
        burger = 0
    if (e5.get().isdigit()):
        sandwich = int(e5.get())*35
    else:
        sandwich = 0
    if (e6.get().isdigit()):
        drinks = int(e6.get())*15
    else:
        drinks = 0
    r1 = fries+noodles+soup+burger+sandwich+drinks
    COM.set(r1)
    r2 = float(r1*15/100.0)
    ST.set(r2)
    r3 = float(r1*5/100.0)
    SC.set(r3)
    r4 = int(r2+r3)
    SUB.set(r4)
    r5 = int(r1+r4)
    TOTAL.set(r5)
top = Tk()
COM=StringVar()
ST=StringVar()
SC=StringVar()
SUB=StringVar()
TOTAL=StringVar()
Label(top, text="FLAVOURS RESTAURANT", fg='red').grid(row=0, column=2)
Label(top, text="FRIES").grid(row=1, column=0, sticky=W)
Label(top, text="NOODLES").grid(row=2, column=0, sticky=W)
Label(top, text="SOUP").grid(row=3, column=0, sticky=W)
Label(top, text="BURGER").grid(row=4, column=0, sticky=W)
Label(top, text="SANDWICH").grid(row=5, column=0, sticky=W)
Label(top, text="DRINKS").grid(row=6, column=0, sticky=W)
Label(top, text=":").grid(row=1, column=1, sticky=W)
Label(top, text=":").grid(row=2, column=1, sticky=W)
Label(top, text=":").grid(row=3, column=1, sticky=W)
Label(top, text=":").grid(row=4, column=1, sticky=W)
Label(top, text=":").grid(row=5, column=1, sticky=W)
Label(top, text=":").grid(row=6, column=1, sticky=W)
Label(top, text="30/-").grid(row=1, column=3, sticky=W)
Label(top, text="30/-").grid(row=2, column=3, sticky=W)
Label(top, text="10/-").grid(row=3, column=3, sticky=W)
Label(top, text="25/-").grid(row=4, column=3, sticky=W)
Label(top, text="35/-").grid(row=5, column=3, sticky=W)
Label(top, text="15/-").grid(row=6, column=3, sticky=W)
Label(top, text="COST OF MEALS").grid(row=1, column=4, sticky=W)
Label(top, text="SERVICE CHARGE").grid(row=2, column=4, sticky=W)
Label(top, text="SALES TAX").grid(row=3, column=4, sticky=W)
Label(top, text="SUB-TOTAL").grid(row=4, column=4, sticky=W)
Label(top, text="TOTAL COST").grid(row=5, column=4, sticky=W)
Label(top, text=":").grid(row=1, column=5, sticky=W)
Label(top, text=":").grid(row=2, column=5, sticky=W)
Label(top, text=":").grid(row=3, column=5, sticky=W)
Label(top, text=":").grid(row=4, column=5, sticky=W)
Label(top, text=":").grid(row=5, column=5, sticky=W)
Label(top, text="15%").grid(row=2, column=7, sticky=W)
Label(top, text="5%").grid(row=3, column=7, sticky=W)
e1 = Entry(top, bg='skyblue')
e2 = Entry(top, bg='skyblue')
e3 = Entry(top, bg='skyblue')
e4 = Entry(top, bg='skyblue')
e5 = Entry(top, bg='skyblue')
e6 = Entry(top, bg='skyblue')
e1.grid(row=1, column=2, sticky=E)
e2.grid(row=2, column=2, sticky=E)
e3.grid(row=3, column=2, sticky=E)
e4.grid(row=4, column=2, sticky=E)
e5.grid(row=5, column=2, sticky=E)
e6.grid(row=6, column=2, sticky=E)
result1=Label(top,text="",textvariable=COM).grid(row=1, column=6, sticky=W)
result2=Label(top,text="",textvariable=ST).grid(row=2, column=6, sticky=W)
result3=Label(top,text="",textvariable=SC).grid(row=3,column=6,sticky=W)
result4=Label(top,text="",textvariable=SUB).grid(row=4,column=6,sticky=W)
result5=Label(top,text="",textvariable=TOTAL).grid(row=5,column=6,sticky=W)  
b1 = Button(top, text="TOTAL", command=add)
b1.grid(row=7, column=3)
b2 = Button(top, text="EXIT", command=top.destroy)
b2.grid(row=7, column=5)
top.geometry("500x200")
top.mainloop()
