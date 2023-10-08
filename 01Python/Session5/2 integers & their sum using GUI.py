from tkinter import *

#### Initialization

m=Tk()
m.title("Simple calculations")
m.geometry("400x200+800+200")
m.resizable(False,False)   
m.configure(background="Grey")

#### Reverse string function
v=StringVar()
v.set('Sum')  #Default radiobutton
def operation():
    operator=v.get()
    operand1=int(textbox1.get())
    operand2=int(textbox2.get())
    if operator == 'Sum':
        answer= operand1+operand2
        sign='+'
    if operator=='Sub':
        answer=operand1-operand2
        sign='-'

    label3.config(text=f"Answer = {operand1} {sign} {operand2} = { answer}")


#### widgets

label1=Label(m,background="grey",text="Enter the first number ",font="bold")
label2=Label(m,background="grey",text="Enter the second number ",font="bold")
label3=Label(m,background="grey",foreground="DArk blue",font="bold") 
textbox1=Entry(m,foreground="black",text="num1")
textbox2=Entry(m,foreground="black",text="num2")
button1=Button(m,foreground="black",text="calculate",command=operation,font="bold")   

Op1=Radiobutton(m,text='Sum', variable=v, value='Sum',background="grey")
Op2=Radiobutton(m,text='Sub', variable=v, value='Sub',background="grey")



label1.grid(row=0,column=0,pady=10)
label2.grid(row=1,column=0,pady=10)
label3.grid(row=2,column=1,pady=10)
textbox1.grid(row = 0 , column=1)
textbox2.grid(row = 1 , column=1)
button1.grid(row=3,column=1)
Op1.grid(row=2,column=0)
Op2.grid(row=3,column=0)





m.mainloop()