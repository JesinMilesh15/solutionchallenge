import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import time
import mysql.connector
from PIL import  Image, ImageTk
from tkinter import ttk

import Content
import forgetpass
import signup
from qrgen import qr
import Bank



class login:
    def __init__(self):
        root = Tk()
        root.title("Login System")
        root.state("zoomed")
        root.config(background="lightblue")
        login = Image.open("image\\login.jpg")
        image = ImageTk.PhotoImage(file="image\\login.jpg")
        lbl = Label(root, image=image)
        lbl.place(x=0, y=0)

        #frm = Frame(root, width=550, height=470, bd=2, relief="raised")
        #frm.place(x=480, y=250)
        lab = Label(root,text="Login",fg="Blue",font=("arial",30,"bold"))
        lab.place(x=730,y=290)


        def focusin(event):
            if usen.get()=="Enter the Username..":
                usen.delete(0,"end")
        def focusout(event):

            if usen.get()=="":
                usen.insert(0,"Enter the Username..")
        def focuspassout(event):

            if pasen.get()=="":
                pasen.insert(0, "Enter..")
        def focuspassin(event):

            if pasen.get()=="Enter..":
                pasen.delete(0, "end")

        lblus = Label(root,text="Username",fg="black",font=("times",20,"bold"))
        lblus.place(x=450,y=450)
        usen = Entry(root,width=50,bd=1,)
        usen.place(x=650,y=460)
        usen.insert(0,"Enter the Username..")
        usen.focus()
        usen.bind("<FocusIn>",focusin)
        usen.bind("<FocusOut>",focusout)


        lalpas = Label(root,text="Password",fg="black",font=("times",20,"bold"))
        lalpas.place(x=450,y=550)
        pasen = Entry(root,width=50,bd=1,show=".")
        pasen.insert(0,"Enter..")
        pasen.place(x=650,y=560)
        pasen.bind("<FocusIn>",focuspassin)
        pasen.bind("<FocusOut>",focuspassout)

        def Login():
            if  usen.get()=="Enter the Username.." or pasen.get()=="Enter the Password..":
                messagebox.showerror("Invalid","Please Fill all Fields..!!")
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")
                    cur=con.cursor()
                except:
                    messagebox.showerror("Not Found","Username and Password not found")
                    trial_no()
                    return
                qry="use user"
                cur.execute(qry)
                qry="select ID,Username,Password from signup where Username=%s and Password=%s"
                cur.execute(qry,(usen.get(),pasen.get()))
                result=cur.fetchone()
                if result==None:
                    messagebox.showerror("Not Found ","Username and Password not found ")
                    trial_no()
                else:
                    root.destroy()
                    ob = Bank.bank()

        global limit
        limit = 0
        def trial_no():
            global limit
            limit += 1
            if limit==3:
                messagebox.showwarning("Warning","You have tried more than the limit")
                messagebox.showinfo("Signup", "Username and Password not found Kindly Signup....")
                messagebox.showinfo("Loading", "Loading...Please Wait..!!")
                time.sleep(3)
                Clear()
                sign()

        def Clear():
            usen.delete(0, "end")
            pasen.delete(0, "end")


        def sign():
            root.destroy()
            ob=signup.start()


        def forpass():
            root.destroy()
            b=forgetpass.forget()

        lobtn = Button(root,text="Login",width=10,height=1,font=("times",15),bg="Blue",fg="white",activebackground="white",activeforeground="black",command=Login)
        lobtn.place(x=730,y=730)

        forbtn = Button(root,text="Forget Password",width=15,height=1,font=("times",15),bg="white",fg="blue",activebackground="white",activeforeground="black",command=forpass)
        forbtn.place(x=450,y=650)

        signbtn = Button(root,text="New User",width=15,height=1,font=("times",15),bg="white",fg="blue",activebackground="white",activeforeground="black",command=sign)
        signbtn.place(x=950,y=650)
        root.mainloop()
ob=login()


