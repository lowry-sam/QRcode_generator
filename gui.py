from tkinter import * 
from tkinter import colorchooser, PhotoImage
import pyqrcode
import png
import segno

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

def submit(): 
    web = entry.get()
    error_label1 = Label()
    if web=="":
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
        error_label2.grid(row=2, column=2)
    
    print(QRCode.website)
    print(QRCode.file_name)
    print(QRCode.chosen_color)
    if not(QRCode.file_name == "" or QRCode.website == "" or QRCode.chosen_color == ""):
        """ qr = pyqrcode.create(QRCode.website)
        print(qr.terminal(quiet_zone=1))
        qr.png(QRCode.file_name, scale=10, background="red")
        qr.show()
        img = BitmapImage(data = qr)
        img_label=Label(window, bg='#F25252',image=img)
        img_label.place(relx=.5,rely=.5,anchor="center")"""

        qr=segno.make_qr(QRCode.website)
        qr.save(QRCode.file_name,
                scale=5,
                dark=QRCode.chosen_color)
        print(QRCode.file_name)
        image=PhotoImage(file=QRCode.file_name)
        
        
        #qr.show()

        
        
        """success = Label()
        success.config(bg="white", height=1000, width=1000)
        success.place(relx=0,rely=0)"""

        code = Label()
        code.config(text="Here is your QR Code!",
                    font=("Calibri",25, "bold"),
                    fg="black",
                    bg="white")
        code.place(relx=.5,rely=.1,anchor="center")

        img_label=Label(window, image=image)
        img_label.place(relx=0, rely=0)

        

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
    my_color=""

def find_color():
    my_color = colorchooser.askcolor()[1]
    print(my_color)
    QRCode.chosen_color=my_color
    #pick_color.config(cursor="")
    """if my_color:
        chosen_color=my_color
        print(chosen_color)"""


window = Tk()
window.title("QR Code Generator")
window.geometry("600x400")
window.config(bg="white")

blank = Label()
blank.config(pady=30, height=0)
blank.grid(row=0,column=0)

title = Label()
title.place(relx=.5,rely=0.1,anchor="center")
title.config(font=("Calibri",25, "bold"), 
             bg="white",
             text="Welcome to the QR code generator!",
             padx=10,
             pady=40)

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

pick_color= Button(window,
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
pick_color.place(relx=0.37, rely=0.4)


submit = Button(window, text="Submit", 
                command=submit, 
                activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="white",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
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
submit.place(relx=0.45,rely=0.74)

delete = Button(window, text="Reset", command=reset,  
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="white",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Calibri", 14),
                   height=-2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   width=5,
                   wraplength=1000,
                   pady=3)
delete.place(relx=0.45,rely=0.6)

window.mainloop()
