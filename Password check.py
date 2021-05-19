'''Python Password Checker BY MOATAZ HARRABI (https://github.com/harrabi04)'''
from tkinter import *
from tkinter import messagebox
window= Tk()
def check(): 
    Maj=False
    Space=False
    Special=False
    num=False
    global pwd 
    pwd = entry.get()
    pwd=str(pwd)
    D={"#":5,'"':5,"'":5,"%":4,"&":4,"$":4,"!":3,"(":3,")":3,"@":3,"+":2,"*":2,"-":2,".":2,"=":2}    
    w=0
    """Check for conditions"""
    for i in pwd:
        if i.isupper():
            Maj=True
            w += 1
            break
    for i in pwd:
        if i==' ':
            Space=True
            w += + 1
            break
    for i in pwd:
        if i.isnumeric():
            num=True
            w+=1
            break
    for i in pwd:
        for j in D:
            if i==j:
             w=w+D[j]
             Special=True
    P=len(pwd)+w
    if P == len(pwd) or pwd.isnumeric() :
        l= Label(text="Weak password", font=("Arial", 25)).place(x=200,y=120, anchor=CENTER)
    elif P >= 1.1*len(pwd) and P < 1.3 * len(pwd):
        l= Label(text="Medium password", font=("Arial", 25)).place(x=200,y=120, anchor=CENTER)
    elif P >= 1.3 * len(pwd):
        l= Label(text="Strong  password", font=("Arial", 25)).place(x=200,y=120, anchor=CENTER)
    if Maj==False:
        messagebox.showinfo("No Maj", "Password doesnt contain UpperCase")
        return
    if num == False:
        messagebox.showinfo("No Numbers", "Password doesnt contain numbers")
        return
    if Space==False:
        messagebox.showinfo("No Space", "Password doesnt contain Space")
        return
    if len(pwd) < 8:
        messagebox.showinfo("Short password", "Enter a password with more than 8 character")
        return
    if Special == False:
        messagebox.showinfo("No Special","Password doesnt contain special char \n Special character are: # \" ' % & $ ! ( ) @ + * - . = ")  
    
entry = StringVar()
window.iconbitmap("Lock.ico")
window.geometry("400x300")
window.title("Password Checker")
label=Label(text='Enter your password to check', width=40, height=10, font=20 ).place(x=200,y=40, anchor=CENTER)
pwdnput=Entry(textvariable=entry, width=35).place(x=200,y=80, anchor=CENTER)
Check= Button(text="Check" ,width=8, height=2, bd=5, command=check).place(x=200,y=180, anchor=CENTER)
window.mainloop()