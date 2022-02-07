from .task1 import Task1Class


def main():
    a = float(input("Введите число №1 ->"))
    b = float(input("Введите число №2 ->"))
    result = Task1Class.sum(a, b)
    print("Задание №1, сумма чисел {} и {}: {}".format(a, b, result))
