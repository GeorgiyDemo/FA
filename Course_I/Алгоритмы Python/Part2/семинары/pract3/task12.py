"""
12* Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом
0. Выведите первое, третье, пятое и т.д. из введенных чисел. Завершающий ноль выводить не
надо.
В этой задаче нельзя использовать глобальные переменные и передавать какие-либо параметры
в рекурсивную функцию. Функция получает данные, считывая их с клавиатуры. Функция не
возвращает значение, а сразу же выводит результат на экран. Основная программа должна
состоять только из вызова этой функции.
"""


def r_def():
    n = int(input())
    if n > 0:
        m = int(input())
        print(n)
        if m > 0:
            r_def()


if __name__ == "__main__":
    r_def()
