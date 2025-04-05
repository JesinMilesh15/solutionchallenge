import time
import tkinter
from tkinter import *
import mysql.connector
from tkinter.font import Font
from tkinter import messagebox
from PIL import Image,ImageTk
import login
import forgetpass

class start:
    def __init__(self):
        win= Tk()
        win.title("Signup")
        win.state("zoomed")
        win.config(background="#ffe633")

        signup = Image.open("image\\signup.jpg")
        image = ImageTk.PhotoImage(file="image\\signup.jpg")
        lbl = Label(win, image=image)
        lbl.place(x=0, y=0)

        frm = Frame(win, width=820, height=700, bd=2, relief="raised")
        frm.place(x=350, y=70)
        lab = Label(frm, text="Signup", fg="#a31fcd", font=("arial", 30, "bold"))
        lab.place(x=350, y=20)



        def focusnamin(event):
            if namen.get() == "Enter the Name..":
                namen.delete(0, "end")

        def focusnamout(event):

            if namen.get() == "":
                namen.insert(0, "Enter the Name..")

        def focuspassout(event):

            if pasen.get() == "":
                pasen.insert(0, "Create a Password..")

        def focuspassin(event):

            if pasen.get() == "Create a Password..":
                pasen.delete(0, "end")

        def focusrepassout(event):

            if reen.get() == "":
                reen.insert(0, "Re Enter..")

        def focusrepassin(event):

            if reen.get() == "Re Enter..":
                reen.delete(0, "end")
        def focusageout(event):

            if ageen.get() == "":
                ageen.insert(0, "Enter the Age..")

        def focusagein(event):

            if ageen.get() == "Enter the Age..":
                ageen.delete(0, "end")
        def focusmobout(event):

            if mben.get() == "":
                mben.insert(0, "Enter the Mobile No..")

        def focusmobin(event):

            if mben.get() == "Enter the Mobile No..":
                mben.delete(0, "end")
        def focusdobout(event):

            if doben.get() == "":
                doben.insert(0, "Enter the DOB..")

        def focusdobin(event):

            if doben.get() == "Enter the DOB..":
                doben.delete(0, "end")
        def focusemout(event):

            if emen.get() == "":
                emen.insert(0, "Enter the Email..")

        def focusemin(event):

            if emen.get() == "Enter the Email..":
                emen.delete(0, "end")
        def focususout(event):

            if usen.get() == "":
                usen.insert(0, "Create a Username..")

        def focususin(event):

            if usen.get() == "Create a Username..":
                usen.delete(0, "end")

        lblnam = Label(frm, text="Name", fg="black", font=("times", 20, "bold"))
        lblnam.place(x=50, y=160)
        namen = Entry(frm, width=40, bd=1)
        namen.place(x=170, y=170)
        namen.insert(0,"Enter the Name..")
        namen.focus()
        namen.bind("<FocusIn>", focusnamin)
        namen.bind("<FocusOut>", focusnamout)

        lblage = Label(frm, text="Age", fg="black", font=("times", 20, "bold"))
        lblage.place(x=450, y=160)
        ageen = Entry(frm, width=40, bd=1)
        ageen.place(x=510, y=170)
        ageen.insert(0, "Enter the Age..")
        ageen.bind("<FocusIn>", focusagein)
        ageen.bind("<FocusOut>", focusageout)


        lbldob = Label(frm, text="DOB", fg="black", font=("times", 20, "bold"))
        lbldob.place(x=50, y=260)
        doben = Entry(frm, width=40, bd=1)
        doben.place(x=170, y=270)
        doben.insert(0, "Enter the DOB..")
        doben.bind("<FocusIn>", focusdobin)
        doben.bind("<FocusOut>", focusdobout)



        lblmb = Label(frm, text="Mobile", fg="black", font=("times", 20, "bold"))
        lblmb.place(x=450, y=260)
        mben = Entry(frm, width=40, bd=1)
        mben.place(x=540, y=270)
        mben.insert(0, "Enter the Mobile No..")
        mben.bind("<FocusIn>", focusmobin)
        mben.bind("<FocusOut>", focusmobout)


        lalem = Label(frm, text="Email", fg="black", font=("times", 20, "bold"))
        lalem.place(x=50, y=360)
        emen = Entry(frm, width=40, bd=1)
        emen.place(x=170, y=370)
        emen.insert(0, "Enter the Email..")
        emen.bind("<FocusIn>", focusemin)
        emen.bind("<FocusOut>", focusemout)



        lblus = Label(frm, text="Username", fg="black", font=("times", 20, "bold"))
        lblus.place(x=420, y=360)
        usen = Entry(frm, width=40, bd=1)
        usen.place(x=550, y=370)
        usen.insert(0, "Create a Username..")
        usen.bind("<FocusIn>", focususin)
        usen.bind("<FocusOut>", focususout)


        lalpas = Label(frm, text="Password", fg="black", font=("times", 20, "bold"))
        lalpas.place(x=50, y=460)
        pasen = Entry(frm, width=40, bd=1)
        pasen.place(x=170, y=470)
        pasen.insert(0, "Create a Password..")
        pasen.bind("<FocusIn>", focuspassin)
        pasen.bind("<FocusOut>", focuspassout)


        lblre= Label(frm, text="Re-Enter", fg="black", font=("times", 20, "bold"))
        lblre.place(x=430, y=460)
        reen = Entry(frm, width=40, bd=1,show="*")
        reen.place(x=550, y=470)
        reen.insert(0, "Re Enter..")
        reen.bind("<FocusIn>", focusrepassin)
        reen.bind("<FocusOut>", focusrepassout)

        def signup():
            if namen.get()=="" or ageen.get()=="" or doben.get()=="" or mben.get()=="" or emen.get()=="" or usen.get()=="" or pasen.get()=="" or reen.get()=="":
                messagebox.showerror("Error","Please Fill all Fields...!!!")
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")
                    cur = con.cursor()
                    data="create database if not exists user"
                    cur.execute(data)
                    qry = "use user"
                    cur.execute(qry)
                    table = "create table if not exists signup(ID int primary key auto_increment not null,Name char(100) not null,Age int not null,Date_of_Birth varchar(100) not null,Mobile_No bigint not null,Email_Id varchar(100) not null,Username varchar(100) not null,Password varchar(100) not null)"
                    cur.execute(table)
                except:
                    print("Table Exists")
                    return
                if pasen.get()==reen.get():
                    qry = "insert into signup(Name,Age,Date_of_Birth,Mobile_No,Email_Id,Username,Password) values(%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(qry, (namen.get(),ageen.get(),doben.get(),mben.get(),emen.get(),usen.get(),pasen.get()))
                    con.commit()
                    messagebox.showinfo("Success","Account Created")
                    clear()

                else:
                    messagebox.showerror("Error","Password Does not Match...!!")

        def clear():
            namen.delete(0,"end")
            ageen.delete(0, "end")
            doben.delete(0, "end")
            mben.delete(0,"end")
            emen.delete(0,"end")
            usen.delete(0, "end")
            pasen.delete(0, "end")
            reen.delete(0,"end")
            namen.focus()
        def lob():
            win.destroy()
            ob=login.login()
        def forget():
            win.destroy()
            ob=forgetpass.forget()


        lobtn = Button(frm, text="Signup", width=10, height=1, font=("times", 15), bg="#a31fcd", fg="white",activebackground="white", activeforeground="black",command=signup)
        lobtn.place(x=390, y=600)

        lobtn1 = Button(frm, text="Login", width=10, height=1, font=("times", 15), bg="white", fg="#a31fcd",activebackground="white", activeforeground="black", command=lob)
        lobtn1.place(x=210, y=540)

        lobtn2 = Button(frm, text="Forget Password", width=15, height=1, font=("times", 15), bg="white", fg="#a31fcd",activebackground="white", activeforeground="black", command=forget)
        lobtn2.place(x=550, y=540)

        win.mainloop()





