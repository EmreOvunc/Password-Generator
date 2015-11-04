#!/usr/bin/env python
# Writer: EmreOvunc&SimgeOzger
# Izmir University of Economics

from Tkinter import *
import string
from random import *
import tkMessageBox


def generate_func():
    text_menu.delete(1.0,END)
    rangee=int(entry_box.get())
    
    if check1var.get()==1 and check2var.get()==1 and check3var.get()==1:
        characters=string.ascii_letters+string.punctuation+string.digits                      
    elif check1var.get()==1 and check2var.get()==0 and check3var.get()==0:
        characters=string.ascii_letters
    elif check1var.get()==0 and check2var.get()==1 and check3var.get()==0:
        characters=string.punctuation
    elif check1var.get()==0 and check2var.get()==0 and check3var.get()==1:
        characters=string.digits
    elif check1var.get()==1 and check2var.get()==1 and check3var.get()==0:
        characters=string.ascii_letters+string.punctuation
    elif check1var.get()==1 and check2var.get()==0 and check3var.get()==1:
        characters=string.ascii_letters+string.digits
    elif check1var.get()==0 and check2var.get()==1 and check3var.get()==1:
        characters=string.punctuation+string.digits        
    else:
         tkMessageBox.showinfo("Error", "Please, Select at least 1 option!")

    password =  "".join(choice(characters)for x in range(rangee))
    text_menu.insert(END,password)


main_window=Tk()
header=main_window.title("PassG v1.1 ")
main_window.geometry("220x200")
#main_window.iconbitmap(r'D:\Python27\DLLs\favicon1.ico')

label_box=Label(text="Enter password length:",font='bold')
label_box.place(x=5,y=8)

entry_box=Entry(width=22,font='bold')
entry_box.place(x=10,y=35)

check1var=IntVar()
check2var=IntVar()
check3var=IntVar()

check1=Checkbutton(text="Ascii",variable=check1var,offvalue=0,onvalue=1)
check2=Checkbutton(text="Punctuation",variable=check2var,offvalue=0,onvalue=1)
check3=Checkbutton(text="Digits",variable=check3var,offvalue=0,onvalue=1)

check1.place(x=10,y=60) 
check3.place(x=62,y=60)
check2.place(x=120,y=60)

label_box=Label(text="Your new password is:",font='bold')
label_box.place(x=5,y=97)

text_menu=Text(height=1,width=22,font='bold')
text_menu.place(x=10,y=120)

button_box=Button(text="Generate",command=generate_func)
button_box.place(x=75,y=150)

programmer_box=Label(text="Emre & Simge 2015",fg='red')
programmer_box.place(x=53,y=178)

mainloop()
