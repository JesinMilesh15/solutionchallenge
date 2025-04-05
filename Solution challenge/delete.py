import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import time
import mysql.connector
from PIL import  Image, ImageTk
import signup
import forgetpass

def Del():
    root=Tk()
    root.title("Delete Account")
    root.state("zoomed")
    root.config(background="lightgreen")
    delete = Image.open("image\\delete.jpg")
    image = ImageTk.PhotoImage(file="image\\delete.jpg")
    lbl=Label(root,image=image)
    lbl.place(x=0,y=0)

    frm = Frame(root,width=550,height=470,bd=2,relief="raised")
    frm.place(x=500,y=210)
    lab = Label(frm,text="Delete Account",fg="green",font=("arial",30,"bold"))
    lab.place(x=150,y=20)

    def focusin(event):
        if emen.get()=="Enter the Email..":
            emen.delete(0,"end")
    def focusout(event):

        if emen.get()=="":
            emen.insert(0,"Enter the Email..")
    def focuspassout(event):

        if pasen.get()=="":
            pasen.insert(0, "Enter the Password..")
    def focuspassin(event):

        if pasen.get()=="Enter the Password..":
            pasen.delete(0, "end")

    lblus = Label(frm,text="Email",fg="black",font=("times",20,"bold"))
    lblus.place(x=50,y=160)
    emen = Entry(frm,width=50,bd=1,)
    emen.place(x=210,y=170)
    emen.insert(0,"Enter the Email..")
    emen.focus()
    emen.bind("<FocusIn>",focusin)
    emen.bind("<FocusOut>",focusout)


    lalpas = Label(frm,text="Password",fg="black",font=("times",20,"bold"))
    lalpas.place(x=50,y=260)
    pasen = Entry(frm,width=50,bd=1)
    pasen.insert(0,"Enter the Password..")
    pasen.place(x=210,y=270)
    pasen.bind("<FocusIn>",focuspassin)
    pasen.bind("<FocusOut>",focuspassout)

    def delete():
        if emen.get()=="Enter the Email.." or pasen.get()=="Enter the Password..":
            messagebox.showerror("Invalid","Please Fill all Fields..!!")
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")
                cur=con.cursor()
            except:
                print("Connected to Database...")
                return
            qry = "use user"
            cur.execute(qry)
            qry = "select ID from signup where Email_Id=%s and Password=%s"
            cur.execute(qry, (emen.get(), pasen.get()))
            result=cur.fetchone()
            if result==None:
                messagebox.showerror("Not Found","Username and Password not found")
                trial_no()
            else:
                qry="delete from signup where ID=%s"
                cur.execute(qry,(result[0],))
                con.commit()
                messagebox.showinfo("Delete","Your Account has been Deleted..")
                Clear()

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
            sign()

    def sign():
        root.destroy()
        ob=signup.start()

    def Clear():
        emen.delete(0, "end")
        pasen.delete(0, "end")

    def forpass():
        root.destroy()
        b=forgetpass.forget()

    lobtn = Button(frm,text="Delete",width=10,height=1,font=("times",15),bg="green",fg="white",activebackground="white",activeforeground="black",command=delete)
    lobtn.place(x=210,y=420)

    forbtn = Button(frm,text="Forget Password",width=15,height=1,font=("times",15),bg="white",fg="green",activebackground="white",activeforeground="black",command=forpass)
    forbtn.place(x=50,y=350)

    signbtn = Button(frm,text="New User",width=15,height=1,font=("times",15),bg="white",fg="green",activebackground="white",activeforeground="black",command=sign)
    signbtn.place(x=350,y=350)

    root.mainloop()