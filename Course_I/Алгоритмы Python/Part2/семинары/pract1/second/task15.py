"""
Задача 15. Создайте класс ПРОГРЕССИЯ с методами вычисления N-го элемента прогрессии,
ее суммы и методом, выводящим сумму на экран.
Создайте дочерние классы: АРИФМЕТИЧЕСКАЯ, ГЕОМЕТРИЧЕСКАЯ со своими методами вычисления.
Создайте список п прогрессий и выведите сумму каждой из них экран.
"""

from random import randint


class ProgressionClass:
    def get_sum(self):
        return self.s

    def calculate(self):
        ...

    def info(self):
        ...


class ArithmeticClass(ProgressionClass):
    def __init__(self, a1, a2, n):
        self.a1 = a1
        self.a2 = a2
        self.n = n

        self.calculate()

    def calculate(self):
        self.s = (self.a1 + self.a2) * self.n / 2

    def info(self):
        return (
            "[Арифметическая прогрессия]\n1-й элемент: "
            + str(self.a1)
            + "\n2-й элемент: "
            + str(self.a2)
            + "\nШаг: "
            + str(self.n)
            + "\nСумма: "
            + str(self.s)
        )


class GeometricClass(ProgressionClass):
    def __init__(self, b1, q):
        self.b1 = b1
        self.q = q
        self.calculate()

    def calculate(self):
        self.s = self.b1 / (1 - self.q)

    def info(self):
        return (
            "[Геометрическая прогрессия]\nЗнаменатель прогрессии: "
            + str(self.q)
            + "\n1-й элемент: "
            + str(self.b1)
            + "\nСумма: "
            + str(self.s)
        )


def main():
    # Создайте список п прогрессий и выведите сумму каждой из них экран.
    try:
        n = int(input("Введите кол-во прогрессий для генерации -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: ArithmeticClass,
        2: GeometricClass,
    }

    progression_list = []

    for _ in range(n):
        d_args = {
            1: [randint(-1000, 1000), randint(-1000, 1000), randint(1, 10)],
            2: [randint(-1000, 1000), randint(-1000, 1000)],
        }

        r_number = randint(1, 2)
        progression_list.append(d[r_number](*d_args[r_number]))

    for e in progression_list:
        # print(e.get_sum())
        print(e.info() + "\n")


if __name__ == "__main__":
    main()
