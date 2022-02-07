"""
№1 создайте коллекцию на свободную тему и выполните:
№2 подсчет количества членов коллекции с помощью функции len()
№3 проверку принадлежности элемента данной коллекции c помощью оператора in
№4 выполните поиск подстроки
№5 обход коллекции с применением оператора цикла
№6 найдите максимальный, минимальный̆ элементы коллекции и сумму элементов
№7 Найдите количество определённого пользователем элемента коллекции
№8 выполните конвертацию типа созданной вами коллекции
№9 выполните сортировку элементов коллекции
№10 реализовать любые два практических задания из темы словари с применением коллекции
№11 реализовать два задания из практической работы по спискам и кортежам с применением коллекций
"""

from collections.abc import MutableSequence

import task_10_module
import task_11_module


class DEMKACollection(MutableSequence):
    """
    Кастомная коллекция
    """

    def __init__(self, data=None):

        # Дёргаем конструктор MutableSequence
        super(DEMKACollection, self).__init__()
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, ii):
        return self._list[ii]

    def __delitem__(self, ii):
        del self._list[ii]

    def __setitem__(self, ii, val):
        self._list[ii] = val

    def __str__(self):
        return str(self._list)

    def sort(self):
        return self._list.sort()

    def insert(self, ii, val):
        self._list.insert(ii, val)

    def append(self, val):
        self.insert(len(self._list), val)


class MainClass:
    def __init__(self):
        self.my_collection = DEMKACollection([1, 5, 3, 2, 5])
        self.task_2()
        self.task_3()
        self.task_4_5()
        self.task_6()
        self.task_7()
        self.task_8()
        self.task_9()
        self.task_10()
        self.task_11()

    def task_2(self):
        print("len:", len(self.my_collection))

    def task_3(self):
        for i in range(11):
            flag = True if i in self.my_collection else False
            print(i, flag)

    def task_4_5(self):
        locale_collection = DEMKACollection(list(self.my_collection) + ["abc"])
        print(locale_collection.__getitem__(0))
        for i in range(len(locale_collection)):
            if "ab" in str(locale_collection.__getitem__(i)):
                print(
                    'Подстрока "ab" есть в элементе №'
                    + str(i)
                    + ' с содержимым "'
                    + locale_collection[i]
                    + '"'
                )

    def task_6(self):
        print(self.my_collection)
        c = self.my_collection
        print("Сумма:", sum(c))
        print("Максимальный элемент:", max(c))
        print("Минимальный элемент:", min(c))

    def task_7(self):
        search_element = int(input("Введите элемент для подсчёта кол-ва -> "))
        count = self.my_collection.count(search_element)
        print("Количество элементов", search_element, ":", count)

    def task_8(self):
        print(type(self.my_collection))
        print(type(tuple(self.my_collection)))
        print(type(frozenset(self.my_collection)))

    def task_9(self):
        c = self.my_collection
        print(c)
        c.sort()
        print(c)

    def task_10(self):
        task_10_module.Task10_1()
        task_10_module.Task10_2()

    def task_11(self):
        task_11_module.Task11_1(DEMKACollection)
        task_11_module.Task11_2(DEMKACollection)


if __name__ == "__main__":
    MainClass()
