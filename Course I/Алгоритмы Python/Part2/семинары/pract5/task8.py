"""
Задача 8:
Пользователь вводит упорядоченный список/массив книг (заданной длины по алфавиту).
Добавить новую книгу, сохранив упорядоченность списка по алфавиту
"""
import numpy as np
from faker import Faker


class BookClass:
    def __init__(self):
        d_ways = {"1": self.auto_generator, "2": self.manual_generator}
        boolean_flag = True

        while boolean_flag:
            input_way = input("Как вы хотите создать список книг?\n1. Автоматическая генерация\n2. Ручной ввод\n-> ")
            if input_way in d_ways:
                d_ways[input_way]()
                boolean_flag = False
            else:
                print("Некорректный ввод данных, попробуйте снова")

        self.arr = np.sort(self.arr)
        self.display()

    def auto_generator(self):
        """Генерация книг"""

        fake = Faker("ru_RU")

        boolean_flag = True
        while boolean_flag:
            try:
                n = int(input("Введите кол-во книг для генерации -> "))
                boolean_flag = False
            except ValueError:
                print("Некорректный ввод данных")

        self.arr = np.array([fake.word() for _ in range(n)])

    def manual_generator(self):
        """Ручной ввод книг"""
        boolean_flag = True
        arr = np.array([])
        while boolean_flag:
            try:
                n = int(input("Введите кол-во книг для ввода -> "))
                boolean_flag = False
            except ValueError:
                print("Некорректный ввод данных")

        for i in range(n):
            book_name = input("Введите название книги №{} -> ".format(i + 1))
            arr = np.append(arr, book_name)
        self.arr = arr

    def add_book(self, book):
        """Метод добавления новой книги"""
        arr = self.arr
        for i in np.arange(arr.shape[0]):
            if arr[i] > book:
                index = i
                break
        print("Индекс для вставки: {}".format(index))
        self.arr = np.insert(arr, index, book)
        self.display()

    def display(self):
        print("Общий массив книг: {}".format(self.arr))


if __name__ == "__main__":
    obj = BookClass()
    newbook_name = input("Введите название книги, которое хотите добавить -> ")
    obj.add_book(newbook_name)
