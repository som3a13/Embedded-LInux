from tkinter import *

#### Initialization

m=Tk()
m.title("Reverse String")
m.geometry("380x140+800+200")
m.resizable(False,False)   
m.configure(background="Grey")

#### Reverse string function
label2=StringVar()
def reverse():
    original_string=textbox1.get()
    reversed_string="".join(reversed(original_string))
    label2.config(text=reversed_string)
    



#### widgets

label1=Label(m,background="grey",text="String to be Reveresed: ",font="bold")
label2=Label(m,background="grey",foreground="DArk blue",font="bold") 
textbox1=Entry(m,foreground="black",text="String")
button1=Button(m,foreground="black",text="Reverse",command=reverse,font="bold")   

label1.grid(row=0,column=0,pady=10)
textbox1.grid(row = 0 , column=1)
label2.grid(row=1,column=1)
button1.grid(row=2,column=1)






m.mainloop()