"""
Задача 3:
Выполните oбработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов. Все
элeменты имeют целый тип. Дано целое число H. Опрeделите, какие столбцы имeют хотя бы
однo такое число, а какие не имeют.
"""
import array as ar
import numpy as np
from random import randint
def main():
    try:
        n = int(input("Введите кол-во строк в матрице -> "))
        m = int(input("Введите кол-во столбцов в матрице -> "))
    except ValueError:
        print("Некорректный ввод данных!")
        return
    
    #Генерация данных
    matrix = np.matrix([[randint(-10,10) for x in range(m)] for y in range(n)])
    print("Сгенерированная матрица:\n", matrix)
    
    boolean_flag = True
    while boolean_flag:
        try:
            h = int(input("Введите число H для его поиска по столбцам -> "))
            boolean_flag = False
        except Exception:
            print("Некорректный ввод данных!")
    
    for col in matrix.T:
        if h in col:
            print("Элемент {} найден в столбце {}".format(h, col))

if __name__ == "__main__":
    main()