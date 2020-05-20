# Задание №1
x=float(input("Введите x -> "))
if abs(x)>1:
    p=1
    z=x
    s=1/x
    n=int(input("Введите N (количество членов) -> "))
    for i in range(n):
        p=p+2
        z=z*(x)**2
        t=1/(p*z)
        s=s+t
    print("Сумма ",n," членов -> ",s)
else:
    print("Введите |х|>1")


# Задание №2
import math

x=float(input("Введите x -> "))
if abs(x)>1:
    p=1
    z=x
    s=1/x
    t=1/x
    e=float(input("Введите e (точность вычисления) -> "))
    while abs(t)>=e:
        p=p+2
        z=z*(x)**2
        t=1/(p*z)
        s=s+t
    print("Сумма с точностью ",e," -> ",s)
else:
    print("Введите |х|>1")
    
print("\nОтвет с помощью функции arcth -> ",(1/2*math.log1p((x+1)/(x-1))))