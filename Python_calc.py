from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Python Calculator")
root.geometry('550x200')
root.resizable(width=False, height=False)
color = "gray60"
root.configure(bg=color)

frame1 = Frame(root, width=550, height=50, bg=color)
frame1.pack(side=TOP)
frame2 = Frame(root, width=550, height=50, bg=color)
frame2.pack(side=TOP)
frame3 = Frame(root, width=550, height=50, bg=color)
frame3.pack(side=TOP)
frame4 = Frame(root, width=550, height=50, bg=color)
frame4.pack(side=TOP)

label = Label(frame1, text="Input Number 1 : ", bg=color)
label.place(x=40, y=17)
entry = Entry(frame1, width=40)
entry.place(x=160, y=17)

label1 = Label(frame2, text="Input Number 2 : ", bg=color)
label1.place(x=40, y=17)
entry1 = Entry(frame2, width=40)
entry1.place(x=160, y=17)


def msg(txt):
    tkinter.messagebox.showinfo("Error", txt)


def cls():
    res_entry.delete(0, END)


def addition():
    cls()
    try:
        res_entry.insert(0, int(entry.get()) + int(entry1.get()))
    except:
        msg("Error!!!")


def subtract():
    cls()
    try:
        res_entry.insert(0, int(entry.get()) - int(entry1.get()))
    except:
        msg("Error!!!")


def multiply():
    cls()
    try:
        res_entry.insert(0, int(entry.get()) * int(entry1.get()))
    except:
        msg("Error!!!")


def division():
    if int(entry1.get()) == 0:
        msg("Cannot divide number by 0")
    cls()
    try:
        res_entry.insert(0, int(entry.get()) / int(entry1.get()))
    except:
        msg("Error!!!")


bcolor = "white"

rbtn1 = Button(frame3, text="+", bg=bcolor, width=17, command=lambda: addition())
rbtn1.place(x=10, y=17)

rbtn2 = Button(frame3, text="-", bg=bcolor, width=17, command=lambda: subtract())
rbtn2.place(x=160, y=17)

rbtn3 = Button(frame3, text="*", bg=bcolor, width=17, command=lambda: multiply())
rbtn3.place(x=310, y=17)

rbtn4 = Button(frame3, text="/", bg=bcolor, width=11, command=lambda: division())
rbtn4.place(x=460, y=17)

res = Label(frame4, text="Result : ", bg=color)
res.place(x=120, y=17)
res_entry = Entry(frame4, width=40)
res_entry.place(x=190, y=17)

root.mainloop()
