import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import upload
import mysql.connector



class loan:
    def __init__(self):
        root = Tk()
        root.title("Education Loan")
        root.state("zoomed")
        root.config(background="lightblue")

        frm = Frame(root, width=1500, height=820, bd=2, relief="raised")
        frm.place(x=10, y=10)
        lab = Label(frm, text="Educational Loan", fg="red", font=("arial", 30, "bold"))
        lab.place(x=550, y=20)
        def focusin(event):
            if acche.get() == "Enter the Applicant Name..":
                acche.delete(0, "end")

        def focusout(event):

            if acche.get() == "":
                acche.insert(0, "Enter the Applicant Name..")

        def focusaccin(event):
            if accnoe.get() == "Enter the Acc No of the Applicant..":
                accnoe.delete(0, "end")

        def focusaccout(event):

            if accnoe.get() == "":
                accnoe.insert(0, "Enter the Acc No of the Applicant..")
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
        def focusfnamin(event):
            if fnamee.get() == "Enter the Father Name..":
                fnamee.delete(0,"end")
        def focusfnamout(event):
            if fnamee.get() == "":
                fnamee.insert(0,"Enter the Father Name..")

        def focusmnamin(event):
            if mnamee.get() == "Enter the Mother Name..":
                mnamee.delete(0, "end")

        def focusmnamout(event):
            if mnamee.get() == "":
                mnamee.insert(0, "Enter the Mother Name..")
        def focusfaccin(event):
            if faccpe.get() == "Enter the Father Acc No..":
                faccpe.delete(0, "end")

        def focusfaccout(event):
            if faccpe.get() == "":
                faccpe.insert(0, "Enter the Father Acc No..")
        def focusfinin(event):
            if fincoe.get() == "Enter the Father Income..":
                fincoe.delete(0, "end")

        def focusfinout(event):
            if fincoe.get() == "":
                fincoe.insert(0, "Enter the Father Income..")

        def focusfocin(event):
            if focce.get() == "Enter the Father Occupation..":
                focce.delete(0, "end")

        def focusfocout(event):
            if focce.get() == "":
                focce.insert(0, "Enter the Father Occupation..")
        def focusloain(event):
            if lapie.get() == "Enter the Loan Applicant Income..":
                lapie.delete(0, "end")

        def focusloaout(event):
            if lapie.get() == "":
                lapie.insert(0, "Enter the Loan Applicant Income..")
        def focuslamin(event):
            if laccpe.get() == "Enter the Loan Amount..":
                laccpe.delete(0, "end")

        def focuslamout(event):
            if laccpe.get() == "":
                laccpe.insert(0, "Enter the Loan Amount..")
        def focusbonin(event):
            if bonae.get() == "Enter the College Bonafide..":
                bonae.delete(0, "end")

        def focusbonout(event):
            if bonae.get() == "":
                bonae.insert(0, "Enter the College Bonafide..")
        def focuscrein(event):
            if crete.get() == "Enter the Credit Amount..":
                crete.delete(0, "end")

        def focuscreout(event):
            if crete.get() == "":
                crete.insert(0, "Enter the Credit Amount..")
        def focusmarin(event):
            if markae.get() == "Enter the 10th Mark..":
                markae.delete(0, "end")

        def focusmarout(event):
            if markae.get() == "":
                markae.insert(0, "Enter the 10th Mark..")
        def focusinccin(event):
            if incee.get() == "Enter the Income Certificate..":
                incee.delete(0, "end")

        def focusinccout(event):
            if incee.get() == "":
                incee.insert(0, "Enter the Income Certificate..")
        def focuscolin(event):
            if cdete.get() == "Enter the College..":
                cdete.delete(0, "end")

        def focuscolout(event):
            if cdete.get() == "":
                cdete.insert(0, "Enter the College..")



        aname = Label(frm, text="Applicant Name", fg="black", font=("times", 20, "bold"))
        aname.place(x=50, y=110)
        acche = Entry(frm, width=40, bd=1)
        acche.place(x=250, y=120)
        acche.insert(0, "Enter the Applicant Name..")
        acche.focus()
        acche.bind("<FocusIn>", focusin)
        acche.bind("<FocusOut>", focusout)

        adob = Label(frm, text="Acc No", fg="black", font=("times", 20, "bold"))
        adob.place(x=510, y=110)
        accnoe = Entry(frm, width=40, bd=1)
        accnoe.place(x=690, y=120)
        accnoe.insert(0, "Enter the Acc No of the Applicant..")
        accnoe.bind("<FocusIn>", focusaccin)
        accnoe.bind("<FocusOut>", focusaccout)

        ifsc = Label(frm, text="IFSC Code", fg="black", font=("times", 20, "bold"))
        ifsc.place(x=940, y=110)
        ifs = Entry(frm, width=40, bd=1)
        ifs.place(x=1160, y=120)
        ifs.insert(0, "Enter the IFSC Code..")
        ifs.bind("<FocusIn>", focusifin)
        ifs.bind("<FocusOut>", focusifout)

        mbno = Label(frm, text="Mobile No", fg="black", font=("times", 20, "bold"))
        mbno.place(x=50, y=210)
        mbnoe = Entry(frm, width=40, bd=1)
        mbnoe.place(x=250, y=220)
        mbnoe.insert(0, "Enter the Moblie No..")
        mbnoe.bind("<FocusIn>", focusmobin)
        mbnoe.bind("<FocusOut>", focusmobout)

        ano = Label(frm, text="Aadhar No", fg="black", font=("times", 20, "bold"))
        ano.place(x=510, y=210)
        anoe = Entry(frm, width=40, bd=1)
        anoe.place(x=690, y=220)
        anoe.insert(0, "Enter the Aadhar No..")
        anoe.bind("<FocusIn>", focusaain)
        anoe.bind("<FocusOut>", focusaaout)

        panno = Label(frm, text="PAN No", fg="black", font=("times", 20, "bold"))
        panno.place(x=950, y=210)
        pannoe = Entry(frm, width=40, bd=1)
        pannoe.place(x=1160, y=220)
        pannoe.insert(0, "Enter the PAN No..")
        pannoe.bind("<FocusIn>", focuspanin)
        pannoe.bind("<FocusOut>", focuspanout)

        dist = Label(frm, text="District", fg="black", font=("times", 20, "bold"))
        dist.place(x=50, y=310)
        diste = Entry(frm, width=40, bd=1)
        diste.place(x=250, y=320)
        diste.insert(0, "Enter the District..")
        diste.bind("<FocusIn>", focusdisin)
        diste.bind("<FocusOut>", focusdisout)

        branch = Label(frm, text="Branch", fg="black", font=("times", 20, "bold"))
        branch.place(x=510, y=310)
        branche = Entry(frm, width=40, bd=1)
        branche.place(x=690, y=320)
        branche.insert(0, "Enter the Branch..")
        branche.bind("<FocusIn>", focusbnhin)
        branche.bind("<FocusOut>", focusbnhout)

        bnkn = Label(frm, text="Bank Name", fg="black", font=("times", 20, "bold"))
        bnkn.place(x=940, y=310)
        bnkne = Entry(frm, width=40, bd=1)
        bnkne.place(x=1160, y=320)
        bnkne.insert(0, "Enter the Bank Name..")
        bnkne.bind("<FocusIn>", focusbnkin)
        bnkne.bind("<FocusOut>", focusbnkout)

        fname = Label(frm, text="Father name ", font=("times", 20, "bold"))
        fname.place(x=50, y=410)
        fnamee = Entry(frm, width=40, bd=1)
        fnamee.place(x=250, y=420)
        fnamee.insert(0, "Enter the Father Name..")
        fnamee.bind("<FocusIn>",focusfnamin)
        fnamee.bind("<FocusOut>",focusfnamout)

        mname = Label(frm, text="Mother Name ", font=("times", 20, "bold"))
        mname.place(x=510, y=410)
        mnamee = Entry(frm, width=40, bd=1)
        mnamee.place(x=690, y=420)
        mnamee.insert(0, "Enter the Mother Name..")
        mnamee.bind("<FocusIn>", focusmnamin)
        mnamee.bind("<FocusOut>", focusmnamout)

        faccp = Label(frm, text="Father Account", font=("times", 20, "bold"))
        faccp.place(x=940, y=410)
        faccpe = Entry(frm, width=40, bd=1)
        faccpe.place(x=1160, y=420)
        faccpe.insert(0, "Enter the Father Acc No..")
        faccpe.bind("<FocusIn>", focusfaccin)
        faccpe.bind("<FocusOut>", focusfaccout)

        finco = Label(frm, text="Father Income", font=("times", 20, "bold"))
        finco.place(x=50, y=510)
        fincoe = Entry(frm, width=40, bd=1)
        fincoe.place(x=250, y=520)
        fincoe.insert(0, "Enter the Father Income..")
        fincoe.bind("<FocusIn>", focusfinin)
        fincoe.bind("<FocusOut>", focusfinout)

        focc = Label(frm, text="Father Occup", font=("times", 20, "bold"))
        focc.place(x=510, y=510)
        focce = Entry(frm, width=40, bd=1)
        focce.place(x=690, y=520)
        focce.insert(0, "Enter the Father Occupation..")
        focce.bind("<FocusIn>", focusfocin)
        focce.bind("<FocusOut>", focusfocout)

        lapi = Label(frm, text="Applicant Income", font=("times", 20, "bold"))
        lapi.place(x=940, y=510)
        lapie = Entry(frm, width=40, bd=1)
        lapie.place(x=1160, y=520)
        lapie.insert(0, "Enter the Loan Applicant Income..")
        lapie.bind("<FocusIn>", focusloain)
        lapie.bind("<FocusOut>", focusloaout)

        laccp = Label(frm, text="Loan Amount", font=("times", 20, "bold"))
        laccp.place(x=50, y=610)
        laccpe = Entry(frm, width=40, bd=1)
        laccpe.place(x=250, y=620)
        laccpe.insert(0, "Enter the Loan Amount..")
        laccpe.bind("<FocusIn>", focuslamin)
        laccpe.bind("<FocusOut>", focuslamout)

        bona = Label(frm, text="Bonafide", font=("times", 20, "bold"))
        bona.place(x=510, y=610)
        bonae = Entry(frm, width=40, bd=1)
        bonae.place(x=690, y=620)
        bonae.insert(0, "Enter the College Bonafide..")
        bonae.bind("<FocusIn>", focusbonin)
        bonae.bind("<FocusOut>", focusbonout)

        cret = Label(frm, text="Credits", font=("times", 20, "bold"))
        cret.place(x=940, y=610)
        crete = Entry(frm, width=40, bd=1)
        crete.place(x=1160, y=620)
        crete.insert(0, "Enter the Credit Amount..")
        crete.bind("<FocusIn>", focuscrein)
        crete.bind("<FocusOut>", focuscreout)

        marka = Label(frm, text="10th Mark", font=("times", 20, "bold"))
        marka.place(x=50, y=710)
        markae = Entry(frm, width=40, bd=1)
        markae.place(x=250, y=720)
        markae.insert(0, "Enter the 10th Mark..")
        markae.bind("<FocusIn>", focusmarin)
        markae.bind("<FocusOut>", focusmarout)

        ince = Label(frm, text="Income No", font=("times", 20, "bold"))
        ince.place(x=510, y=710)
        incee = Entry(frm, width=40, bd=1)
        incee.place(x=690, y=720)
        incee.insert(0, "Enter the Income Certificate..")
        incee.bind("<FocusIn>", focusinccin)
        incee.bind("<FocusOut>", focusinccout)

        cdet = Label(frm, text="College Details", font=("times", 20, "bold"))
        cdet.place(x=940, y=710)
        cdete = Entry(frm, width=40, bd=1)
        cdete.place(x=1160, y=720)
        cdete.insert(0, "Enter the College..")
        cdete.bind("<FocusIn>", focuscolin)
        cdete.bind("<FocusOut>", focuscolout)

        def load():
            if acche.get() == "" or accnoe.get() == "" or ifs.get() == "" or mbnoe.get()=="" or anoe.get() == "" or pannoe.get() == "" or diste.get() == "" or branche.get() == "" or bnkne.get() == "" or fnamee.get() == "" or mnamee.get() == "" or faccpe.get() == "" or fincoe.get() == "" or focce.get() == "" or lapie.get() == "" or laccpe.get() == "" or bonae.get() == "" or crete.get() == "" or markae.get() == "" or incee.get() == "" or cdete.get() == "Enter the College..":
                messagebox.showerror("Error","All Fields Required")
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Jesin@102006")
                    cur = con.cursor()
                    data = "create database if not exists user"
                    cur.execute(data)
                    qry = "use user"
                    cur.execute(qry)
                    table ="create table if not exists loan(ID int primary key auto_increment not null,Account_Holder char(100) not null,Account_No int not null,IFSC_Code varchar(100) not null,Mobile_No bigint not null,Aadhar_No bigint not null,Pan_No varchar(100) not null,District char(100) not null,Branch char(100) not null,Bank_Name char(100) not null,Father_Name char(100) not null,Mother_Name char(100) not null,Father_Acc_No bigint not null,Father_Income int not null,Father_Occupation char(100) not null,Loan_Applicant_Income int not null,Loan_Amount int not null,Bonafide_No int not null,Credit_Amount int not null,Tenth_Mark int not null,Income_Certificate_No varchar(100) not null,College_Details varchar(100) not null)"
                    cur.execute(table)
                except:
                    print("Table Exists")
                    return
                qry = "insert into loan(Account_Holder,Account_No,IFSC_Code,Mobile_No,Aadhar_No,Pan_No,District,Branch,Bank_Name,Father_Name,Mother_Name,Father_Acc_No,Father_Income,Father_Occupation,Loan_Applicant_Income,Loan_Amount,Bonafide_No,Credit_Amount,Tenth_Mark,Income_Certificate_No,College_Details) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(qry, (acche.get(), accnoe.get(), ifs.get(), mbnoe.get(), anoe.get(), pannoe.get(), diste.get(), branche.get(),bnkne.get(), fnamee.get(), mnamee.get(), faccpe.get(), fincoe.get(), focce.get(), lapie.get(),laccpe.get(), bonae.get(), crete.get(), markae.get(), incee.get(), cdete.get()))
                con.commit()
                messagebox.showinfo("Terms and Conditions","""
                1. Eligibility Criteria:
                
                The applicant must be a citizen of the country where the loan is being applied.
                The student should have secured admission to a recognized institution (college/university) in a professional or technical course.
                Some banks require the applicant to have a strong academic record.
                The co-applicant (parent/guardian) should have a stable income source (for unsecured loans).
                
                2. Loan Coverage:
                
                Tuition fees and other academic expenses (library, lab, examination fees, etc.).
                Cost of books, equipment, and uniforms.
                Travel expenses (for studying abroad).
                Accommodation or hostel fees.
                Insurance (if required by the bank).
                
                3. Loan Amount & Interest Rate:
                
                The loan amount depends on the course and institution.
                Interest rates vary based on the bank and loan type (secured/unsecured).
                Some banks offer a lower interest rate for female students.
                
                4. Collateral Requirements:
                
                Loans above a certain limit (e.g., $10,000 or ₹7.5 lakh in India) may require collateral (property, fixed deposits, etc.).
                Loans below a certain limit may be granted without collateral based on the co-applicant’s creditworthiness.
                
                5. Repayment Terms:
                
                Repayment typically starts after the course is completed + a grace period (6 months to 1 year).
                The repayment period ranges from 5 to 15 years.
                Prepayment or foreclosure may be allowed with minimal charges.
         
                6. Required Documents:
                
                Admission letter from the institution.
                Fee structure from the institution.
                Identity proof (passport, Aadhaar, etc.).
                Address proof (utility bills, ration card, etc.).
                Income proof of co-applicant (salary slips, ITR, bank statements).
                Academic records (mark sheets, certificates).
                Collateral documents (if applicable).
                
                7. Loan Disbursement:
                
                The loan amount is usually disbursed directly to the educational institution in installments.
                Some banks may allow partial disbursement to the student for related expenses.
                
                8. Government Subsidies & Schemes:
                
                Some governments provide interest subsidies for students from economically weaker sections.
                Loans under government schemes may have relaxed repayment terms.""")

                messagebox.showinfo("Success", "Loan Applied")

        aplbtn = Button(frm, text="Apply", width=15, height=1, font=("times", 15), bg="blue", fg="white",activebackground="white",activeforeground="black",command=load)
        aplbtn.place(x=690, y=760)
        root.mainloop()
