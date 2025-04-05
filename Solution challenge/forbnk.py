import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox
import time
from PIL import Image,ImageTk
import Bank
import delbnk





class forget:
    def __init__(self):
        win = Tk()
        win.title("Forget Password")
        win.state("zoomed")
        win.config(background="lightpink")

        forget = Image.open("image\\forget.jpg")
        image = ImageTk.PhotoImage(file="image\\forget.jpg")
        lbl = Label(win, image=image)
        lbl.place(x=0, y=0)

        frm = Frame(win, width=550, height=470, bd=2, relief="raised")
        frm.place(x=500, y=250)
        lab = Label(frm, text="Forget Password", fg="#ff33a8", font=("arial", 30, "bold"))
        lab.place(x=140, y=20)

        def focusaccin(event):
            if accnoe1.get() == "Enter the Account No..":
                accnoe1.delete(0, "end")

        def focusaccout(event):

            if accnoe1.get() == "":
                accnoe1.insert(0, "Enter the Account No..")

        def focuspasswin(event):

            if passwe1.get() == "Create a New Password..":
                passwe1.delete(0, "end")

        def focuspasswout(event):

            if passwe1.get() == "":
                passwe1.insert(0, "Create a New Password..")

        accno = Label(frm, text="Account No", fg="black", font=("times", 20, "bold"))
        accno.place(x=50, y=160)
        accnoe1 = Entry(frm, width=40, bd=1)
        accnoe1.place(x=210, y=170)
        accnoe1.insert(0, "Enter the Account No..")
        accnoe1.bind("<FocusIn>", focusaccin)
        accnoe1.bind("<FocusOut>", focusaccout)

        passw = Label(frm, text="Password", fg="black", font=("times", 20, "bold"))
        passw.place(x=50, y=260)
        passwe1 = Entry(frm, width=40, bd=1)
        passwe1.place(x=210, y=270)
        passwe1.insert(0, "Create a New Password..")
        passwe1.bind("<FocusIn>", focuspasswin)
        passwe1.bind("<FocusOut>", focuspasswout)

        def update():
            if accnoe1.get() == "Enter the Account No.." or passwe1.get() == "Create a New Password..":
                messagebox.showerror("Invalid", "Please Fill all Fields..!!")
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")

                    cur = con.cursor()

                except:
                    return
                qry = "use user"
                cur.execute(qry)
                qry = "select Account_Holder from bank where Account_No=%s"
                cur.execute(qry, (accnoe1.get(),))
                result = cur.fetchone()
                if result==None:
                    messagebox.showerror("Not Found ", "Account not found try again...")
                    trial_no()

                else:
                    qry = "update bank set Password=%s where Account_No=%s"
                    cur.execute(qry, (passwe1.get(),accnoe1.get()))
                    con.commit()
                    messagebox.showinfo("Updated","Password Updated Successfully..!!")
                    clear()
        global limit
        limit = 0
        def trial_no():
            global limit
            limit += 1
            if limit==3:
                messagebox.showwarning("Warning","You have tried more than the limit")
                messagebox.showinfo("Create", "Account not found Kindly Create....")
                messagebox.showinfo("Loading", "Loading...Please Wait..!!")
                time.sleep(3)
                new()


        def clear():
            accnoe1.delete(0,"end")
            passwe1.delete(0,"end")
            accnoe1.focus()

        def new():
            win.destroy()
            ob = Bank.bank()

        def delete():
            win.destroy()
            delbnk.Del()



        lobtn = Button(frm, text="Update", width=10, height=1, font=("times", 15), bg="#ff33a8", fg="white",
                       activebackground="white", activeforeground="black", command=update)
        lobtn.place(x=210, y=420)

        lobtn = Button(frm, text="New User", width=10, height=1, font=("times", 15) ,bg="white", fg="#ff33a8",
                       activebackground="white", activeforeground="black", command=new)
        lobtn.place(x=50, y=350)

        lobtn = Button(frm, text="Delete", width=10, height=1, font=("times", 15), bg="white", fg="#ff33a8",
                       activebackground="white", activeforeground="black", command=delete)
        lobtn.place(x=350, y=350)

        win.mainloop()