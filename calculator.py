from tkinter import *
from tkinter import messagebox
import math
screen =Tk()#for screen of calculator
screen.title("My calculator")#screen_title
screen.configure(bg="blue")
screen.iconbitmap("cal.ico")
screen.maxsize(width=1000,height=450)
screen.minsize(width=362,height=450)
screen.geometry('362x488')#screen size

def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)

def clear():
    global operator
    operator =" "  
    tex.set(operator)  

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo("Notification","Try again something is wrong",parent = screen)    

def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification","Try again something is wrong",parent = screen)


def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator) 
    except:
        messagebox.showinfo("Notification","Try again something is wrong",parent = screen)   


def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator) 
    except:
        messagebox.showinfo("Notification","Try again something is wrong",parent = screen)


def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator) 
    except:
        messagebox.showinfo("Notification","Try again something is wrong",parent = screen)   


def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator) 
    except:
        messagebox.showinfo("Notification","Try again something is wrong",parent = screen)                         




def on_enter7(e):
    btn7.configure(bg="red")    
def on_leave7(e):
    btn7.configure(bg="powderblue") 

def on_enter8(f):
    btn8.configure(bg="red")    
def on_leave8(f):
    btn8.configure(bg="powderblue")    
            
def on_enter9(e):
    btn9.configure(bg="red")    
def on_leave9(e):
    btn9.configure(bg="powderblue")   

def on_enteradd(e):
    btnadd.configure(bg="red")    
def on_leaveadd(e):
    btnadd.configure(bg="powderblue")    


def on_enter4(e):
    btn4.configure(bg="red")    
def on_leave4(e):
    btn4.configure(bg="powderblue")    

def on_enter5(e):
    btn5.configure(bg="red")    
def on_leave5(e):
    btn5.configure(bg="powderblue")    


def on_enter6(e):
    btn6.configure(bg="red")    
def on_leave6(e):
    btn6.configure(bg="powderblue")    
  


def on_entersubt(e):
    btnsubt.configure(bg="red")    
def on_leavesubt(e):
    btnsubt.configure(bg="powderblue")    


def on_enter1(e):
    btn1.configure(bg="red")    
def on_leave1(e):
    btn1.configure(bg="powderblue")   


def on_enter2(e):
    btn2.configure(bg="red")    
def on_leave2(e):
    btn2.configure(bg="powderblue")    


def on_enter3(e):
    btn3.configure(bg="red")    
def on_leave3(e):
    btn3.configure(bg="powderblue")   

def on_entermul(e):
    btnmul.configure(bg="red")    
def on_leavemul(e):
    btnmul.configure(bg="powderblue") 

def on_enter0(e):
    btn0.configure(bg="red")    
def on_leave0(e):
    btn0.configure(bg="powderblue") 

def on_enterCLR(e):
    btnCLR.configure(bg="red")    
def on_leaveCLR(e):
    btnCLR.configure(bg="powderblue")

def on_enterEQ(e):
    btnEQ.configure(bg="red")    
def on_leaveEQ(e):
    btnEQ.configure(bg="powderblue")      

def on_enterDIV(e):
    btnDIV.configure(bg="red")    
def on_leaveDIV(e):
    btnDIV.configure(bg="powderblue")

def on_enterenter(e):
    entry1.configure(bg="red",fg="white")
def on_enterleave(e):
    entry1.configure(bg="orange",fg="black")   

def on_entersin(e):
    btnsin.configure(bg="red")    
def on_leavesin(e):
    btnsin.configure(bg="powderblue")  

def on_entercos(e):
    btncos.configure(bg="red")    
def on_leavecos(e):
    btncos.configure(bg="powderblue") 

def on_entertan(e):
    btntan.configure(bg="red")    
def on_leavetan(e):
    btntan.configure(bg="powderblue")  


def on_entersqrt(e):
    btnsqrt.configure(bg="red")    
def on_leavesqrt(e):
    btnsqrt.configure(bg="powderblue")    

def on_enterlog(e):
    btnlog.configure(bg="red")    
def on_leavelog(e):
    btnlog.configure(bg="powderblue")          


tex = StringVar()
operator  = " "

entry1= Entry(screen,bg="orange",font=("aerial",20,"italic bold"),bd='30',justify="right",textvariable = tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=1,column=0)

entry1.bind("<Enter>",on_enterenter)
entry1.bind("<Leave>",on_enterleave)

btn7.bind("<Enter>",on_enter7)
btn7.bind("<Leave>",on_leave7)

btn8 = Button(screen,text="8",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(8),activebackground="blue",activeforeground="red",bg="powder blue")
btn8.grid(row=1,column=1)

btn8.bind("<Enter>",on_enter8)
btn8.bind("<Leave>",on_leave8)

btn9 = Button(screen,text="9",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(9),activebackground="blue",activeforeground="red",bg="powder blue")
btn9.grid(row=1,column=2)

btn9.bind("<Enter>",on_enter9)
btn9.bind("<Leave>",on_leave9)

btnadd = Button(screen,text="+",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click("+"),activebackground="blue",activeforeground="red",bg="powder blue")
btnadd.grid(row=1,column=3)

btnadd.bind("<Enter>",on_enteradd)
btnadd.bind("<Leave>",on_leaveadd)

btn4 = Button(screen,text="4",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(4),activebackground="blue",activeforeground="red",bg="powder blue")
btn4.grid(row=2,column=0)

btn4.bind("<Enter>",on_enter4)
btn4.bind("<Leave>",on_leave4)

btn5 = Button(screen,text="5",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(5),activebackground="blue",activeforeground="red",bg = "powder blue")
btn5.grid(row=2,column=1)

btn5.bind("<Enter>",on_enter5)
btn5.bind("<Leave>",on_leave5)

btn6 = Button(screen,text="6",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(6),activebackground="blue",activeforeground="red",bg = "powder blue")
btn6.grid(row=2,column=2)

btn6.bind("<Enter>",on_enter6)
btn6.bind("<Leave>",on_leave6)

btnsubt = Button(screen,text="-",font=("aerial",18,"italic bold"),bd='8',padx=18,pady=16,command=lambda:click("-"),activebackground="blue",activeforeground="red",bg= "powder blue")
btnsubt.grid(row=2,column=3)

btnsubt.bind("<Enter>",on_entersubt)
btnsubt.bind("<Leave>",on_leavesubt)

btn1 = Button(screen,text="1",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(1),activebackground="blue",activeforeground="red",bg = "powder blue")
btn1.grid(row=3,column=0)

btn1.bind("<Enter>",on_enter1)
btn1.bind("<Leave>",on_leave1)

btn2 = Button(screen,text="2",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(2),activebackground="blue",activeforeground="red",bg = "powder blue")
btn2.grid(row=3,column=1)

btn2.bind("<Enter>",on_enter2)
btn2.bind("<Leave>",on_leave2)

btn3 = Button(screen,text="3",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(3),activebackground="blue",activeforeground="red",bg = "powder blue")
btn3.grid(row=3,column=2)

btn3.bind("<Enter>",on_enter3)
btn3.bind("<Leave>",on_leave3)

btnmul = Button(screen,text="*",font=("aerial",15,"italic bold"),bd='8',padx=19,pady=16,command=lambda:click("*"),activebackground="blue",activeforeground="red",bg = "powder blue")
btnmul.grid(row=3,column=3)

btnmul.bind("<Enter>",on_entermul)
btnmul.bind("<Leave>",on_leavemul)

btn0 = Button(screen,text="0",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(0),activebackground="blue",activeforeground="red",bg = "powder blue")
btn0.grid(row=4,column=0)

btn0.bind("<Enter>",on_enter0)
btn0.bind("<Leave>",on_leave0)

btnCLR = Button(screen,text="C",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=clear,activebackground="blue",activeforeground="red",bg = "powder blue")
btnCLR.grid(row=4,column=1)

btnCLR.bind("<Enter>",on_enterCLR)
btnCLR.bind("<Leave>",on_leaveCLR)

btnEQ = Button(screen,text="=",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=equal,activebackground="blue",activeforeground="red",bg = "powder blue")
btnEQ.grid(row=4,column=2)

btnEQ.bind("<Enter>",on_enterEQ)
btnEQ.bind("<Leave>",on_leaveEQ)

btnDIV = Button(screen,text="/",font=("aerial",15,"italic bold"),bd='8',padx=19,pady=16,command=lambda:click("/"),activebackground="blue",activeforeground="red",bg = "powder blue")
btnDIV.grid(row=4,column=3)

btnDIV.bind("<Enter>",on_enterDIV)
btnDIV.bind("<Leave>",on_leaveDIV)

####advance one
btnsin = Button(screen,text="sin",font=("aerial",15,"italic bold"),bd='8',padx=19,pady=16,command=cmsin,activebackground="blue",activeforeground="red",bg = "powder blue")
btnsin.grid(row=0,column=4)

btnsin.bind("<Enter>",on_entersin)
btnsin.bind("<Leave>",on_leavesin)

btncos = Button(screen,text="cos",font=("aerial",15,"italic bold"),bd='8',padx=19,pady=16,command=cmcos,activebackground="blue",activeforeground="red",bg = "powder blue")
btncos.grid(row=1,column=4)

btncos.bind("<Enter>",on_entercos)
btncos.bind("<Leave>",on_leavecos)

btntan = Button(screen,text="tan",font=("aerial",15,"italic bold"),bd='8',padx=19,pady=16,command=cmtan,activebackground="blue",activeforeground="red",bg = "powder blue")
btntan.grid(row=2,column=4)

btntan.bind("<Enter>",on_entertan)
btntan.bind("<Leave>",on_leavetan)

btnsqrt = Button(screen,text="sqrt",font=("aerial",15,"italic bold"),bd='8',padx=19,pady=16,command=cmsqrt,activebackground="blue",activeforeground="red",bg = "powder blue")
btnsqrt.grid(row=3,column=4)

btnsqrt.bind("<Enter>",on_entersqrt)
btnsqrt.bind("<Leave>",on_leavesqrt)


btnlog = Button(screen,text="log",font=("aerial",15,"italic bold"),bd='8',padx=19,pady=16,command=cmlog,activebackground="blue",activeforeground="red",bg =  "powder blue")
btnlog.grid(row=4,column=4)

btnlog.bind("<Enter>",on_enterlog)
btnlog.bind("<Leave>",on_leavelog)

###########################################################################################################

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=0,column=5)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=1,column=5)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=2,column=5)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=3,column=5)


btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=4,column=5)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=0,column=6)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=1,column=6)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=2,column=6)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=3,column=6)


btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=4,column=6)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=0,column=7)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=1,column=7)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=2,column=7)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=3,column=7)


btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=4,column=7)



btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=0,column=8)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=1,column=8)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=2,column=8)

btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=3,column=8)


btn7 = Button(screen,text="7",font=("aerial",15,"italic bold"),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground="blue",activeforeground="red",bg="powder blue")
btn7.grid(row=4,column=8)










screen.mainloop()#loop that will run again and again