#Вариант 19
import math

def solve(x, n=1):
    w = 1  # для постороения факториала
    v = 2  # для постороения факториала
    a = 2  # первое базовое значение в числителе ~ 2^1, 2^3, ..., 2^(2*n-1)
    b = pow(x,2)  # второе базовое значение в числителе ~ x^2, x^4, ..., x^(2*n)
    c = 2  # базовое значение для факториала (т.к. начинается с 2)
    d = 1  # базовое значение для знака (т.к. чередуется)
    
    #Вычисляем результат
    result = d * a * b / c

    for i in range(n-1):
        v += 2  # для постороения факториала (рекуррентная формула)
        w += 2  # для постороения факториала (рекуррентная формула)
        # рекуррентные формулы
        a = a * 4
        b = b * pow(x,2)
        c = c * w * v
        #Чередование знака
        d = -d

        #Результат
        result += d * a * b / c
    #Т.к. 1- по условию
    return 1 - result

#Получение точного значения
def math_calc(x):
    result = pow(math.cos(x),2)
    return result

#Задание 1
def task_1(x):
    print('Точное значение с помощью модуля math: '+str(math_calc(x)))
    print('Вычисления с помощью ряда:')
    for i in range(5, 11):
        res = solve(x, i)
        print(f'При n = {i}: {res}')

#Задание 2
def task_2(x):
    print('Точное значение с помощью модуля math: '+str(math_calc(x)))
    e = [10**-3, 10**-5]
    for i in e:
        n = 3
        res_past = solve(x, 1)
        res = solve(x, 2)
        
        while abs(res - res_past) > i:
            res_past = res
            res = solve(x, n)
            n += 1
        print(f'При E = {i}: {res}')


flag = True
while flag:
    x = float(input('x = '))
    if x < 1:
        flag = False
    else:
        print("Введите верное значение x < 1")
 
print('\033[31mЗадание 1\033[0m')
task_1(x)
print()
print('\033[31mЗадание 2\033[0m')
task_2(x)
