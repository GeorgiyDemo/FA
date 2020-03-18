import math
from random import randint
from .quadraticequation import QuadraticEquation
from .linearequation import LinearEquation
def main():
    try:
        n = int(input("Введите количество уравнений -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d, main_list = {1: LinearEquation, 2: QuadraticEquation}, []
    for _ in range(n):
        d_args = {1: [randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)],2: [str(randint(-1000, 1000)) + "x^2+" + str(randint(-1000, 1000)) + "x+" + str(randint(-1000, 1000)) + "=0"],}
        r_number = randint(1, 2)
        main_list.append(d[r_number](*d_args[r_number]))
    for e in main_list: print(e.info() + "\n")
if __name__ == "__main__":
    main()