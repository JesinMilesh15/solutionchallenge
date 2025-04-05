import qrcode
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk


class qr:
    def __init__(self):
        root = Tk()
        root.title("QR Generator")
        root.state("zoomed")
        root.config(background="lightblue")


        frm = Frame(root, width=900, height=700, bd=2, relief="raised")
        frm.place(x=420, y=30)

        lab = Label(frm, text="QR Generator", fg="red", font=("arial", 30, "bold"))
        lab.place(x=290, y=20)


        data = Label(frm, text="URL", fg="black", font=("times", 20, "bold"))
        data.place(x=50, y=160)
        datae = Entry(frm, width=100, bd=1)
        datae.place(x=150, y=170)
        datae.focus()

        def generate():
            qr = qrcode.QRCode(version=10, box_size=5, border=9)
            if datae.get()=="":
                messagebox.showerror("Link Required","Kindly fill the Data")
            else:

                qr.add_data(datae.get())
                qr.make(fit=True)
                image=qr.make_image(Fill="black",back_color="white")
                image.save("D:\\Python Files\\Solution challenge\\image 1\\qr.png")

                log = Image.open("D:\\Python Files\\Solution challenge\\image 1\\qr.png")
                image = ImageTk.PhotoImage(file="D:\\Python Files\\Solution challenge\\image 1\\qr.png")

                lbl = Label(frm, image=image,height=380,width=500)
                lbl.place(x=190, y=290)
                image.resize((50, 50))



        gebtn = Button(frm, text="Generate", width=15, height=1, font=("times", 15), bg="green", fg="white",activebackground="white", activeforeground="black",command=generate)
        gebtn.place(x=350, y=230)

        root.mainloop()

