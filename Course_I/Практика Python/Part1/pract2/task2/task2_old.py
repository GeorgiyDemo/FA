"""
Задача 2.
Задание:
Реализовать текстовый калькулятор для решения системы уравнений. Возможные уравнения
внутри системы: линейное, квадратное, кубическое, биквадратное. Добавить в программу
считывание с файла системы уравнения. Программа должна автоматически определять вид
уравнения, без явных указателей. Принцип ввода реализовать на усмотрение разработчика,
добавить его рядом с программой в виде текстового документа. Встроенными функциями и
библиотечными для решения уравнений и систем пользоваться ЗАПРЕЩЕНО.

Есть система тригонометрических уравнений вида:
a*cos(x)+b*sin(y)=c
d*cos(y)+e*sin(x)=k
, где a, b, c, d, e, k коэффициенты и вводятся с клавиатуры.
"""

import math

# если считать определитель и обратную матрицу по схеме: [url]http://www.cyberforum.ru/python/thread721979.html[/url], то numpy будет не нужен
import numpy as np


# считаем значение функции a*cos(x)+b*sin(y)-c и d*cos(y)+e*sin(x)-k в точке x,y при заданных a, b, c, d, e, k
def f(x, y, a, b, c, d, e, k):
    return a * math.cos(x) + b * math.sin(y) - c, d * math.cos(y) + e * math.sin(x) - k


# вычисляем матрицу Якоби
def matr_yakobi(v):
    matrix = [[]]

    w, h = 2, 2
    matrix = [[0 for x in range(w)] for y in range(h)]

    x = v[0]
    y = v[1]

    matrix[0][0] = -a * math.sin(x)
    matrix[0][1] = b * math.cos(y)

    matrix[1][0] = e * math.cos(x)
    matrix[1][1] = -d * math.sin(y)

    return matrix


def find_T(x0):
    x0 = np.array(x0)
    x0 = x0.T
    return x0


# подсчитываем обратную матрицу к матрице Якоби.
def find_Yakobi_inverse(Y):
    Y = np.matrix(Y)
    Y = Y.I
    new_Y = Y.tolist()
    return new_Y


# умножаем матрицу Якоби a на вектор b
def matmult(a, b):
    a0 = a[0][0] * b[0] + a[0][1] * b[1]
    a1 = a[1][0] * b[0] + a[1][1] * b[1]
    return [a0, a1]


# применяаем метод Ньютона для поиска новых значений x,y: здесь x0 -- это список, состоящий из x, y
def iteration(x0, a, b, c, d, e, k):
    fx0 = f(x0[0], x0[1], a, b, c, d, e, k)
    Yakobi = matr_yakobi(x0)

    det = np.linalg.det(Yakobi)
    if det == 0.0:
        print("DET=0, ERROR")

    Yakobi_inverse = find_Yakobi_inverse(Yakobi)
    y1 = matmult(Yakobi_inverse, fx0)

    x1 = [0.0, 0.0]
    return [x0[0] - y1[0], x0[1] - y1[1]]


a = 100
b = 1.5
c = -0.5
d = -1.5
e = 2
k = 1

a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
c = int(input("Введите значение c:"))
d = int(input("Введите значение d:"))
e = int(input("Введите значение e:"))
k = int(input("Введите значение k:"))
aa = float(input("Введите погрешность:"))

x0 = [0.5, 0.5]

x = x0[0]
y = x0[1]

while (
    abs(a * math.cos(x) + b * math.sin(y) - c) >= aa
    or abs(e * math.sin(x) + d * math.cos(y) - k) >= aa
):
    x0 = iteration(x0, a, b, c, d, e, k)
    x = x0[0]
    y = x0[1]

print("x=", x0[0], "y=", x0[1])
print(
    "Решение получено с помощью метода Ньютона. О нём можно прочитать здесь: [url]http://www.exponenta.ru/educat/systemat/hanova/equation/loc.asp[/url]"
)
