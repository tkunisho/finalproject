"""
Program: KunishoTakaharuFinalProject
Author: Takaharu Kunisho
Last date Modified: Mar/14/2022

This is a program that user creates their own ice cream and display the total purchase price.
"""

import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

def subWindow():
    sub_window = tk.Toplevel()
    sub_window.geometry("550x300")
    sub_window.title("Exit")

    mainlbl1 = tk.Label(sub_window,
                 text = "Thank you for coming!\n Come Again!",
                 bd=2,
                 relief="raised",
                 bg="blue",
                 fg="white",
                 font="Broadway 20 bold",
                 width = 30,
                 height = 4)  
    mainlbl1.place(x=10, y=10)
    button10 = tk.Button(sub_window, text="Exit", bg="red", font="Broadway 13 bold",  width=15, height = 3, command=sub_window.destroy)
    button10.place(x=200, y=200)


my_window = Tk()
my_window.geometry("900x800")
my_window.title("TK Ice Cream Store")
welcome1 = Label(my_window,
                 text = "WELCOME TO",
                 bd=4,
                 relief="raised",
                 bg="blue",
                 fg="white",
                 font="Broadway 32 bold",
                 width = 20,
                 height = 2,
                 padx=20)  
welcome1.place(x=160, y=50)

welcome2 = Label(my_window,
                 text = "TK Ice Cream Store",
                 bd=4,
                 font="Broadway 32 bold",
                 width = 20,
                 height = 2,
                 padx=20)  
welcome2.place(x=160, y=170)

image1 = PhotoImage(file="ice1.gif")
lbl0 = Label(my_window, image=image1)
lbl0.place(x=60, y=200)


image2 = PhotoImage(file="ice2.gif")

lbl1 = Label(my_window, image=image2)
lbl1.place(x=720, y=200)


lbl2 =Label(text="Please Enter your name: ", bg="white", font="Broadway 15 bold")
lbl2.place(x=250, y=280)

txt = Entry(width=20)
txt.place(x=510, y= 285)
cname = txt.get()

lbl3 = Label(text="Please choose your size", bg="white", font="Broadway 15 bold")
lbl3.place(x=20, y=350)

lbl4 = Label(text="Please choose your flavor", bg="white", font="Broadway 15 bold")
lbl4.place(x=310, y=350)

lbl5 = Label(text="Please choose your toppings", bg="white", font="Broadway 15 bold")
lbl5.place(x=600, y=350)


sizetext = ["Small ($4.00)", "Medium ($4.50)", "Large ($5.50)"]
var = IntVar()
var.set(0) # auto select value = 0 default.
for i in range(len(sizetext)):
    size = Radiobutton(my_window, value=i, variable=var, text=sizetext[i], font="Broadway 12")
    size.place(x=70, y=410 + (i * 40))


flavortext = ["Vanilla (+$0.00)", "Chocolate (+$1.00)", "Strawberry (+$2.00)"]
fvar = IntVar()
for i in range(len(flavortext)):
    flavor = Radiobutton(my_window, value=i, variable=fvar, text= flavortext[i], font="Broadway 12")
    flavor.place(x=360, y=410 + (i * 40))



def allorder():
    total = 0
    message = ""
    choice = var.get()
    choice1 = fvar.get()
    choice2 = CheckVar1.get()
    choice3 = CheckVar2.get()
    choice4 = CheckVar3.get()
    
    if choice == 0:
        total += 4
        message += "Size: Small\n"
    elif choice == 1:
        total += 4.5
        message += "Size: Medium\n"
    elif choice == 2:
        total += 5.5
        message += "Size: Large\n"

    if choice1 ==0:
        total +=0
        message += "Flavor: Vanilla\n"
    elif choice1 ==1:
        total +=1
        message += "Flavor: Chocolate\n"
    elif choice1 ==2:
        total +=2
        message += "Flavor: Strawberry\n"

    if choice2 == 1:
        total += 0.5
        message += "Topping: Sprinkle\n"
    if choice3 == 1:
        total += 1
        message += "Topping: Caramel\n"
    if choice4 == 1:
        total += 1.5
        message += "Topping: Hot Fudge\n"

    response = messagebox.askyesno("Your Order", "Please Confirm Your Order\n\n" + message)
    if response == True:
        lbl7["text"] = "Your Order has been placed. Please Exit Now"
    elif response == False:
        messagebox.showinfo("Error", "please try again")
    #return total
    #return messagebox.askquestion("Your Order", "Please Confirm Your Order\n" + message)


def totalprice():
    total = 0.00
    message = ""
    choice = var.get()
    choice1 = fvar.get()
    choice2 = CheckVar1.get()
    choice3 = CheckVar2.get()
    choice4 = CheckVar3.get()
    
    if choice == 0:
        total += 4.00
        message += "Small\n"
    elif choice == 1:
        total += 4.50
        message += "Medium\n"
    elif choice == 2:
        total += 5.50
        message += "Large\n"

    if choice1 ==0:
        total +=0.00
        message += "Vanilla\n"
    elif choice1 ==1:
        total +=1.00
        message += "Chocolate\n"
    elif choice1 ==2:
        total +=2.00
        message += "Strawberry\n"

    if choice2 == 1:
        total += 0.50
        message += "Sprinkle\n"
    if choice3 == 1:
        total += 1.00
        message += "Caramel\n"
    if choice4 == 1:
        total += 1.50
        message += "Hot Fudge\n"
    lbl6["text"] = "$" + str(total)
    #return total
    #return messagebox.showinfo("Total Price", "Your Total is: $" + str(total))

def clear_selection():
    check1.deselect()
    check2.deselect()
    check3.deselect()
    lbl6["text"] = "$ " + str("0.00")
    lbl7["text"] = " "
    text = " "

lbl5 = Label(text="Your Total is: ", font="Broadway 20")
lbl5.place(x=300, y=550)

lbl6 = Label(my_window, font="Broadway 20")
lbl6.place(x=500, y=550)

lbl7 = Label(my_window, bg="green", font="Broadway 20 bold")
lbl7.place(x=150, y=600)


CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()

check1 = Checkbutton(my_window, text="Sprinkle (+$0.50)", font="Broadway 12", variable = CheckVar1, onvalue = 1, offvalue = 0)
check1.place(x=650, y=410)

check2 = Checkbutton(my_window, text="Caramel (+$1.00)", font="Broadway 12", variable = CheckVar2, onvalue = 1, offvalue = 0)
check2.place(x=650, y=450)

check3 = Checkbutton(my_window, text="Hot Fudge (+$1.50)", font="Broadway 12", variable = CheckVar3, onvalue = 1, offvalue = 0)
check3.place(x=650, y=490)

#print(check3.cget("text"))
    

button1 = Button(my_window, text="Confirm Order", bg="blue", font="Broadway 13 bold", width=15, height = 3, command=allorder)
button1.place(x=60, y=670)

button2 = Button(my_window, text="Check Price", bg="green", font="Broadway 13 bold", width=15, height = 3, command=totalprice)
button2.place(x=260, y=670)

button3 = Button(my_window, text="Reset Price\n Topping", bg="yellow", font="Broadway 13 bold", width=15, height = 3, command=clear_selection)
button3.place(x=460, y=670)

button4 = Button(my_window, text="Exit", bg="red", font="Broadway 13 bold",  width=15, height = 3, command=subWindow)
button4.place(x=660, y=670)


my_window.mainloop()
