import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import time
import mysql.connector
from PIL import  Image, ImageTk
from qrgen import qr
import Bank


class con:
    def __init__(self):
        win=Tk()
        win.title("Login System")
        win.state("zoomed")
        win.config(background="lightblue")

        frm = Frame(win, width=1450, height=700, bd=2, relief="raised")
        frm.place(x=50, y=50)
        lab = Label(frm, text="Contents", fg="Blue", font=("arial", 30, "bold"))
        lab.place(x=620, y=20)

        def qrs():
            win.destroy()
            obj=qr()
        def bank1():
            win.destroy()
            obj=Bank.bank()

        btn = Button(frm, text="QR scanner", width=15, height=1, font=("times", 15), bg="lightblue", fg="blue",activebackground="white", activeforeground="black", command=qrs)
        btn.place(x=150, y=220)
        btn2 = Button(frm, text="Account", width=15, height=1, font=("times", 15), bg="lightgreen", fg="blue",activebackground="white", activeforeground="black", command=bank1)
        btn2.place(x=350, y=220)

        win.mainloop()