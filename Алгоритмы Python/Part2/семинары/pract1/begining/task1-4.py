import math

class Task1Class:
    """
    Задача 1. Создайте класс с методом класса, в котором определялась бы сумма двух целых чисел.
    """
    @staticmethod
    def sum(a, b):
        return a+b

class Task2Class:
    """
    Задача 2. Создайте класс с методом-конструктором, в котором следует определить атрибуты
    экземпляра класса, необходимые для сложения двух целых чисел. Напишите метод, в котором
    бы определялась сумма двух целых чисел.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self.b

#TODO
class Task3Class:
    """
    Задача 3. Создайте класс с методами, формирующими вложенную последовательность.
    Пользователю должна быть предоставлена возможность заполнить ее либо случайными числами в
    интервале [-10; 10], либо осуществить ввод данных с клавиатуры.
    """

class Task4Class:
    """
    Разработайте класс с соответствующими методами, обеспечивающий нахождение
значения функции г и вывод на экран результатов вычислений, Исходные данные в соответстви
с вариантом функции первого семестра.
    """

    def __init__(self, x):
        self.x = x
        self.getter()

    def getter(self):

        x = self.x
        upper = x ** 3 * math.e ** (x - 1)
        lower = x ** 3 - math.fabs(x)
        if lower == 0:
            print("Знаменатель равен нулю, деление на 0!")
            self.result = 0
            return

        first = upper / lower

        log_sqrt = math.sqrt(x) - x

        if log_sqrt >= 0:
            buf_log = math.log(log_sqrt, 2)
        else:
            print("Выражение в log[sqrt(x)-x,2] меньше 0!")
            self.result = 0
            return

        self.result = first - buf_log

def main():
    print("Задание 1:", Task1Class.sum(3,4))
    obj = Task2Class(2,4)
    print("Задание 2:", obj.sum())


    print("*Задание 4 на условные операторы*")
    try:
        x = float(input("Введите x -> "))
    except:
        print("Проблема ввода данных!")
        return
    
    obj = Task4Class(x)
    print("Результат: " + str(obj.result))


if __name__ == "__main__":
    main()