"""
Определённые интегралы, представленные в таблице заданий (приложение 1), вычислить:
•	Методом трапеций
•	С использованием квадратурной формулы Симпсона

Результаты вывести на экран.
"""
import math


def f_1(x):
    """То, что именно мы интегрируем"""
    return x*math.tan(x**2+1)


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

    a = 0
    b = 0.6

    n, res = iterate_upto_precision(trapezoid, f_1, a, b)
    print(
        f'Интегрирование методом трапеций\nРезультат: {res}, число разбиений интервала n = {n}')
    n, res = iterate_upto_precision(simpson, f_1, a, b)
    print(
        f'Интегрирование методом Симпсона\nРезультат: {res}, число разбиений интервала n = {n}')


if __name__ == "__main__":
    main()
