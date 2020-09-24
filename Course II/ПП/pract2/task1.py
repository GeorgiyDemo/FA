import tkinter as tk
from math import sin, cos, pi 

def drawer(canvas, x, y):
    """Создание точки"""
    #canvas.create_line(x, y, x+1, y, fill="black")
    canvas.create_line(x, y, x+1, y, fill="black")

def sgn(x): 
	return ((x>0)-(x<0))*1

def processing(canvas, a, b, n):
    na = 2 / n 
    # defining the accuracy 
    step = 10000
    piece =(pi * 2)/step 
    xp =[]
    yp =[]
    t = 0
    
    for t1 in range(step + 1): 
        # because sin ^ n(x) is mathematically the same as (sin(x))^n... 
        x =(abs((cos(t)))**na)*a * sgn(cos(t)) 
        y =(abs((sin(t)))**na)*b * sgn(sin(t)) 
        xp.append(x)
        yp.append(y) 
        t+= piece 

    if len(xp) == len(yp):
        print("Точки совпадают")
        for i in range(len(xp)):
            drawer(canvas, xp[i], yp[i])
    else:
        print("Точки не совпадают")
    #plt.plot(xp, yp) # plotting all point from array xp, yp 

if __name__ == "__main__":

    width = 600
    height = 600
    center_x = width // 2
    center_y = height // 2


    root = tk.Tk()
    c = tk.Canvas(root, width=width, heigh=height)
    

    n = 0.4
    while n != 2.5:    
        a, b = 200, 200
        processing(c,a,b,n)
        n  = round(n + 0.1, 1)
        break

    c.pack()

    root.mainloop()
