from tkinter import *

root = Tk()

e = Entry(width=20)
b = Button(text="Преобразовать")
l = Label(bg="black", fg="white", width=20)


def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l["text"] = " ".join(s)


b.bind("<Button-1>", strToSortlist)

e.pack()
b.pack()
l.pack()
root.mainloop()
