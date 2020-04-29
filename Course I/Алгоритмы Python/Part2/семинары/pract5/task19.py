"""
Задача 19:
Заполнить вводом с клавиатуры численный массив за исключением последнего элемента,
вывести его на экран. Запросить еще одно значение и его позицию в в массиве. Вставить
указанное число в заданную позицию, подвинув элементы после него.
"""
import array as ar
from random import randint

a = ar.array("i", [])
N = 5
for i in range(N):
    numb = int(input())
    a.append(numb)
print(a)
numb = int(input("Число: "))
pos = int(input("Позиция: "))
 
a.insert(pos-1, numb)
 
print(a)