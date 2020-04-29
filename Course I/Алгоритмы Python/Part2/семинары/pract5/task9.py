"""
Задача 9:
Дан список/массив целых чисел. Упорядочьте по возрастанию только:
а) положительные числа;
б) элементы с четными порядковыми номерами в списке.
"""
import numpy as np
from random import randint

def a_processing(arr):
    """По возрастанию только положительные числа"""
    buffer = arr[arr > 0]
    buffer = np.sort(buffer)
    index = 0
    for i in np.arange(arr.shape[0]):
        if arr[i] > 0:
            arr[i] = buffer[index]
            index += 1
    return arr

def b_processing(arr):
    """По возрастанию только элементы с четными порядковыми номерами"""
    buffer = arr[::2]
    buffer = np.sort(buffer)

    index = 0
    for i in np.arange(arr.shape[0]):
        if i % 2 == 0:
            arr[i] = buffer[index]
            index += 1
    return arr
    
def main():
    try:
        n = int(input("Введите кол-во элементов в массиве -> "))
    except ValueError:
        print("Некорректный ввод данных!")
        return

    arr = np.array([randint(-100,100) for _ in range(n)])
    print("Исходный массив:\n{}".format(arr))
    print("Упорядочьте по возрастанию только положительные числа:\n{}".format(a_processing(arr)))
    print("Упорядочьте по возрастанию только элементы с четными порядковыми номерами:\n{}".format(b_processing(arr)))

if __name__ == "__main__":
    main()