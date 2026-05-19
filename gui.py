from tkinter import *
from tkinter import colorchooser, PhotoImage, messagebox
import segno
import os
import shutil
from PIL import Image, ImageTk
from pathlib import Path

directory = Path(__file__).resolve().parent

class QRCode:
    website = ""
    file_name = ""
    chosen_color = ""

def submit_func(): 
    web = entry.get()
    file_n=entry2.get()
    ext = opt.get()
    
    if ext=="File Type":
        ext = "png"

    if  len(entry.get()) < 1:
        messagebox.showwarning("warning", "Website URL is required.")
    else:
        QRCode.website=web

    if file_n=="":
        QRCode.file_name= web + "_qrcode." + ext
        file_n_png = web + "_qrcode" + ".png"
        file_n_unchanged = web + "_qrcode"
    else:
        QRCode.file_name = file_n + "." + ext
        file_n_png = file_n + ".png"
        file_n_unchanged = file_n
    
    if not QRCode.chosen_color:
        QRCode.chosen_color="#000000"
    
    if len(entry.get()) > 0:
        qr=segno.make_qr(QRCode.website)
        if not ext == "jpeg":
            qr.save(QRCode.file_name,
                    scale=50,
                    dark=QRCode.chosen_color)
        else:
            qr.save(file_n_png,
                    scale=50,
                    dark=QRCode.chosen_color)
            
        window.geometry("525x750")
        disable_enable()

        global image
        if ext == "png":
            img = Image.open(QRCode.file_name)
        elif ext == "svg":
            qr=segno.make_qr(QRCode.website)
            qr.save(file_n_png,
                scale=50,
                dark=QRCode.chosen_color)
            img = Image.open(file_n_png)
        else:
            imgg = Image.open(file_n_png).convert('RGB').save(file_n_unchanged + '.jpeg')
            img = Image.open(file_n_png)
        resize = img.resize((300,300))
        image = ImageTk.PhotoImage(resize)

        """bp = directory
        bq = os.path.join(directory,"generated_codes")
        fn = QRCode.file_name
        folder = "generated_codes"
        fp = os.path.join(bp, fn)
        fq = os.path.join(bp, folder)
        full = os.path.join(bq, QRCode.file_name)
        try: shutil.move(fp, fq)
        except: shutil.move(fp, full)
        
        if not ext=="png":
            os.remove(os.path.join(bp, file_n_png))"""

        global code, code2, new_code
        code = Label()
        code.config(text="Here is your QR Code!",
                    font=("Calibri",25, "bold"),
                    fg="black",
                    bg="white",
                    justify="center",
                    anchor="center")
        code.grid(column=0, row=5, columnspan=3)

        img_label.config(image=image)
        img_label.grid(column=0, row=6, columnspan=3,)

        code2 = Label()
        code_var=StringVar()
        code_var.set("Your QR code was saved under " + QRCode.file_name)
        code2.config(textvariable=code_var,
                    font=("Calibri",12, "bold"),
                    fg="black",
                    bg="white", 
                    justify="center",
                    anchor="center")
        code2.grid(column=0, row=7, columnspan=3)
        
        new_code = Button(window, text="New code!", 
                          command=get_new_code,  
                            activebackground="blue", 
                            activeforeground="white",
                            anchor="center",
                            bd=3,
                            bg="white",
                            cursor="hand2",
                            disabledforeground="gray",
                            fg="black",
                            font=("Calibri", 12),
                            height=-2,
                            highlightbackground="black",
                            highlightcolor="green",
                            highlightthickness=2,
                            justify="center",
                            overrelief="raised",
                            padx=2,
                            width=10,
                            wraplength=1000,
                            pady=2)
        new_code.grid(column=0, row=8, columnspan=3, pady=5, sticky="n")
        
        credit.place(rely=0.98)
        #OptionMenu(window, opt, *file_types).config(state="disabled")

def reset():
    entry.delete(0,END)
    entry2.delete(0,END)
    QRCode.chosen_color="#000000"

def get_new_code():
    window.geometry("525x325")
    credit.place(rely=0.95)
    disable_enable()
    entry.delete(0,END)
    entry2.delete(0,END)
    QRCode.chosen_color="#000000"
    img_label.grid_forget()
    code.grid_forget()
    code2.grid_forget()
    new_code.destroy()
    opt.set("File Type")
    #OptionMenu(window, opt, *file_types).config(state="normal")
    
def find_color():
    my_color = colorchooser.askcolor()[1]
    QRCode.chosen_color=my_color


def disable_enable():
    number.set(number.get()+1)
    if (number.get()%2==0):
        entry.config(state="normal")
        entry2.config(state="normal")
        pick_color.config(state="normal")
        submit.config(state="normal")
        delete.config(state="normal")
    else: 
        entry.config(state="disabled")
        entry2.config(state="disabled")
        pick_color.config(state="disabled")
        submit.config(state="disabled")
        delete.config(state="disabled")

window = Tk()
window.title("QR Code Generator")
window.geometry("525x325")
window.config(bg="white")
window.resizable(height=FALSE,width=FALSE)

number = IntVar()
img_label=Label(window)

title = Label()
title.config(font=("Calibri",25, "bold"), 
             bg="white",
             text="Welcome to the QR Code Generator!",
             padx=10,
             pady=20,
             anchor="center",
             justify="center")
title.grid(column=0, row=0, columnspan=4, sticky="n")

credit = Label()
credit.config(font=("Calibri",8, "bold"), 
             bg="white",
             text="A python app created by Sam Lowry, 2026",
             padx=10,
             pady=5,
             anchor="center",
             justify="center",
             fg = "red")
credit.place(rely=0.95, relx=0.5, anchor="center")

entry_label = Label()
entry_label.config(font=('Calibri', 12), 
                   bg="white",
                   justify="left", 
                   anchor='e', 
                   padx = 5, 
                   fg = "black", 
                   text="Website URL:", 
                   cursor="",
                   pady=5)
entry_label.grid(row=1, column=0, sticky="w")
                   
entry = Entry()
entry.config(font=('Calibri', 12), bg = "white", fg = "black", width=30, cursor="")
entry.grid(row=1, column=1, sticky="w")

entry_label2 = Label()
entry_label2.config(font=('Calibri', 12),  
                    bg="white",
                    justify="left", 
                    padx = 5, 
                    fg = "black", 
                    text="Name of QR code:", 
                    cursor="",
                    pady=5)
entry_label2.grid(row=2, column=0, sticky="w")

entry2 = Entry()
entry2.config(font=('Calibri', 12), bg = "white", fg = "black", width=30, cursor="")
entry2.grid(row=2, column=1, sticky="w")

drop_down_label = Label()
drop_down_label.config(font=('Calibri', 12),  
                    width=10,
                    text="File Type:", 
                    justify="left",
                    anchor="w",
                    padx=10,
                    bg="white"
                    )
drop_down_label.grid(row=1, column=2, sticky="w")

file_types = ["png", "jpeg", "svg"]
opt = StringVar(value="File Type")
OptionMenu(window, opt, *file_types).grid(row=2, column=2, sticky="w", padx=5)
OptionMenu(window, opt, *file_types).config(anchor="e", width=10)

pick_color = Button(window,
                   text="Pick a color!", 
                   command=find_color,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="white",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Calibri", 16),
                   #height=10,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   width=15,
                   pady=10,
                   
                   wraplength=1000)
pick_color.grid(column=0, row=3, columnspan=4, pady=10)


submit = Button(window, text="Submit", 
                command=submit_func,
                activebackground="red", activeforeground="black",
                anchor="center",
                bd=3,
                bg="blue",
                fg="white",
                cursor="hand2",
                disabledforeground="gray",
                font=("Calibri", 14),
                height=-2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=10,
                pady=5,
                width=5,
                wraplength=1000)
submit.grid(column=0, row=4, columnspan=4, pady=5, sticky="N")

delete= Button(window, text="Reset", command=reset,  
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="white",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Calibri", 10),
                height=-2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=2,
                width=5,
                wraplength=1000,
                pady=5)
#delete.grid(column=0, row=3, columnspan=1, sticky="se")

window.mainloop()