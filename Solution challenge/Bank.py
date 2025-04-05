import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import time
import mysql.connector
from PIL import  Image, ImageTk
from tkinter import ttk
import Content
import mysql.connector
import upbnk
import delbnk
import forbnk
import qrgen
import qrcode
import login
from eduloan import loan

class bank:
    def __init__(self):
        root = Tk()
        root.title("Bank Mangement")
        root.state("zoomed")
        root.config(background="lightblue")


        frm = Frame(root, width=1500, height=790, bd=2, relief="raised")
        frm.place(x=10, y=30)
        lab = Label(frm, text="Bank Management", fg="red", font=("arial", 30, "bold"))
        lab.place(x=550, y=20)

        def focusin(event):
            if acche.get() == "Enter the Holder Name..":
                acche.delete(0, "end")

        def focusout(event):

            if acche.get() == "":
                acche.insert(0, "Enter the Holder Name..")

        def focusaccin(event):
            if accnoe.get() == "Enter the Account No..":
                accnoe.delete(0, "end")

        def focusaccout(event):

            if accnoe.get() == "":
                accnoe.insert(0, "Enter the Account No..")
        def focusifin(event):
            if ifs.get() == "Enter the IFSC Code..":
                ifs.delete(0, "end")

        def focusifout(event):

            if ifs.get() == "":
                ifs.insert(0, "Enter the IFSC Code..")
        def focusmobin(event):
            if mbnoe.get() == "Enter the Moblie No..":
                mbnoe.delete(0, "end")

        def focusmobout(event):

            if mbnoe.get() == "":
                mbnoe.insert(0, "Enter the Moblie No..")
        def focusaain(event):
            if anoe.get() == "Enter the Aadhar No..":
                anoe.delete(0, "end")

        def focusaaout(event):

            if anoe.get() == "":
                anoe.insert(0, "Enter the Aadhar No..")

        def focuspanin(event):
            if pannoe.get() == "Enter the PAN No..":
                pannoe.delete(0, "end")

        def focuspanout(event):

            if pannoe.get() == "":
                pannoe.insert(0, "Enter the PAN No..")

        def focusdisin(event):
            if diste.get() == "Enter the District..":
                diste.delete(0, "end")

        def focusdisout(event):

            if diste.get() == "":
                diste.insert(0, "Enter the District..")

        def focusbnhin(event):
            if branche.get() == "Enter the Branch..":
                branche.delete(0, "end")

        def focusbnhout(event):

            if branche.get() == "":
                branche.insert(0, "Enter the Branch..")

        def focusbnkin(event):
            if bnkne.get() == "Enter the Bank Name..":
                bnkne.delete(0, "end")

        def focusbnkout(event):

            if bnkne.get() == "":
                bnkne.insert(0, "Enter the Bank Name..")

        def focuspasswin(event):

            if passwe.get() == "Create a Password..":
                passwe.delete(0, "end")

        def focuspasswout(event):

            if passwe.get() == "":
                passwe.insert(0, "Create a Password..")

        def focusrepassein(event):

            if repasswe.get() == "Re-Enter..":
                repasswe.delete(0, "end")

        def focusrepasseout(event):

            if repasswe.get() == "":
                repasswe.insert(0, "Re-Enter..")



        acch = Label(frm, text="Account Holder", fg="black", font=("times", 20, "bold"))
        acch.place(x=50, y=160)
        acche = Entry(frm, width=40, bd=1)
        acche.place(x=250, y=170)
        acche.insert(0, "Enter the Holder Name..")
        acche.focus()
        acche.bind("<FocusIn>", focusin)
        acche.bind("<FocusOut>", focusout)

        accno = Label(frm, text="Account No", fg="black", font=("times", 20, "bold"))
        accno.place(x=510, y=160)
        accnoe = Entry(frm, width=40, bd=1)
        accnoe.place(x=670, y=170)
        accnoe.insert(0, "Enter the Account No..")
        accnoe.bind("<FocusIn>", focusaccin)
        accnoe.bind("<FocusOut>", focusaccout)

        ifsc = Label(frm, text="IFSC Code", fg="black", font=("times", 20, "bold"))
        ifsc.place(x=940, y=160)
        ifs = Entry(frm, width=40, bd=1)
        ifs.place(x=1090, y=170)
        ifs.insert(0, "Enter the IFSC Code..")
        ifs.bind("<FocusIn>", focusifin)
        ifs.bind("<FocusOut>", focusifout)

        mbno = Label(frm, text="Mobile No", fg="black", font=("times", 20, "bold"))
        mbno.place(x=50, y=260)
        mbnoe = Entry(frm, width=40, bd=1)
        mbnoe.place(x=250, y=270)
        mbnoe.insert(0, "Enter the Moblie No..")
        mbnoe.bind("<FocusIn>", focusmobin)
        mbnoe.bind("<FocusOut>", focusmobout)

        ano = Label(frm, text="Aadhar No", fg="black", font=("times", 20, "bold"))
        ano.place(x=510, y=260)
        anoe = Entry(frm, width=40, bd=1)
        anoe.place(x=670, y=270)
        anoe.insert(0, "Enter the Aadhar No..")
        anoe.bind("<FocusIn>", focusaain)
        anoe.bind("<FocusOut>", focusaaout)

        panno = Label(frm, text="PAN No", fg="black", font=("times", 20, "bold"))
        panno.place(x=950, y=260)
        pannoe = Entry(frm, width=40, bd=1)
        pannoe.place(x=1090, y=270)
        pannoe.insert(0, "Enter the PAN No..")
        pannoe.bind("<FocusIn>", focuspanin)
        pannoe.bind("<FocusOut>", focuspanout)

        dist = Label(frm, text="District", fg="black", font=("times", 20, "bold"))
        dist.place(x=50, y=360)
        diste = Entry(frm, width=40, bd=1)
        diste.place(x=250, y=370)
        diste.insert(0, "Enter the District..")
        diste.bind("<FocusIn>", focusdisin)
        diste.bind("<FocusOut>", focusdisout)

        branch = Label(frm, text="Branch", fg="black", font=("times", 20, "bold"))
        branch.place(x=510, y=360)
        branche = Entry(frm, width=40, bd=1)
        branche.place(x=670, y=370)
        branche.insert(0, "Enter the Branch..")
        branche.bind("<FocusIn>", focusbnhin)
        branche.bind("<FocusOut>", focusbnhout)

        bnkn = Label(frm, text="Bank Name", fg="black", font=("times", 20, "bold"))
        bnkn.place(x=940, y=360)
        bnkne = Entry(frm, width=40, bd=1)
        bnkne.place(x=1090, y=370)
        bnkne.insert(0, "Enter the Bank Name..")
        bnkne.bind("<FocusIn>", focusbnkin)
        bnkne.bind("<FocusOut>", focusbnkout)

        passw = Label(frm, text="Password", fg="black", font=("times", 20, "bold"))
        passw.place(x=50, y=460)
        passwe = Entry(frm, width=40, bd=1)
        passwe.place(x=250, y=470)
        passwe.insert(0, "Create a Password..")
        passwe.bind("<FocusIn>",focuspasswin)
        passwe.bind("<FocusOut>",focuspasswout)

        repassw = Label(frm, text="Re-Enter", fg="black", font=("times", 20, "bold"))
        repassw.place(x=510, y=460)
        repasswe = Entry(frm, width=40, bd=1,show=".")
        repasswe.place(x=670, y=470)
        repasswe.insert(0, "Re-Enter..")
        repasswe.bind("<FocusIn>",focusrepassein)
        repasswe.bind("<FocusOut>",focusrepasseout)

        def backf():
            root.destroy()
            obj1 = login.login()
        def add():
            if acche.get() == "" or accnoe.get() == "" or ifs.get() == "" or mbnoe.get() == "" or anoe.get() == "" or pannoe.get() == "" or diste.get() == "" or branche.get() == "" or bnkne.get() == "" or passwe.get()=="" or repasswe.get()=="":
                messagebox.showerror("Error", "Please Fill all Fields...!!!")
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")
                    cur = con.cursor()
                    data = "create database if not exists user"
                    cur.execute(data)
                    qry = "use user"
                    cur.execute(qry)
                    table = "create table if not exists bank(ID int primary key auto_increment not null,Account_Holder char(100) not null,Account_No int not null,IFSC_Code varchar(100) not null,Mobile_No bigint not null,Aadhar_No bigint not null,Pan_No varchar(100) not null,District char(100) not null,Branch char(100) not null,Bank_Name char(100) not null,Password varchar(100) not null)"
                    cur.execute(table)
                except:
                    print("Table Exists")
                    return
                if passwe.get() == repasswe.get():
                    messagebox.showinfo("Terms and Conditions"
                    ,"""

                    1. Account Ownership & Authorization
                    
                    You must be the legal owner or have authorization to add the bank account.
                    
                    You consent to verification processes to confirm ownership.
                    
                    
                    2. Accuracy of Information
                    
                    You must provide accurate bank details (account number, routing number, etc.).
                    
                    Any incorrect information may lead to failed transactions or account restrictions.
                    
                    
                    3. Consent for Transactions
                    
                    You authorize debits and credits to/from the linked bank account.
                    
                    You may need to provide consent for recurring transactions.
                    
                    
                    4. Security & Fraud Prevention
                    
                    The institution may monitor transactions for fraud.
                    
                    Unauthorized use or suspicious activity may lead to account suspension.
                    
                    
                    5. Liability & Disputes
                    
                    The institution is not liable for issues caused by incorrect information provided by you.
                    
                    Dispute resolution procedures will be outlined for unauthorized transactions.
                    
                    
                    6. Privacy & Data Protection
                    
                    Your banking information will be handled according to the platform’s privacy policy.
                    
                    Your data may be shared with third parties for verification or compliance purposes.
                    
                    
                    7. Removal or Changes
                    
                    You can remove or update the bank account as per the platform's policies.
                    
                    The institution may restrict changes under certain conditions""")
                    qry = "insert into bank(Account_Holder,Account_No,IFSC_Code,Mobile_No,Aadhar_No,Pan_No,District,Branch,Bank_Name,Password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(qry,(acche.get(), accnoe.get(), ifs.get(), mbnoe.get(), anoe.get(), pannoe.get(), diste.get(),branche.get(),bnkne.get(),passwe.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Account Created")
                    clear()
                    insert()

                else:
                    messagebox.showerror("Error", "Password Does not Match...!!")
        def clear():
            acche.delete(0,"end")
            accnoe.delete(0, "end")
            ifs.delete(0, "end")
            mbnoe.delete(0,"end")
            anoe.delete(0,"end")
            pannoe.delete(0, "end")
            diste.delete(0, "end")
            branche.delete(0,"end")
            bnkne.delete(0, "end")
            passwe.delete(0, "end")
            repasswe.delete(0, "end")

        def insert():
            acche.insert(0, "Enter the Holder Name..")
            accnoe.insert(0, "Enter the Account No..")
            ifs.insert(0, "Enter the IFSC Code..")
            mbnoe.insert(0, "Enter the Moblie No..")
            anoe.insert(0, "Enter the Aadhar No..")
            pannoe.insert(0, "Enter the PAN No..")
            diste.insert(0, "Enter the District..")
            branche.insert(0, "Enter the Branch..")
            bnkne.insert(0, "Enter the Bank Name..")
            passwe.insert(0, "Create a Password..")
            repasswe.insert(0, "Re-Enter the Password..")
            acche.focus()

        def update():
            root.destroy()
            ob=upbnk.upbnk()
        def dele():
            root.destroy()
            ob=delbnk.Del()
        def forget():
            root.destroy()
            ob=forbnk.forget()

        def qrg():
            if acche.get() == "" or accnoe.get() == "" or ifs.get() == "" or mbnoe.get() == "" or anoe.get() == "" or pannoe.get() == "" or diste.get() == "" or branche.get() == "" or bnkne.get() == "" or passwe.get() == "" or repasswe.get() == "":
                messagebox.showerror("Error", "Please Fill all Fields...!!!")
            else:
                qr = qrcode.QRCode(version=10, box_size=4, border=9)
                acch="Acc_Holder=",acche.get()
                accn="Acc_No",accnoe.get()
                ifcd="Mobile=",ifs.get()
                mobe="Mobile=",mbnoe.get()
                aao="Aadhar",anoe.get()
                pano="Pan_No",pannoe.get()
                distri="District",diste.get()
                branchh="Branch=",branche.get()
                bnknam="Bank_Name",bnkne.get()
                passwd="Password=",passwe.get()
                qr.add_data(str(acch)+str(accn)+str(ifcd)+str(mobe)+str(aao)+str(pano)+str(distri)+str(branchh)+str(bnknam)+str(passwd))
                qr.make(fit=True)
                image = qr.make_image(Fill="black", back_color="white")
                image.save("D:\\Python Files\\Solution challenge\\image 1\\qrb.png")

                log = Image.open("D:\\Python Files\\Solution challenge\\image 1\\qrb.png")
                image = ImageTk.PhotoImage(file="D:\\Python Files\\Solution challenge\\image 1\\qrb.png")
                lbl = Label(frm, image=image)
                lbl.place(x=1070, y=400)
                image.show()



        def education():
            root.destroy()
            obj=loan()
        addbtn = Button(frm, text="Add Account", width=15, height=1, font=("times", 15), bg="red", fg="white",activebackground="white", activeforeground="black",command=add)
        addbtn.place(x=630, y=730)

        upbtn = Button(frm, text="Update Account", width=15, height=1, font=("times", 15), bg="green", fg="white",activebackground="white", activeforeground="black",command=update)
        upbtn.place(x=910, y=730)
        rebtn = Button(frm, text="Remove Account", width=15, height=1, font=("times", 15), bg="#1478e8", fg="white",activebackground="white", activeforeground="black",command=dele)
        rebtn.place(x=50, y=730)

        sebtn = Button(frm, text="Forget Password", width=15, height=1, font=("times", 15), bg="orange", fg="white",activebackground="white", activeforeground="black",command=forget)
        sebtn.place(x=330, y=730)

        lonbtn = Button(frm, text="Educational Loan", width=15, height=1, font=("times", 15), bg="green", fg="white",activebackground="white", activeforeground="black",command=education)
        lonbtn.place(x=1190, y=40)

        bacbtn = Button(frm, text="Logout", width=15, height=1, font=("times", 15), bg="red", fg="white",activebackground="white", activeforeground="black", command=backf)
        bacbtn.place(x=90, y=40)

        qrbtn = Button(frm, text="Generate QR", width=15, height=1, font=("times", 15), bg="#cb14e8", fg="white",activebackground="white", activeforeground="black",command=qrg)
        qrbtn.place(x=1190, y=730)

        root.mainloop()