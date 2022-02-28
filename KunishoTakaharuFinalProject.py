"""
Program: KunishoTakaharuFinalProject
Author: Takaharu Kunisho
Last date Modified: Mar/14/2022

This is a program that user creates their own ice cream.
The customer confirm their order, and also the user can check the total purchase price.
"""

import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

# Create the second window
def subWindow():
    sub_window = tk.Toplevel()
    sub_window.geometry("450x300") # Set the size of second window
    sub_window.title("Exit")       # Set the title of second window


    #Label for second window, setting text, font, size. 
    mainlbl1 = tk.Label(sub_window,
                 text = "Thank you for coming!\n Come Again!",
                 bd=2,
                 relief="raised",
                 bg="blue",
                 fg="white",
                 font="Broadway 20 bold",
                 width = 30,
                 height = 4)
    #Set the location of the label. 
    mainlbl1.place(x=10, y=10)


    #Create a button to exit the window. 
    button10 = tk.Button(sub_window, text="Exit", bg="red", font="Broadway 13 bold",  width=15, height = 3, command=sub_window.destroy)

    #Set the location of exit button. 
    button10.place(x=150, y=200)

# Function to correct the information of what size, flavor, and toppings the customer choose and display their order in the messagebox. 
def allorder():
    message = ""
    choice = var.get()        #Size choice from the user. 
    choice1 = fvar.get()      #Flavor choice from the user. 
    choice2 = CheckVar1.get() #Topping choice from the user (Sprinckles)
    choice3 = CheckVar2.get() #Topping choice from the user (Caramel)
    choice4 = CheckVar3.get() #Topping choice from the user (Hot Fudge)

    #Determine what size the user choose.
    #Use if-elif because the user can only choose 1 choice.
    if choice == 0:                    #Determine if the user choose small size.
        message += "Size: Small\n"     #Add text (Size: Small) to messagebox. 
    elif choice == 1:                  #Determine if the user choose medium size.
        message += "Size: Medium\n"    #Add text (Size: Medium) to messagebox.
    elif choice == 2:                  #Determine if the user choose Large size.
        message += "Size: Large\n"     #Add text (Size: Large) to messagebox.

    #Determine what flavor the user choose.
    #Use if-elif because the user can only choose 1 choice.
    if choice1 ==0:                             #Determine if the user choose vanilla flavor.
        message += "Flavor: Vanilla\n"          #Add text (Flavor: Vanilla) to messagebox.
    elif choice1 ==1:                           #Determine if the user choose chocolate flavor.
        message += "Flavor: Chocolate\n"        #Add text (Flavor: Chocolate) to messagebox.
    elif choice1 ==2:                           #Determine if the user choose strawberry flavor.
        message += "Flavor: Strawberry\n"       #Add text (Flavor: Strawberry) to messagebox.


    #Determine what topping the user choose.
    #Use ifs because the user can choose more than 1 choice.
    if choice2 == 1:                            #Determine if the user choose Large size.
        message += "Topping: Sprinkle\n"        #Add text (Topping: Sprinckles) to messagebox.
    if choice3 == 1:                            #Determine if the user choose Large size.
        message += "Topping: Caramel\n"         #Add text (Topping: Caramel) to messagebox.
    if choice4 == 1:                            #Determine if the user choose Large size.
        message += "Topping: Hot Fudge\n"       #Add text (Topping: Hot Fudge) to messagebox.

    #Display their orders in the messagebox, asking the user if their choices are correct.
    response = messagebox.askyesno("Your Order", "Please Confirm Your Order\n\n" + message)
    if response == True:                        #If the user selects "Yes" then their order is completed. 
        lbl8["text"] = "Your Order has been placed. Please Exit Now"
    elif response == False:                     #If the user selects "No" then Error message displays in the messagebox. 
        messagebox.showinfo("Error", "please try again")

# Function to correct the information of what size, flavor, and toppings the customer choose and calculate/display the total price
def totalprice(): 
    total = 0.00                  #set total price to 0.
    choice = var.get()            #determine what size the user choose. 
    choice1 = fvar.get()          #determine what flavor the user choose.
    choice2 = CheckVar1.get()     #determine if the user choose sprinkles for topping.
    choice3 = CheckVar2.get()     #determine if the user choose caramel for topping.
    choice4 = CheckVar3.get()     #determine if the user choose hot fudge for topping.

    #Determine what size the user choose. 0 for small, 1 for medium, 2 for large.
    if choice == 0:               #determine if the user choose small size.
        total += 4.00             #add $4 to total if the user choose small size. 
    elif choice == 1:             #determine if the user choose medium size.
        total += 4.50             #add $4.5 to total if the user choose medium size. 
    elif choice == 2:             #determine if the user choose large size.
        total += 5.50             #add $5.5 to total if the user choose large size. 

    #Determine what flavor the user choose. 0 for Vanilla, 1 for chocolate, 2 for strawberry
    if choice1 ==0:               #determine if the user choose Vanilla Flavor.
        total +=0.00              #add $0 to total if the user choose vanilla flavor.
    elif choice1 ==1:             #determine if the user choose Chocolate Flavor.
        total +=1.00              #add $1 to total if the user choose vanilla flavor.
    elif choice1 ==2:             #determine if the user choose Strawberry Flavor.
        total +=2.00              #add $2 to total if the user choose vanilla flavor.

    #Determine what topping the user choose. 1 for checked and 0 is unchecked
    if choice2 == 1:              #determine if the user add sprinckles.
        total += 0.50             #add $0.5 to total if the user add sprinkles.
    if choice3 == 1:              #determine if the user add caramel.
        total += 1.00             #add $1 to total if the user add caramel.
    if choice4 == 1:              #determine if the user add hot fudge.
        total += 1.50             #add $1 to total if the user add fudge.
    lbl7["text"] = "$" + str(total)   #Display the total amount at the location of lbl7

#When the user click "Reset Order", checkbox will be unchecked and total price will reset. 
def clear_selection(): 
    check1.deselect()             #uncheck the sprinkle checkbox
    check2.deselect()             #uncheck the caramel checkbox
    check3.deselect()             #uncheck the hot fudge checkbox
    lbl7["text"] = "$ " + str("0.00")  #Total price reset and disply $0
    lbl8["text"] = " "            #lbl8, which is "You order has been placed. Please exit now" will be erased. 
    

#Create the main window
my_window = Tk()
my_window.geometry("900x800")                 # Set the size of second window
my_window.title("TK Ice Cream Store")         # Set the title of second window
welcome1 = Label(my_window,                   # Creating a label, setting text, font, size.  
                 text = "WELCOME TO",
                 bd=4,
                 relief="raised",
                 bg="blue",
                 fg="white",
                 font="Broadway 32 bold",
                 width = 20,
                 height = 2,
                 padx=20)  
welcome1.place(x=160, y=50)                   #Placing the label above. 
 
welcome2 = Label(my_window,                   # Creating a label, setting text, font, size.
                 text = "TK Ice Cream Store",
                 bd=4,
                 font="Broadway 32 bold",
                 width = 20,
                 height = 2,
                 padx=20)  
welcome2.place(x=160, y=170)

image1 = PhotoImage(file="ice1.gif")          #Opening picture 1 file
lbl0 = Label(my_window, image=image1)         #Naming picture file
lbl0.place(x=60, y=200)                       #Placing picture file in the window.


image2 = PhotoImage(file="ice2.gif")          #Opening picture 1 file
lbl1 = Label(my_window, image=image2)         #Naming picture file
lbl1.place(x=720, y=200)                      #Placing picture file in the window


#Creating a label, setting text, color, font.
lbl2 =Label(text="Please Enter your name: ", bg="white", font="Broadway 15 bold")
lbl2.place(x=250, y=280)                      #Placing label in the window.

txt = Entry(width=20)                         #Creating input box
txt.place(x=510, y= 285)                      #Location of label2

#Creating a label, setting text, color, font.
lbl3 = Label(text="Please choose your size", bg="white", font="Broadway 15 bold")
lbl3.place(x=20, y=350)                       #Location of label3

#Creating a label, setting text, color, font.
lbl4 = Label(text="Please choose your flavor", bg="white", font="Broadway 15 bold")
lbl4.place(x=310, y=350)                      #Location of label4

#Creating a label, setting text, color, font.
lbl5 = Label(text="Please choose your toppings", bg="white", font="Broadway 15 bold")
lbl5.place(x=600, y=350)                      #Location of label5

#Creating radio buttons for sizes, small, medium, large.
sizetext = ["Small ($4.00)", "Medium ($4.50)", "Large ($5.50)"]
var = IntVar()
var.set(0) # auto select value = 0 default.
for i in range(len(sizetext)):
    size = Radiobutton(my_window, value=i, variable=var, text=sizetext[i], font="Broadway 12")
    size.place(x=70, y=410 + (i * 40))

#Creating radio buttons for flavors, vanilla, chocolate, strawberry.
flavortext = ["Vanilla (+$0.00)", "Chocolate (+$1.00)", "Strawberry (+$2.00)"]
fvar = IntVar()
for i in range(len(flavortext)):
    flavor = Radiobutton(my_window, value=i, variable=fvar, text= flavortext[i], font="Broadway 12")
    flavor.place(x=360, y=410 + (i * 40))

#Creating label6, setting text, color, font.
lbl6 = Label(text="Your Total is: ", font="Broadway 20")
lbl6.place(x=300, y=550)    #Location of label6

#Creating label7, setting text, color, font.
lbl7 = Label(my_window, font="Broadway 20")
lbl7.place(x=500, y=550)    #Location of label7

#Creating label8, setting text, color, font.
lbl8 = Label(my_window, bg="green", font="Broadway 20 bold")
lbl8.place(x=150, y=600)    #Location of label8


#Making checkboxs selection an integer
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()

#Creating checkbox for sprinkle
check1 = Checkbutton(my_window, text="Sprinkle (+$0.50)", font="Broadway 12", variable = CheckVar1, onvalue = 1, offvalue = 0)
check1.place(x=650, y=410)      #Location of sprinkle checkbox

#Creating checkbox for caramel
check2 = Checkbutton(my_window, text="Caramel (+$1.00)", font="Broadway 12", variable = CheckVar2, onvalue = 1, offvalue = 0)
check2.place(x=650, y=450)      #Location of caramel checkbox
  
#Creating checkbox for hot fudge
check3 = Checkbutton(my_window, text="Hot Fudge (+$1.50)", font="Broadway 12", variable = CheckVar3, onvalue = 1, offvalue = 0)
check3.place(x=650, y=490)      #Location of hot fudge checkbox

    
#Creating Confirm Order button for users to confirm their order
button1 = Button(my_window, text="Confirm Order", bg="blue", font="Broadway 13 bold", width=15, height = 3, command=allorder)
button1.place(x=60, y=670)             #Location of "Confirm Order" button

#Creating Check Price button for users to confirm their order
button2 = Button(my_window, text="Check Price", bg="green", font="Broadway 13 bold", width=15, height = 3, command=totalprice)
button2.place(x=260, y=670)            #Location of "Check Price" button

#Creating Reset button for users to confirm their order
button3 = Button(my_window, text="Reset Order", bg="yellow", font="Broadway 13 bold", width=15, height = 3, command=clear_selection)
button3.place(x=460, y=670)            #Location of "Reset Order" button

#Creating Finish Order button for users to confirm their order
button4 = Button(my_window, text="Finish Order", bg="red", font="Broadway 13 bold",  width=15, height = 3, command=subWindow)
button4.place(x=660, y=670)            #Location of "Finish Order" button


my_window.mainloop()
