import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import time
import mysql.connector
from PIL import  Image, ImageTk
import Bank
import forbnk

def Del():
    root=Tk()
    root.title("Delete Account")
    root.state("zoomed")
    root.config(background="lightgreen")
    delete = Image.open("image\\delete.jpg")
    image = ImageTk.PhotoImage(file="image\\delete.jpg")
    lbl = Label(root, image=image)
    lbl.place(x=0, y=0)

    frm = Frame(root,width=550,height=470,bd=2,relief="raised")
    frm.place(x=500,y=210)
    lab = Label(frm,text="Delete Account",fg="green",font=("arial",30,"bold"))
    lab.place(x=150,y=20)

    def focusaccin(event):
        if accnoe1.get() == "Enter the Account No..":
            accnoe1.delete(0, "end")

    def focusaccout(event):

        if accnoe1.get() == "":
            accnoe1.insert(0, "Enter the Account No..")

    def focuspasswin(event):

        if passwe1.get() == "Enter the Password..":
            passwe1.delete(0, "end")

    def focuspasswout(event):

        if passwe1.get() == "":
            passwe1.insert(0, "Enter the Password..")

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
    passwe1.insert(0, "Enter the Password..")
    passwe1.bind("<FocusIn>", focuspasswin)
    passwe1.bind("<FocusOut>", focuspasswout)

    def delete():
        if accnoe1.get()=="Enter the Account No." or passwe1.get()=="Enter the Password..":
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
            qry = "select ID from bank where Account_No=%s and Password=%s"
            cur.execute(qry, (accnoe1.get(),passwe1.get()))
            result=cur.fetchone()
            if result==None:
                messagebox.showerror("Not Found","Account not found")
                trial_no()
            else:
                messagebox.showwarning("Terms and Conditions"
                                       ,"""
                1. Account Ownership & Authorization

                Only the account holder or an authorized representative can request deletion.
                
                Identity verification may be required before processing the request.
                
                
                2. Pending Transactions & Obligations
                
                All pending transactions must be completed or canceled before deletion.
                
                Any outstanding dues, fees, or liabilities must be cleared.
                
                
                3. Data Retention & Privacy
                
                Some personal data may be retained for legal, regulatory, or security reasons.
                
                Transaction history may remain accessible even after account deletion.
                
                
                4. Irreversibility of Deletion
                
                Once deleted, the account may not be recoverable.
                
                Certain services may allow reactivation within a specific period.
                
                
                5. Subscription & Linked Services
                
                Any active subscriptions linked to the account will be canceled.
                
                Deletion may impact linked accounts or third-party services.
                
                
                6. Legal & Compliance Restrictions
                
                Certain accounts (e.g., financial or regulated accounts) may have additional deletion requirements.
                
                Legal obligations may delay or restrict deletion in some cases.""")
                qry="delete from bank where ID=%s"
                cur.execute(qry,(result[0],))
                con.commit()
                messagebox.showinfo("Delete","Your Account has been Deleted..")
                Clear()
                accnoe1.focus()

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

    def new():
        root.destroy()
        ob = Bank.bank()

    def Clear():
        accnoe1.delete(0, "end")
        passwe1.delete(0, "end")

    def forpass():
        root.destroy()
        b=forbnk.forget()

    lobtn = Button(frm,text="Delete",width=10,height=1,font=("times",15),bg="green",fg="white",activebackground="white",activeforeground="black",command=delete)
    lobtn.place(x=210,y=420)

    forbtn = Button(frm,text="Forget Password",width=15,height=1,font=("times",15),bg="white",fg="green",activebackground="white",activeforeground="black",command=forpass)
    forbtn.place(x=50,y=350)

    signbtn = Button(frm,text="New Account",width=15,height=1,font=("times",15),bg="white",fg="green",activebackground="white",activeforeground="black",command=new)
    signbtn.place(x=350,y=350)

    root.mainloop()