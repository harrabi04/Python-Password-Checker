'''Python Password Checker'''
from tkinter import *
pwd1=''
window= Tk()
window.geometry("400x300")
window.title("Password Checker/generator")
label=Label(text='Enter your password to check', width=40, height=10, font=20 ).place(x=200,y=40, anchor=CENTER)
input1=Entry(textvariable=pwd1).place(x=200,y=80, anchor=CENTER)
Check= Button(text="Check" ,width=8, height=2, bd=5).place(x=200,y=180, anchor=CENTER)
generate=Button(text="Generate",width=8, height=2, bd=5).place(x=200, y=250, anchor=CENTER)
window.mainloop()
Maj=False
Space=False
Special=False
num=False
def printonwindw()
    if Maj==False:
        print("Password doesnt contain Maj".center(50,"*"))
    if Space==False:
        print("Password doesnt contain Space".center(50,"*"))

def check(pwd):
    D={"#":5,'"':5,"'":5,"%":4,"&":4,"$":4,"!":3,"(":3,")":3,"@":3,"+":2,"*":2,"-":2,".":2,"=":2}    
    while len(pwd) < 8:
        print("Enter a password with more than 8 character".center(50,"*"))
        pwd = input("Please enter your password to check: ")
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
    if num == False:
        print("Password doesnt contain numbers".center(50,"*"))
    for i in pwd:
        for j in D:
            if i==j:
             w=w+D[j]
             Special=True
    if Special == False:
        print("Password doesnt contain special char".center(50,"*"))
        print("Special character are: # \" ' % & $ ! ( ) @ + * - . = ")

    P=len(pwd)+w
    if P == len(pwd) and P :
        print("weak password".center(30,"/"))
    if P >= 1.1*len(pwd) and P < 1.4 * len(pwd):
        print("medium password".center(30,"/"))
    if P >= 1.4 * len(pwd):
        print("Strong password".center(30,"/"))