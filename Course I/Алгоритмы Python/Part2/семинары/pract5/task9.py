"""
Задача 9:
Дан список/массив целых чисел. Упорядочьте по возрастанию только:
а) положительные числа;
б) элементы с четными порядковыми номерами в списке.
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

    #Упорядочить по возрастанию только положительные числа
    


    np_arr = np.vectorize(lambda x: x > 0, np_arr)
    print(np.array([np_arr]))
    arr3 = np.argsort(np_arr)
    print(arr3)
 
    #print(np.sort(np_arr, 0, np.where(np_arr < 0)))

if __name__ == "__main__":
    main()