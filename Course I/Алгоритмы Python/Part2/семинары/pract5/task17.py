"""
Задача 17:
Сдвинуть элементы массива в указанном направлении (влево или вправо) и на указанное число
шагов. Освободившиеся ячейки заполнить нулями. Выводить массив после каждого шага.
"""
import numpy as np
from random import randint
def main():
    try:
        n = int(input("Введите кол-во элементов в массиве -> "))
    except ValueError:
        print("Некорректный ввод данных!")
        return
    np_arr = np.array([randint(-100,100) for _ in range(n)])
    print("Исходный массив:", np_arr)

    #Индекс
    itemindex = np.where(np_arr < 0)[0][0]
    print("Индекс первого отрицательного элемента: {}".format(itemindex))
    #Новый массив
    new_arr = np_arr[itemindex+1:]
    #Сумма по молулю
    s = np.sum((np.absolute(new_arr)))
    print("Сумма модулей после отрицательного элемента: {}".format(s))

if __name__ == "__main__":
    main()
