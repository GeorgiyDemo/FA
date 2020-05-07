"""
Определённые интегралы, представленные в таблице заданий (приложение 1), вычислить:
•	Методом трапеций
•	С использованием квадратурной формулы Симпсона

Результаты вывести на экран.
"""
import math


def f1(x):
    """Функция для интегрирования №1"""
    return x*math.tan(pow(x,2)+1)

def f2(x):
    """Функция для интегрирования №2"""
    return ((pow(math.log(x+1),2))/x)*pow(math.e,-x)

def trapezoid(f, a, b, n):
    """Метод трапеций"""
    result = 0
    h = (b-a)/n
    for i in range(1, n + 1):
        x_i = a + i*h
        x_prev = a + (i-1)*h
        result += (f(x_prev) + f(x_i)) / 2 * h
    return result


def simpson(f, a, b, n):
    """Метод Симпсона"""
    result = 0
    h = (b-a)/n
    for i in range(1, n):
        x = a+i*h
        if i % 2 == 0:
            result += 2*f(x)
        else:
            result += 4*f(x)
    result += f(a)+f(b)
    result *= h/3
    return result


def iterate_upto_precision(method, f, a, b, precision=10**-6):
    """Интегрирование с заданной точностью"""
    n = 4
    while True:
        res_n = method(f, a, b, n)
        res_2n = method(f, a, b, 2*n)
        if abs(res_n - res_2n) > precision:
            n *= 2
        else:
            return n, res_2n


def main():

    main_list = [{"f":f1, "a": 0, "b" : 0.6},{"f": f2, "a": 0, "b" : 1}]
    for d in main_list:
        n, res = iterate_upto_precision(trapezoid, **d)
        print('Интегрирование методом трапеций\nРезультат: {}, число разбиений интервала n = {}'.format(res, n))
        n, res = iterate_upto_precision(simpson, **d)
        print('Интегрирование методом Симпсона\nРезультат: {}, число разбиений интервала n = {}'.format(res, n))

if __name__ == "__main__":
    main()
