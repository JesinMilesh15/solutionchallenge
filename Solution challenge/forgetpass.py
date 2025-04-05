import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox
import signup
import time
from PIL import Image,ImageTk
from delete import Del





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

        def focusin(event):
            if emen.get()=="Enter the Email..":
                emen.delete(0,"end")
        def focusout(event):

            if emen.get()=="":
                emen.insert(0,"Enter the Email..")
        def focuspassout(event):

            if pasen.get()=="":
                pasen.insert(0, "Create a New Password..")
        def focuspassin(event):

            if pasen.get()=="Create a New Password..":
                pasen.delete(0, "end")

        lblus = Label(frm, text="Email", fg="black", font=("times", 20, "bold"))
        lblus.place(x=50, y=160)
        emen = Entry(frm, width=50, bd=1, )
        emen.place(x=210, y=170)
        emen.insert(0, "Enter the Email..")
        emen.focus()
        emen.bind("<FocusIn>", focusin)
        emen.bind("<FocusOut>", focusout)

        lalpas = Label(frm, text="Password", fg="black", font=("times", 20, "bold"))
        lalpas.place(x=50, y=260)
        pasen = Entry(frm, width=50, bd=1)
        pasen.insert(0, "Create a New Password..")
        pasen.place(x=210, y=270)
        pasen.bind("<FocusIn>", focuspassin)
        pasen.bind("<FocusOut>", focuspassout)

        def update():
            if emen.get() == "Enter the Email.." or pasen.get() == "Create a New Password..":
                messagebox.showerror("Invalid", "Please Fill all Fields..!!")
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")

                    cur = con.cursor()

                except:
                    return
                qry = "use user"
                cur.execute(qry)
                qry = "select Username,Password from signup where Email_Id=%s"
                cur.execute(qry, (emen.get(),))
                result = cur.fetchone()
                if result==None:
                    messagebox.showerror("Not Found ", "Email not found try again...")
                    trial_no()

                else:
                    qry = "update signup set Password=%s where Email_Id=%s"
                    cur.execute(qry, (pasen.get(),emen.get()))
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
                messagebox.showinfo("Signup", "Email not found Kindly Signup....")
                messagebox.showinfo("Loading", "Loading...Please Wait..!!")
                time.sleep(3)
                signup()


        def clear():
            emen.delete(0,"end")
            pasen.delete(0,"end")
            emen.focus()

        def signup1():
            win.destroy()
            ob=signup.start()

        def delete():
            win.destroy()
            Del()



        lobtn = Button(frm, text="Update", width=10, height=1, font=("times", 15), bg="#ff33a8", fg="white",
                       activebackground="white", activeforeground="black", command=update)
        lobtn.place(x=210, y=420)

        lobtn = Button(frm, text="New User", width=10, height=1, font=("times", 15) ,bg="white", fg="#ff33a8",
                       activebackground="white", activeforeground="black", command=signup1)
        lobtn.place(x=50, y=350)

        lobtn = Button(frm, text="Delete", width=10, height=1, font=("times", 15), bg="white", fg="#ff33a8",
                       activebackground="white", activeforeground="black", command=delete)
        lobtn.place(x=350, y=350)

        win.mainloop()