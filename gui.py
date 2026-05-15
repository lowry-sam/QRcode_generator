from tkinter import *
from tkinter import colorchooser
import qrcode
import generator

website = ""
name = ""
my_color = ""

window = Tk()
window.title("QR Code Generator")
window.geometry("400x400")

def find_color():
    my_color = colorchooser.askcolor()[0]
    my_label = Label(window, text=my_color).pack(pady=10)

pick_color = Button(window, text="Pick Color", command=find_color).pack()


entry = Entry()
entry.config(font=('Calibri', 30), bg = "red", fg = "green", width=10)
entry.pack()


def submit(): 
    website = entry.get()
    print(website)

def reset():
    entry.delete(0,END)

submit = Button(window,text="submit", command=submit).pack()

delete = Button(window, text="clear", command=reset).pack()

window.mainloop()