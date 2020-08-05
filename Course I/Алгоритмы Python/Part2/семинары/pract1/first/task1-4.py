import math
from random import randrange


class Task1Class:
    """
    Задача 1. Создайте класс с методом класса, в котором определялась бы сумма двух целых чисел.
    """

    @staticmethod
    def sum(a, b):
        return a + b


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


class Task3Class:
    """
    Задача 3. Создайте класс с методами, формирующими вложенную последовательность.
    Пользователю должна быть предоставлена возможность заполнить ее либо случайными числами в
    интервале [-10; 10], либо осуществить ввод данных с клавиатуры.
    """

    def __init__(self):
        try:
            d = {
                "1": self.user_input,
                "2": self.random_input,
            }
            self.main_list = []
            self.list_len = int(input("Введите длинну последовательности -> "))
            method_number = input(
                "Как вы хотите заполнить последовательность?\n1. Вручную\n2. Автоматически\n-> "
            )

            if method_number in d:
                d[method_number]()
                self.out_list()
            else:
                print("Некорректный ввод")

        except Exception as e:
            print("Возникла ошибка: ", e)

    def number_checker(self, e):
        """
        Фильтрация на числа
        """
        try:
            return int(e)
        except ValueError:
            return e

    def user_input(self):
        """
        Ручное заполнение последовательности
        """
        for i in range(self.list_len):
            locale_element = self.number_checker(
                input("Введите элемент №" + str(i + 1) + " -> ")
            )
            self.main_list.append(locale_element)

    def random_input(self):
        """
        Автоматическое заполнение последовательности
        """
        self.main_list = [randrange(-10, 10) for _ in range(self.list_len)]

    def out_list(self):
        """
        Вывод полученной последовательности
        """
        print("Полученная последовательность:")
        print(self.main_list)


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
    print("Задание 1:", Task1Class.sum(3, 4))
    obj = Task2Class(2, 4)
    print("Задание 2:", obj.sum())

    print("Задание 3:")
    Task3Class()

    print("\nЗадание 4:")
    try:
        x = float(input("Введите x -> "))
    except ValueError:
        print("Проблема ввода данных!")
        return

    obj = Task4Class(x)
    print("Результат: " + str(obj.result))


if __name__ == "__main__":
    main()
