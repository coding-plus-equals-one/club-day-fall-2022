from tkinter import *
from tkinter import ttk

# import pytz
# import pygame

root = Tk()
root.title("Sign-Up Sheet")
root.geometry("350x475")

num = 1
qrcode = PhotoImage(file="qrcode.png")


def values():
    global num
    name = c.get()
    email = e.get()
    discinfo = g.get()
    info = str(num) + ". " + name + ", " + email + ", " + discinfo
    print(info)
    file = open("signupsheet.txt", "a")
    file.write(info)
    file.write("\n")
    file.close()
    c.delete(0, END)
    e.delete(0, END)
    g.delete(0, END)
    num += 1


a = Label(root, text="Sign-Up Sheet")
a.grid(row=0, column=1)
b = Label(root, text="Full Name:")
b.grid(row=1, column=0)
c = Entry(root)
c.grid(row=1, column=1, columnspan=2)
d = Label(root, text="Personal Email:")
d.grid(row=2, column=0)
e = Entry(root)
e.grid(row=2, column=1, columnspan=2)
f = Label(root, text="Discord(optional):")
f.grid(row=3, column=0)
g = Entry(root)
g.grid(row=3, column=1, columnspan=2)
h = Button(root, text="Submit", command=values)
h.grid(row=4, column=1)
i = Label(root, image=qrcode)
i.grid(row=5, column=0, columnspan=2)
j = Label(root, text="Check out our website using the QRcode above!")
j.grid(row=6, column=0, columnspan=2)
root.mainloop()
