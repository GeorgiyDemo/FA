"""
Задача 21:
Сгенерировать 2000 случайных целых чисел в диапазоне от -5 до 4, записать их в ячейки
массива. Посчитать сколько среди них положительных, отрицательных и нулевых значений.
Вывести на экран элементы массива и посчитанные количества. Рассмотрите возможность
использования numpy.set_printoptions для полноценного вывода занчений массива на экран.
"""
import array as ar
from random import randint
neg = pos = zero = 0
a = ar.array("i", [])
for i in range(2000):
    numb = int(randint(-5, 4))
    a.append(numb)
    print(numb, end=' ')
    if numb < 0:
        neg += 1
    elif numb > 0:
        pos += 1
    else:
        zero += 1
 
print("\nПоложительных: ", pos)
print("Отрицательных: ", neg)
print("Равных нулю: ", zero)