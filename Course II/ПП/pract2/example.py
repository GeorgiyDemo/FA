# Python program to implement 
# Superellipse 

# importing the required libraries 
import matplotlib.pyplot as plt 
from math import sin, cos, pi 

def sgn(x): 
	return ((x>0)-(x<0))*1

def processing(a, b, n):
    na = 2 / n 
    # defining the accuracy 
    step = 100
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

    print(xp)
    plt.plot(xp, yp) # plotting all point from array xp, yp 


def main():
    
    n = 0.4
    while n != 2.5:
    
        a, b = 200, 200
        processing(a,b,n)
        n  = round(n + 0.1, 1)
        break

    plt.title("Superellipse with parameter "+str(n)) 
    plt.show() 

if __name__ == "__main__":
    main()
