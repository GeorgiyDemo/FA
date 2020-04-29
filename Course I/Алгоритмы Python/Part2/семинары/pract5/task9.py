"""
Задача 9:
Дан список/массив целых чисел. Упорядочьте по возрастанию только:
а) положительные числа;
б) элементы с четными порядковыми номерами в списке.
"""
import array as ar
from random import randint

def a_processing(arr):
    buf_list = []
    for i in range(len(arr)):
        if arr[i] > 0:
            buf_list.append(arr[i])
    buf_list.sort()
    index = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = buf_list[index]
            index += 1
    return arr

def b_processing(arr):
    buf_list = []
    arr = self.l
    for i in range(len(arr)):
        if i % 2 == 0:
            buf_list.append(arr[i])
    buf_list.sort()

    index = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = buf_list[index]
            index += 1
    self.b_l = arr

def main():
    try:
        n = int(input("Введите кол-во элементов в массиве -> "))
    except ValueError:
        print("Некорректный ввод данных!")
        return
    #ar.array(
    arr = [randint(-100,100) for _ in range(n)]
    print("Исходный массив:", arr)

    #Упорядочить по возрастанию только положительные числа

    arr.sort(key=lambda x: x if x > 0)
    print(arr)

    """
    np_arr = np.vectorize(lambda x: x > 0, np_arr)
    np_arr.excluded =
    arr3 = np.argsort(np_arr)
    print(arr3)
    print(np.sort(np_arr, 0, np.where(np_arr < 0)))
    """
if __name__ == "__main__":
    main()