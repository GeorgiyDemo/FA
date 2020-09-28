from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Шкала с ползунком")
        self.style = Style()
        self.style.theme_use("default")
 
        self.pack(fill=BOTH, expand=1)
 
        scale = Scale(self, from_=0, to=100, command=self.onScale)
        #scale.pack(side=LEFT, padx=15)
 
        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack(side=LEFT)
 
    def onScale(self, val):
        v = int(float(val))
        self.var.set(v)
 
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("250x100+300+300")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()