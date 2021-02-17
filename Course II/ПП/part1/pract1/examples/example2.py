from tkinter import *


class Block:
    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.b = Button(master, text="Преобразовать")
        self.l = Label(master, bg="black", fg="white", width=20)
        self.e.pack()
        self.b.pack()
        self.l.pack()

    def setFunc(self, func):
        self.b["command"] = eval("self." + func)

    def strToSortlist(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l["text"] = " ".join(s)

    def strReverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l["text"] = " ".join(s)


root = Tk()
first_block = Block(root)
first_block.setFunc("strToSortlist")
second_block = Block(root)
second_block.setFunc("strReverse")
root.mainloop()
