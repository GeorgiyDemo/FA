import math

class arcth:
    
    def __init__(self,x):
        if abs(x)>1:
            self.x=x
        else:
            raise ValueError("Введите |х|>1")
            
    def summa(self,n):
        p=1
        z=x
        s=1/x
        for _ in range(n):
            p+=2
            z*=(x)**2
            t=1/(p*z)
            s+=t
        return s
    
    def summa_eps(self,e):
        p=1
        z=x
        s=1/x
        t=1/x
        while abs(t)>=e:
            p+=2
            z*=(x)**2
            t=1/(p*z)
            s+=t
        return s

try:
    x=float(input("Введите x -> "))
    obj1=arcth(x)
    n=int(input("Введите N (количество членов) -> "))
    e=float(input("Введите e (точность вычисления) -> "))
    print("Сумма ",n," членов ряда -> ",obj1.summa(n))
    print("Сумма с точностью ",e," -> ",obj1.summa_eps(e))
    print("Ответ с помощью функции arcth -> ",(1/2*math.log1p((x+1)/(x-1))))
except ValueError as ve:
    print(ve,"\nПопробуйте ещё раз")