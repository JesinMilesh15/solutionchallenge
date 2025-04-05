import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import time
import mysql.connector
from PIL import  Image, ImageTk
from tkinter import ttk
import mysql.connector
import forbnk
import Bank

class upbnk:
    def __init__(self):
        root = Tk()
        root.title("Update Account")
        root.state("zoomed")
        root.config(background="#ec77dc")

        upd = Image.open("image\\forbnk.png")
        image = ImageTk.PhotoImage(file="image\\forbnk.png")
        lbl = Label(root, image=image, background="#ec77dc")
        lbl.place(x=140, y=170)


        frm = Frame(root, width=550, height=650, bd=2, relief="raised")
        frm.place(x=820, y=100)
        lab = Label(frm, text="Update Account", fg="#f11bd4", font=("arial", 30, "bold"))
        lab.place(x=140, y=20)



        def focusin(event):
            if acche1.get() == "Enter the Holder Name..":
                acche1.delete(0, "end")

        def focusout(event):

            if acche1.get() == "":
                acche1.insert(0, "Enter the Holder Name..")

        def focusaccin(event):
            if accnoe1.get() == "Enter the Account No..":
                accnoe1.delete(0, "end")

        def focusaccout(event):

            if accnoe1.get() == "":
                accnoe1.insert(0, "Enter the Account No..")
        def focusmobin(event):
            if mbnoe1.get() == "Enter the Moblie No..":
                mbnoe1.delete(0, "end")

        def focusmobout(event):

            if mbnoe1.get() == "":
                mbnoe1.insert(0, "Enter the Moblie No..")

        def focuspasswin(event):

            if passwe1.get() == "Enter the Password..":
                passwe1.delete(0, "end")

        def focuspasswout(event):

            if passwe1.get() == "":
                passwe1.insert(0, "Enter the Password..")




        acch = Label(frm, text="Account Holder", fg="black", font=("times", 20, "bold"))
        acch.place(x=50, y=160)
        acche1 = Entry(frm, width=40, bd=1)
        acche1.place(x=250, y=170)
        acche1.insert(0, "Enter the Holder Name..")
        acche1.focus()
        acche1.bind("<FocusIn>", focusin)
        acche1.bind("<FocusOut>", focusout)

        accno = Label(frm, text="Account No", fg="black", font=("times", 20, "bold"))
        accno.place(x=50, y=260)
        accnoe1 = Entry(frm, width=40, bd=1)
        accnoe1.place(x=250, y=270)
        accnoe1.insert(0, "Enter the Account No..")
        accnoe1.bind("<FocusIn>", focusaccin)
        accnoe1.bind("<FocusOut>", focusaccout)

        mbno = Label(frm, text="Mobile No", fg="black", font=("times", 20, "bold"))
        mbno.place(x=50, y=360)
        mbnoe1 = Entry(frm, width=40, bd=1)
        mbnoe1.place(x=250, y=370)
        mbnoe1.insert(0, "Enter the Moblie No..")
        mbnoe1.bind("<FocusIn>", focusmobin)
        mbnoe1.bind("<FocusOut>", focusmobout)

        passw = Label(frm, text="Password", fg="black", font=("times", 20, "bold"))
        passw.place(x=50, y=460)
        passwe1 = Entry(frm, width=40, bd=1)
        passwe1.place(x=250, y=470)
        passwe1.insert(0, "Enter the Password..")
        passwe1.bind("<FocusIn>",focuspasswin)
        passwe1.bind("<FocusOut>",focuspasswout)

        def update1():
            if acche1.get() == "" or accnoe1.get() == "" or mbnoe1.get() == "" or passwe1.get() == "":
                messagebox.showerror("Error", "Please Fill all Fields...!!!")
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")
                    cur = con.cursor()
                except:
                    return
                qry = "use user"
                cur.execute(qry)
                qry = "select Password from bank where Account_No=%s"
                cur.execute(qry, (accnoe1.get(),))
                result = cur.fetchone()

                if passwe1.get() == result[0]:
                    qry = "update bank set Account_Holder=%s,Mobile_No=%s where Account_No=%s"
                    cur.execute(qry,(acche1.get(),mbnoe1.get(), accnoe1.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Account Updated Successfully")
                    clear()
                    insert()

                elif result == None:
                    messagebox.showerror("Error","Account Not Found")

                else:
                    messagebox.showerror("Error", "Password Does not Match...!!")

        def clear():
            acche1.delete(0, "end")
            accnoe1.delete(0, "end")
            mbnoe1.delete(0, "end")
            passwe1.delete(0, "end")


        def insert():
            acche1.insert(0, "Enter the Holder Name..")
            accnoe1.insert(0, "Enter the Account No..")
            mbnoe1.insert(0, "Enter the Moblie No..")
            passwe1.insert(0, "Enter the Password..")
            acche1.focus()

        def forpass():
            root.destroy()
            b = forbnk.forget()
        def new():
            root.destroy()
            ob = Bank.bank()

        lobtn = Button(frm, text="Update", width=10, height=1, font=("times", 15), bg="#f11bd4", fg="white",activebackground="white", activeforeground="black", command=update1)
        lobtn.place(x=210, y=600)

        lobtn = Button(frm, text="New User", width=10, height=1, font=("times", 15), bg="white", fg="#f11bd4",
                       activebackground="white", activeforeground="black", command=new)
        lobtn.place(x=50, y=550)

        forbtn = Button(frm, text="Forget Password", width=15, height=1, font=("times", 15), bg="white", fg="#f11bd4",activebackground="white", activeforeground="black", command=forpass)
        forbtn.place(x=350, y=550)
        root.mainloop()