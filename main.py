from tkinter import *
import datetime
import random as automate
from tkinter import messagebox as tmsg
num1 = automate.randint(1,9998)
root = Tk()
quan = IntVar()
quan1 = IntVar()
quan2 = IntVar()
quan3 = IntVar()
quan4= IntVar()
quan5 = IntVar()
quan6 = IntVar()
quan7 = IntVar()
quan8 = IntVar()
quan9 = IntVar()
quan10 = IntVar()
quan11 = IntVar()
newquan1 = IntVar()
newquan2 = IntVar()
newquan3 = IntVar()
newquan4 = IntVar()
newquan5 = IntVar()
newquan6 = IntVar()
newquan7 = IntVar()
newquan8 = IntVar()
newquan9 = IntVar()
newquan10 = IntVar()
def total():
    l12_entry.delete(0,END)
    l12_entry.insert(0,f'${quan.get()*0.90+quan1.get()*0.45+quan2.get()*0.25+quan3.get()*0.15+quan4.get()*0.75+quan5.get()*0.98+quan6.get()*1.25+quan7.get()*0.56+quan8.get()*0.78+quan9.get()*2+quan10.get()}')
    cost_entry.delete(0,END)
    cost_entry.insert(0,f'${newquan1.get()*3+newquan2.get()*3.4+newquan3.get()*2.50+newquan4.get()*2.90+newquan5.get()*1.54+newquan6.get()*1.24+newquan7.get()*3.44+newquan8.get()*2.45+newquan9.get()*2.50+newquan10.get()*1}')
    gst_entry.delete(0,END)
    gst_entry.insert(0,"$1")
    Total_entry.delete(0,END)
    Total_entry.insert(0,f'${quan.get()*0.90+quan1.get()*0.45+quan2.get()*0.25+quan3.get()*0.15+quan4.get()*0.75+quan5.get()*0.98+quan6.get()*1.25+quan7.get()*0.56+quan8.get()*0.78+quan9.get()*2+quan10.get()+newquan1.get()*3+newquan2.get()*3.4+newquan3.get()*2.50+newquan4.get()*2.90+newquan5.get()*1.54+newquan6.get()*1.24+newquan7.get()*3.44+newquan8.get()*2.45+newquan9.get()*2.50+newquan10.get()*1+1}')
def clear():
    l12_entry.delete(0,END)
    a_entry.delete(0,END)
    a_entry.insert(0,0)
    b_entry.delete(0,END)
    b_entry.insert(0,0)
    c_entry.delete(0,END)
    c_entry.insert(0,0)
    d_entry.delete(0,END)
    d_entry.insert(0,0)
    e_entry.delete(0,END)
    e_entry.insert(0,0)
    f_entry.delete(0,END)
    f_entry.insert(0,0)
    g_entry.delete(0,END)
    g_entry.insert(0,0)
    h_entry.delete(0,END)
    h_entry.insert(0,0)
    i_entry.delete(0,END)
    i_entry.insert(0,0)
    j_entry.delete(0,END)
    j_entry.insert(0,0)
    k_entry.delete(0,END)
    k_entry.insert(0,0)
    l12_entry.delete(0,END)
    l12_entry.insert(0,0)
    cost_entry.delete(0,END)
    cost_entry.insert(0,0)
    gst_entry.delete(0,END)
    gst_entry.insert(0,0)
    w_entry.delete(0,END)
    w_entry.insert(0,0)
    w1_entry.delete(0,END)
    w1_entry.insert(0,0)
    w2_entry.delete(0,END)
    w2_entry.insert(0,0)
    w3_entry.delete(0,END)
    w3_entry.insert(0,0)
    Total_entry.delete(0,END)
    Total_entry.insert(0,0)
    text.delete("1.0",END)
    w4_entry.delete(0,END)
    w4_entry.insert(0,0)
    w5_entry.delete(0,END)
    w5_entry.insert(0,0)
    w6_entry.delete(0,END)
    w6_entry.insert(0,0)
    w7_entry.delete(0,END)
    w7_entry.insert(0,0)
    w8_entry.delete(0,END)
    w8_entry.insert(0,0)
    w9_entry.delete(0,END)
    w9_entry.insert(0,0)
def bill():
    text.delete("1.0",END)
    data = f'''Reciept Ref {datetime.datetime.now()}
           Bill ID : {num1}
                                                   
            1.Diet coke     {a_entry.get()}  1.Apple Pie       {w_entry.get()}
            2.Coco-Cola     {b_entry.get()}  2.Hamburger       {w1_entry.get()}
            3.Mountain dew  {c_entry.get()}  3.Clam chowder    {w2_entry.get()}
            4.Red Bull      {d_entry.get()}  4.Bagel and Lox   {w3_entry.get()}
            5.Jacobs        {e_entry.get()}  5.Deep Dish Pizza {w4_entry.get()}
            6.Monster       {f_entry.get()}  6.Texas Barbecue  {w5_entry.get()}
            7.Lavazza       {g_entry.get()}  7.Hominy Grits    {w6_entry.get()}
            8.Evian         {h_entry.get()}  8.Tacos           {w7_entry.get()}
            9.Milo          {i_entry.get()}  9.PanCakes        {w8_entry.get()}
            10.Folgers      {j_entry.get()}  10.HotDogs        {w9_entry.get()}
            11.Twinings     {k_entry.get()}
       TOTAL = {Total_entry.get()}'''
    text.insert(END,data)
    tmsg.askquestion('save?','Do you want to sav this')
root.title('Food Billing System')
root.geometry('1400x900')
root.config(bg="orange")
l = Label(root,text="Food Billing System",bg="black",fg="white",font=('helvetica',50,'bold'),borderwidth="8", relief="raised")
l.pack()
f = Frame(root,highlightthickness=5, highlightbackground="gold",bg="orange", width=800, height=700, bd= 0,relief='flat')
f.pack(side="left")
la = Label(f,text="Bill",font=('helvetica',40),bg="orange")
la.place(x=310,y=320)
l12 = Label(f,text="Cost of Drinks",font=('Helvetica',19),bg="orange")
l12.place(x=0,y=400)
l12_entry = Entry(f,width=10)
l12_entry.place(x=170,y=400)
cost = Label(f,text="Cost of Food",font=('helvetica',19),bg="orange")
cost.place(x=0,y=450)
cost_entry = Entry(f,width=10)
cost_entry.place(x=170,y=450)
gst = Label(f,text="GST",font=('Helvetica',19),bg="orange")
gst.place(x=0,y=500)
gst_entry = Entry(f,width=10)
gst_entry.place(x=170,y=500)
Total = Label(f,text="Total",font=('helvetica',19),bg="orange")
Total.place(x=0,y=550)
Total_entry = Entry(f,width=20)
Total_entry.place(x=170,y=550)
f1 = Frame(f,height=328,width=400,highlightthickness=5, highlightbackground="gold",bg="orange",relief='flat')
f1.place(x=0,y=0)
f2 = Frame(f,height=328,width=400,highlightthickness=5, highlightbackground="gold",bg="orange",relief='flat')
f2.place(x=390,y=0)
text = Text(root)
text.pack(side="left")
text.config(highlightbackground = "gold")
but = Button(text,bg="orange",height=2,width=6,text="Total",command=total)
but.place(x=0,y=330)
bu1 = Button(text,bg="orange",height=2,width=6,text="Reset",command=clear)
bu1.place(x=50,y=330)
a = Label(f1,text="Diet Coke",font=('Helvetica',19),bg="orange")
a.place(x=0,y=0)
but2 = Button(text,bg="orange",text="Bill",command=bill,height=2,width=6)
but2.place(x=100,y=330)
but3 = Button(text,bg="orange",text="Exit",command=root.destroy,height=2,width=6)
but3.place(x=150,y=330)
a_entry = Entry(f1,width=6,textvariable=quan)
a_entry.place(x=320,y=-1)
b = Label(f1,text="Coco Cola",font=('Helvetica',19),bg="orange")
b.place(x=0,y=28)
b_entry = Entry(f1,width=6,textvariable=quan1)
b_entry.place(x=320,y=27)
c = Label(f1,text="Mountain Dew",font=('Helvetica',19),bg='orange')
c.place(x=0,y=56)
c_entry  = Entry(f1,width=6,textvariable=quan2)
c_entry.place(x=320,y=54)
d = Label(f1,text="Red Bull",font=('Helvetica',19),bg="orange")
d.place(x=0,y=86)
d_entry = Entry(f1,width=6,textvariable=quan3)
d_entry.place(x=320,y=81)
e = Label(f1,text="Jacobs",font=('Helvetica',19),bg="orange")
e.place(x=0,y=114)
e_entry = Entry(f1,width=6,textvariable=quan4)
e_entry.place(x=320,y=109)
f = Label(f1,text="Monster",font=("Helvetica",19),bg="orange")
f.place(x=0,y=144)
f_entry = Entry(f1,width=6,textvariable=quan5)
f_entry.place(x=320,y=137)
g = Label(f1,text="Lavazza",font=('Helvetica',19),bg="orange")
g.place(x=0,y=174)
g_entry = Entry(f1,width=6,textvariable=quan6)
g_entry.place(x=320,y=164)
h = Label(f1,text="Evian",font=('Helvetica',19),bg="orange")
h.place(x=0,y=204)
h_entry = Entry(f1,width=6,textvariable=quan7)
h_entry.place(x=320,y=191)
i = Label(f1,text="Milo",font=('Helvetica',19),bg="orange")
i.place(x=0,y=234)
i_entry = Entry(f1,width=6,textvariable=quan8)
i_entry.place(x=320,y=218)
j = Label(f1,text="Folgers",font=('Helvetica',19),bg="orange")
j.place(x=0,y=261)
j_entry = Entry(f1,width=6,textvariable=quan9)
j_entry.place(x=320,y=245)
k = Label(f1,text="Twinings",font=('Helvetica',19),bg="orange")
k.place(x=0,y=288)
k_entry = Entry(f1,width=6,textvariable=quan10)
k_entry.place(x=320,y=272)
w = Label(f2,text="Apple Pie",font=('Helvetica',19),bg="orange")
w.place(x=0,y=0)
w_entry = Entry(f2,width=6,textvariable=newquan1)
w_entry.place(x=325,y=0)
w1 = Label(f2,text="Hamburger",font=('helvetica',19),bg="orange")
w1.place(x=0,y=28)
w1_entry = Entry(f2,width=6,textvariable=newquan2)
w1_entry.place(x=325,y=27)
w2 = Label(f2,text="Clam chowder",font=('helvetica',19),bg="orange")
w2.place(x=0,y=56)
w2_entry = Entry(f2,width=6,textvariable=newquan3)
w2_entry.place(x=325,y=54)
w3 = Label(f2,text='Bagel and Lox',font=('helvetica',19),bg="orange")
w3.place(x=0,y=84)
w3_entry = Entry(f2,width=6,textvariable=newquan4)
w3_entry.place(x=325,y=82)
w4 = Label(f2,text="Deep dish Pizza",font=("Helvetica",19),bg="orange")
w4.place(x=0,y=111)
w4_entry = Entry(f2,width=6,textvariable=newquan5)
w4_entry.place(x=325,y=110)
w5 = Label(f2,text="Texas Barbecue",font=('Helvetica',19),bg="orange")
w5.place(x=0,y=138)
w5_entry = Entry(f2,width=6,textvariable=newquan6)
w5_entry.place(x=325,y=138)
w6 = Label(f2,text="Hominy Grits ",font=('Helvetica',19),bg="orange")
w6.place(x=0,y=166)
w6_entry = Entry(f2,width=6,textvariable=newquan7)
w6_entry.place(x=325,y=166)
w7 = Label(f2,text="Tacos",font=('Helvetica',19),bg="orange")
w7.place(x=0,y=194)
w7_entry = Entry(f2,width=6,textvariable=newquan8)
w7_entry.place(x=325,y=194)
w8 = Label(f2,text="PanCakes",font=('Helvetica',19),bg="orange")
w8.place(x=0,y=222)
w8_entry = Entry(f2,width=6,textvariable=newquan9)
w8_entry.place(x=325,y=222)
w9 = Label(f2,text="HotDogs",font=('Helvetica',19),bg="orange")
w9.place(x=0,y=250)
w9_entry = Entry(f2,width=6,textvariable=newquan10)
w9_entry.place(x=325,y=250)
root.mainloop()
#End
