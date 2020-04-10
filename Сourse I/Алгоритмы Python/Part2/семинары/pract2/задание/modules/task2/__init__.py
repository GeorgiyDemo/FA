from .task2 import Task2Class


def main():
    a = float(input("Введите число №1 ->"))
    b = float(input("Введите число №2 ->"))
    obj = Task2Class(a, b)
    print("Задание 2:", obj.sum())
