#Вариант 16
import math
from decimal import Decimal

def mechanic_calculator(x, e):

    #Знаменатель полный
    c = 1
    #Знаменатель малый
    c_part = -1
    #Числитель
    m = Decimal(pow(x,-1))
    #Сумма
    summ = 0
    i = 1

    while True:

        
        #Числитель
        m *= Decimal(pow(x,2))

        #Вычисляем знаменатель малый
        c_part = c_part+2
        
        #Вычисляем знаменатель N
        c = Decimal(math.factorial(c_part))
        
        #Получаем результат
        r = m / c

        print("n={}, ({}/{}!) = {}/{} = {}".format(i, m, c_part, m, c, r))
        summ += r
    
        if abs(r) < 10**-e:
            break
        else:
            i += 1

    return i, summ

def math_calculator(x):
    #Функция для подсчета результата с помощью math
    r = math.sinh(x)
    return r

# Проверка на ввод x
f = True
while f == True:
    x = float(input("Введите x: "))

    if abs(x) < float('inf'):
        f = False
    else:
        print("Значение не удовлетворяет условию задачи")
 
e = int(input("Введите степень погрешности e: "))
i, r = mechanic_calculator(x, e)
print("\nx="+str(x)+" при n="+str(i)+" и e=" +str(10**-e)+", результат: "+str(r))
r = math_calculator(x)
print("Результат с помощью math.log: "+str(r))