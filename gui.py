from tkinter import *
from tkinter import colorchooser, PhotoImage, messagebox
import pyqrcode
import png
import segno
import os
import shutil
from PIL import Image, ImageTk

"""import qrcode 
from colors import colors
import re
from colorama import Fore, Back, Style
import os
from PIL import Image"""
#import sys
# sys.path.append('f:\Programming_Projects\QRcode_generator')
# import qrcode
#import generator
#from main import my_function

url = pyqrcode.create('https://pythonguides.com/')
print(url.terminal(quiet_zone=1))

class QRCode:
    website = ""
    file_name = ""
    chosen_color = ""
#global submit
def submit_func(): 
    web = entry.get()
    error_label1 = Label()
    if web=="":
        messagebox.showwarning("warning", "Website URL is required.")
    else:
        QRCode.website=web
    """if web=="":
        error_label1.config(font=('Calibri', 8, "bold"), 
                            fg="red",
                            bg="white",
                            justify="left", 
                            anchor='w', 
                            padx = 5, 
                            text="You must input a URL!", 
                            cursor="",
                            pady=5)
        error_label1.grid(row=1, column=2)
    else:
        QRCode.website = web 
        error_label1.config(fg="white", font=0, bg="white", width=40)
        error_label1.grid(row=1, column=2)
    file_n=entry2.get()
    error_label2 = Label()
    if file_n=="":
        error_label2.config(font=('Calibri', 8, "bold"), 
                            fg="red",
                            bg="white",
                            justify="left", 
                            anchor='w', 
                            padx = 5, 
                            text="You must input a file name!", 
                            cursor="",
                            pady=5)
        error_label2.grid(row=2, column=2)
    else:
        QRCode.file_name = file_n + ".png"
        error_label2.config(fg="white", font=0, bg="white", width=40)
        error_label2.grid(row=2, column=2)"""
    ext = opt.get()
    if ext=="File Type":
        ext = "png"

    file_n=entry2.get()
    error_label2 = Label()
    
    if file_n=="":
        QRCode.file_name= web + "_qrcode." + ext
        file_n_png = web + "_qrcode" + ".png"
        dummy = web + "_qrcode"
        #file_n = "something_qrcode"
    else:
        QRCode.file_name = file_n + "." + ext
        file_n_png = file_n + ".png"
        dummy = file_n
    
        

    if not QRCode.chosen_color:
        QRCode.chosen_color="#000000"
    
    
    #print(QRCode.website)
    #print(QRCode.file_name)
    #print(QRCode.chosen_color)
    if not(QRCode.website == ""):
        """ qr = pyqrcode.create(QRCode.website)
        print(qr.terminal(quiet_zone=1))
        qr.png(QRCode.file_name, scale=10, background="red")
        qr.show()
        img = BitmapImage(data = qr)
        img_label=Label(window, bg='#F25252',image=img)
        img_label.place(relx=.5,rely=.5,anchor="center")"""
        if not ext == "jpeg":
            print(QRCode.file_name)
            qr=segno.make_qr(QRCode.website)
            qr.save(QRCode.file_name,
                    scale=50,
                    dark=QRCode.chosen_color)
        else:
            print("here")
            qr=segno.make_qr(QRCode.website)
            qr.save(file_n_png,
                    scale=50,
                    dark=QRCode.chosen_color)
        
        #os.makedirs("generated_codes", exist_ok=True)        
        #qr.save(os.path.join("generated_codes", QRCode.file_name))
        #print(QRCode.file_name)
       
        #image=PhotoImage(file=QRCode.file_name)
        #img_label.config(image=image)

        
        
        #qr.show()

        
        
        """ success = Label()
        success.config(bg="white", height=1000, width=1000)
        success.place(relx=0,rely=0)"""
        window.geometry("600x700")
        submit.place(relx=0.5,rely=.385)
        submit.config(state="disabled")
        #submit.destroy()
        pick_color.place(relx=0.5, rely=0.255, anchor="center")    
        pick_color.config(state="disabled")
        delete.place(relx=0.5,rely=.3225)
        delete.config(state="disabled")
        #delete.destroy()
        title.place(relx=0.5,rely=0.065)
        entry.config(state="disabled")
        entry2.config(state="disabled")

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
            print(file_n_png)
            print(file_n)
            imgg = Image.open(file_n_png).convert('RGB').save(dummy + '.jpeg')
            img = Image.open(file_n_png)
        """try:
            img = Image.open(QRCode.file_name)
        except: 
            qr=segno.make_qr(QRCode.website)
            qr.save(web + "_qrcode.png",
                scale=50,
                dark=QRCode.chosen_color)
            img = Image.open(web + "_qrcode.png")"""
        resize = img.resize((300,300))

        image = ImageTk.PhotoImage(resize)
        bp = "F:\Programming_Projects\QRcode_generator"
        bq = "F:\Programming_Projects\QRcode_generator\generated_codes"
        fn = QRCode.file_name
        folder = "generated_codes"
        fp = os.path.join(bp, fn)
        fq = os.path.join(bp, folder)
        full = os.path.join(bq, QRCode.file_name)
        print(full)
        print(fq)
        try: shutil.move(fp, fq)
        except: shutil.move(fp, full)
        #resize_image = image.zoom(5, 5)
        img_label.config(image=image)
        img_label.place(relx=0.5,rely=0.68, anchor="center")
        if not ext=="png":
            os.remove(os.path.join(bp, file_n_png))
       # os.makedirs("generated_codes", exist_ok=True)        
        #image.save(os.path.join("generated_codes", QRCode.file_name))

        global code, code2, new_code
        code = Label()
        code.config(text="Here is your QR Code!",
                    font=("Calibri",25, "bold"),
                    fg="black",
                    bg="white")
        code.place(relx=.5,rely=.47,anchor="center")

        code2 = Label()
        code_var=StringVar()
        code_var.set("Your QR code was saved under " + QRCode.file_name)
        code2.config(textvariable=code_var,
                    font=("Calibri",12, "bold"),
                    fg="black",
                    bg="white")
        code2.place(relx=.5,rely=.9,anchor="center")

        #OptionMenu(window, opt, *file_types).config(state="disabled")
        
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
        new_code.place(relx=0.5,rely=0.95,anchor="center")

        """new_code = Button()
        new_code.config(text="Create another code", command=success.destroy() and new_code.destroy())
        new_code.place(relx=.5,rely=.5)"""
    
"""def my_function (text, file_name, color):
    qr = qrcode.QRCode(
        version = 1, 
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size = 20, 
        border = 2,
    )
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color=color, back_color='white')
                
    os.makedirs("generated_codes", exist_ok=True)        
    img.save(os.path.join("generated_codes", file_name))
    img.show()"""

def reset():
    entry.delete(0,END)
    entry2.delete(0,END)
    QRCode.chosen_color="#000000"

def get_new_code():
    window.geometry("600x300")
    
    entry.config(state="normal")
    entry2.config(state="normal")
    entry.delete(0,END)
    entry2.delete(0,END)

    pick_color.config(state="normal")
    pick_color.place(relx=0.5, rely=0.6, anchor="center")
    title.place(relx=.5,rely=0.15,anchor="center")
    

    img_label.grid_forget()
    img_label.place(rely=1.5)
    code.place(rely=1.5)
    code2.place(rely=1.5)
    code.grid_forget()
    code2.grid_forget()
    #new_code.grid_forget()
    new_code.destroy()
    code.place(rely=1.5)
    code2.place(rely=1.5)
    submit.place(relx=0.5,rely=0.9,anchor="center")
    delete.place(relx=0.5,rely=0.755,anchor="center")
    submit.config(state="normal")
    delete.config(state="normal")
    opt = StringVar(value="File Type")
    OptionMenu(window, opt, *file_types).config(state="normal")
    

def find_color():
    my_color = colorchooser.askcolor()[1]
    print(my_color)
    QRCode.chosen_color=my_color
    #pick_color.config(cursor="")
    """if my_color:
        chosen_color=my_color
        print(chosen_color)"""


"""def create_buttons():
    submit.config(text="Submit", 
                #command=submit, 
                command=submit_func,
                activebackground="gray", 
                   activeforeground="black",
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
                   pady=3,
                   width=5,
                   wraplength=1000)
    submit.place(relx=0.5,rely=0.9,anchor="center")

    delete.config(text="Reset", command=reset,  
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
                    pady=2)
    delete.place(relx=0.5,rely=0.755,anchor="center")"""


window = Tk()
window.title("QR Code Generator")
window.geometry("600x300")
window.config(bg="white")
window.resizable(height=FALSE,width=FALSE)

global submit, delete
#submit = Button(window)
#delete = Button(window)


blank = Label()
blank.config(pady=30, height=0)
blank.grid(row=0,column=0)

title = Label()
#title.place(relx=.5,rely=0.15,anchor="center")
title.config(font=("Calibri",25, "bold"), 
             bg="white",
             text="Welcome to the QR code generator!",
             padx=10,
             pady=40,
             anchor="center",
             justify="center")
title.grid(column=0, row=0, columnspan=5)

img_label=Label(window)
img_label.place(relx=0.1,rely=0.5)
#img_label.grid(column=0,row=3)


entry_label = Label()
entry_label.config(font=('Calibri', 12), 
                   bg="white",
                   justify="left", 
                   anchor='w', 
                   padx = 5, 
                   fg = "black", 
                   text="Website URL:", 
                   cursor="",
                   pady=5)
entry = Entry()
entry.config(font=('Calibri', 12), bg = "white", fg = "black", width=40, cursor="hand2")
entry_label.grid(row=1, column=0)
entry.grid(row=1, column=1)

entry_label2 = Label()
entry_label2.config(font=('Calibri', 12),  
                    bg="white",
                    justify="left", 
                    padx = 5, 
                    fg = "black", 
                    text="Name of QR code:", 
                    cursor="",
                    pady=5)

entry2 = Entry()
entry2.config(font=('Calibri', 12), bg = "white", fg = "black", width=40, cursor="")
entry_label2.grid(row=2, column=0)
entry2.grid(row=2, column=1)

drop_down_label = Label()
drop_down_label.config(font=('Calibri', 12),  
                    bg="white",
                    justify="left", 
                    padx = 5, 
                    fg = "black", 
                    text="File Type:", 
                    cursor="",
                    pady=5,
                    width=6,
                    anchor="e")
drop_down_label.grid(row=3, column=0)
file_types = ["png", "jpeg", "svg"]
opt = StringVar(value="File Type")
OptionMenu(window, opt, *file_types).grid(row=4, column=0)
OptionMenu(window, opt, *file_types).config(anchor="e")

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
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   width=15,
                   pady=3,
                   wraplength=1000)
pick_color.place(relx=0.5, rely=0.6, anchor="center")


submit = Button(window, text="Submit", 
                #command=submit, 
                command=submit_func,
                activebackground="gray", 
                   activeforeground="black",
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
                   pady=3,
                   width=5,
                   wraplength=1000)
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
                    pady=2)
submit.place(relx=0.5,rely=0.9,anchor="center")
delete.place(relx=0.5,rely=0.755,anchor="center")


#OptionMenu.place(relx=0.9, rely=0.8)

window.mainloop()
