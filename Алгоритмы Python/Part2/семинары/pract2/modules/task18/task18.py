import math
from random import randint

class LinearEquation(EquationClass):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # Поскольку я устал и мне надо сделать просто КАКОЕ-ТО ЛИНЕЙНОЕ УРАВНЕНИЕ
        self.calculation()

    def calculation(self):
        # Просто представляем, что вся задача сводится к решению ax+b=c
        self.result = (self.c - self.b) / self.a

    def info(self):
        a = self.a
        b = self.b
        c = self.c
        equation_str = str(a) + "x+" + str(b) + "=" + str(c)
        return "*Информация о простом линейном уравнении*\nОбщий вид: " + equation_str + "\nКоэффициент a = " + str(
            a) + "\nКоэффициент b = " + str(b) + "\nКоэффициент c = " + str(c) + "\nОтвет:\n" + str(self.result)





def main():
    # Создайте список n уравнений и выведите полную информацию об уравнениях на экран.
    try:
        n = int(input("Введите количество уравнений -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: LinearEquation,
        2: QuadraticEquation,
    }

    main_list = []

    for _ in range(n):
        d_args = {
            1: [randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)],
            2: [str(randint(-1000, 1000)) + "x^2+" + str(randint(-1000, 1000)) + "x+" + str(
                randint(-1000, 1000)) + "=0"],
        }

        r_number = randint(1, 2)
        main_list.append(d[r_number](*d_args[r_number]))

    for e in main_list:
        print(e.info() + "\n")


if __name__ == "__main__":
    main()
