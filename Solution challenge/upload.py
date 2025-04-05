import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

class upimg:
    def __init__(self):
        root = Tk()
        root.title("Upload and Save Images")
        root.state("zoomed")
        root.config(background="lightblue")

        frm = Frame(root, width=1500, height=750, bd=2, relief="raised")
        frm.place(x=10, y=30)
        lab = Label(frm, text="Upload Images", fg="Blue", font=("arial", 30, "bold"))
        lab.place(x=550, y=20)


        def upload_photo():
            file_path = filedialog.askopenfilename(
                title="Select an Image",
                filetypes=[("Image Files", ".png;.jpg;.jpeg;.gif;*.bmp")]
            )
            if file_path:
                global img
                img = Image.open(file_path)
                img = img.resize((250, 250))
                img_tk = ImageTk.PhotoImage(img)
                photo_label.config(image=img_tk)
                photo_label.image = img_tk
                salbtn.config(state=tk.NORMAL)


        def save_photo():
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG Image", ".png"), ("JPEG Image", ".jpg"), ("All Files", ".")]
            )
            if save_path:
                img.save(save_path)
                status_label.config(text="Image saved successfully!")


        photo_label = tk.Label(root)
        photo_label.pack(pady=10)

        status_label = tk.Label(root, text="")
        status_label.pack(pady=10)

        uplbtn = Button(frm, text="Upload Photo", width=15, height=1, font=("times", 15), bg="pink", fg="white", activebackground="white", activeforeground="black", command=upload_photo)
        uplbtn.place(x=550, y=440)

        salbtn = Button(frm, text="Save Photo", width=15, height=1, font=("times", 15), bg="pink", fg="white",activebackground="white", activeforeground="black", command=save_photo, state=tk.DISABLED)
        salbtn.place(x=550, y=540)

        root.mainloop()