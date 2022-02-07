"""
Деменчук Георгий, ПИ19-4
Задания 1-12
"""

import random
from itertools import permutations


class Task1(object):
    """
    Нaпишите программу, на вход которой подаётся список чисел одной строкой.
    Программа должна для каждого элемента этого списка вывести сумму двух его cоседей.
    Для элeментов списка, являющиxся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
    Например, если на вход подаётся cписок «1 3 5 6 10», то на выход ожидается cписок «13 6 9 15 7».
    Если на вход пришло только однo число, надо вывести его же.
    Вывoд должен содержать одну строку с чиcлами новoго списка, разделёнными пробeлом.
    """

    def __init__(self):
        out_text = "Введите список чисел через запятую -> "
        self.input_l = [int(x) for x in input(out_text).split(",")]
        self.processing()
        print(self.result)

    def processing(self):
        out_l = []
        l = self.input_l
        if len(l) == 1:
            self.result = l[0]
        else:

            # В начало добавляем сумму последнего и первого элемента
            out_l.append(l[-1] + l[1])
            print(l[0], "пары: ", l[-1], l[1])
            for i in range(1, len(l) - 1):
                print(l[i], "пары: ", l[i - 1], l[i + 1])
                out_l.append(l[i - 1] + l[i + 1])

            # В конец добавляем сумму предпоследнего и нулевого элемента
            out_l.append(l[-2] + l[0])
            print(l[-1], "пары: ", l[-2], l[0])

            self.result = out_l


class Task2(object):
    """
    Нaпишите прогрaмму, котoрая принимает на вход спиcок чисел в одной cтроке и выводит на экран в
    oдну строкy значения, котoрые повторяются в нём бoлее одного раза.
    Выводимые числа не дoлжны повторяться, пoрядок их вывода может быть произвольным.
    Нaпример: 4 8 0 3 4 2 0 3
    """

    def __init__(self):
        out_text = "Введите список чисел через запятую -> "
        self.input_l = [int(x) for x in input(out_text).split(",")]
        self.processing()
        print(self.result)

    def processing(self):
        d = {}
        result = []
        l = self.input_l

        for e in l:
            d[e] = 0

        for e in l:
            d[e] += 1

        for k, v in d.items():
            if v > 1:
                result.append(k)

        self.result = "Повторяющиеся значения:\n" + "".join(
            str(x) + " " for x in result
        )


class Task3(object):
    """
    Выполните oбработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов.
    Все элeменты имeют целый тип. Дано целое число H.
    Опрeделите, какие столбцы имeют хотя бы однo такое число, а какие не имeют.
    """

    def __init__(self):
        try:
            self.n = int(input("Введите количество строк N в матрице -> "))
            self.m = int(input("Введите количество столбцов M в матрице -> "))
        except:
            print("Ошибка ввода данных")
            return

        self.matrix_gen()
        self.element_search()

    def matrix_gen(self):
        m = [[random.randint(10, 99) for c in range(self.m)] for r in range(self.n)]
        print("Исходная матрица:")
        for e in m:
            print(e)
        self.matrix = m

    def element_search(self):
        d = {}
        try:
            number = int(input("Введите число H для поиска по столбцам -> "))
        except:
            print("Ошибка ввода данных")
            return

        for i in range(len(self.matrix[0])):
            d[i] = 0

        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == number:
                    d[i] += 1

        for k, v in d.items():
            if v == 0:
                print("Столбец №" + str(k + 1) + " - значений нет")
            else:
                print(
                    "Столбец №"
                    + str(k + 1)
                    + " - повторение значения "
                    + str(v)
                    + " раз(а)"
                )


class Task4(object):
    """
    Список задается пользователем с клавиатуры. Определите, является ли список симметричным .
    """

    def __init__(self):
        try:
            self.n = int(input("Введите размерность матрицы -> "))
        except:
            print("Ошибка ввода данных")
            return
        self.matrix_input()
        self.symmetry_detect()

    def check_digit(self, e):
        try:
            return int(e)
        except:
            return e

    # TODO СДЕЛАТЬ В ОДНУ СТРОЧКУ
    def matrix_input(self):
        l = []
        for i in range(self.n):
            l.append([])
            for j in range(self.n):
                l[i].append(
                    self.check_digit(
                        input("Введите элемент [" + str(i) + "][" + str(j) + "] ->")
                    )
                )

        print("\nИсходная матрица:")
        for e in l:
            print(e)
        self.out_l = l

    def symmetry_detect(self):

        d = {
            True: "Список является симметричным",
            False: "Список НЕ является симметричным",
        }

        l = self.out_l
        flag = True
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i][j] != l[j][i]:
                    flag = False
        print(d[flag])


class Task5(object):
    """
    Список задается пользователем с клавиатуры.
    Определите, можно ли удалить из списка каких-нибудь два элемента так,
    чтобы новый список оказался упорядоченным
    """

    def __init__(self):
        self.l = list(
            set(
                [
                    self.check_digit(e)
                    for e in input("Введите элементы списка через запятую -> ").split(
                        ","
                    )
                ]
            )
        )
        self.processing()

    def check_digit(self, e):
        try:
            return int(e)
        except:
            return e

    def processing(self):
        this_list = self.l
        perm = permutations(this_list, 2)
        for e in list(perm):
            print(e)
            buf_list = this_list[:]
            buf_list.remove(e[0])
            buf_list.remove(e[1])
            buf_list1 = buf_list[:]
            buf_list1.sort()

            if buf_list1 == buf_list:
                print("Удалили элементы", e[0], "и", e[1], "\nПолучили:", buf_list)
                break


class Task6(object):
    """
    Список задается пользователем с клавиатуры.
    Определите, сколько различных значений содержится в списке.
    """

    def __init__(self):
        self.processing()

    def check_digit(self, e):
        try:
            return int(e)
        except:
            return e

    def processing(self):
        s = "Введите элементы списка через запятую ->"
        r = len(set([self.check_digit(e) for e in input(s).split(",")]))
        print("Уникальных значений в списке:", r)


class Task7(object):
    """
    Список задается пользователем с клавиатуры.
    Удаление из списка элементов, значения которых уже встречались в предыдущих элементах
    """

    def __init__(self):
        self.processing()

    def check_digit(self, e):
        try:
            return int(e)
        except:
            return e

    def processing(self):
        s = "Введите элементы списка через запятую ->"
        r = list(set([self.check_digit(e) for e in input(s).split(",")]))
        print("Список без повторных значений: ", r)


class Task8(object):
    """
    Пользователь вводит упорядоченный список книг (заданной длины по алфавиту).
    Добавить новую книгу, сохранив
    упорядоченность списка по алфавиту
    """

    def __init__(self):
        self.add_values()
        self.add_new_value()

    def add_values(self):
        books_list = input("Введите книги через запятую -> ").split(",")
        for i in range(len(books_list)):
            if books_list[i][0] == " ":
                books_list[i] = books_list[i][1:]
        self.books_list = sorted(books_list, key=str.lower)
        print("Введенный list:\n" + str(self.books_list))

    def add_new_value(self):
        self.new_book = input(
            "Введите название книги для добавления в существующий список ->"
        )
        self.add_book_to_list()

    def add_book_to_list(self):
        buf_list = [e.lower() for e in self.books_list]
        input_element = self.new_book.lower()

        for i in range(len(buf_list)):
            if buf_list[i] > input_element:
                index = i
                break

        print("Индекс для вставки:", index)
        out_list = self.books_list[:index] + [self.new_book] + self.books_list[index:]
        print("Результирующий list:\n" + str(out_list))

        # Driver function
        # list = [1, 2, 4]
        # n = 3

        # print(insert(list, n))


class Task9(object):
    """
    Дан список целых чисел. Упорядочьте по возрастанию только:
    а) положительные числа;
    б) элементы с четными порядковыми номерами в списке.
    """

    def __init__(self):

        try:
            n = int(input("Введите размерность списка ->"))
        except:
            print("Что-то пошло не так при вводе данных")
            return

        self.l = [random.randint(-10, 10) for _ in range(n)]
        print("Исходная матрица:\n", self.l)
        self.a_processing()
        self.b_processing()
        print("Упорядочьте по возрастанию только положительные числа:\n", self.a_l)
        print(
            "Упорядочьте по возрастанию только элементы с четными порядковыми номерами в списке:\n",
            self.b_l,
        )

    def a_processing(self):
        buf_list = []
        matrix = self.l
        for i in range(len(matrix)):
            if matrix[i] > 0:
                buf_list.append(matrix[i])
        buf_list.sort()

        index = 0
        for i in range(len(matrix)):
            if matrix[i] > 0:
                matrix[i] = buf_list[index]
                index += 1
        self.a_l = matrix

    def b_processing(self):
        buf_list = []
        matrix = self.l
        for i in range(len(matrix)):
            if i % 2 == 0:
                buf_list.append(matrix[i])
        buf_list.sort()

        index = 0
        for i in range(len(matrix)):
            if i % 2 == 0:
                matrix[i] = buf_list[index]
                index += 1
        self.b_l = matrix


class Task10(object):
    """
    Даны два списка. Определите, совпадают ли множества их элементов.
    """

    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.input_data()
        self.comparator()

    def input_data(self):

        try:
            n1 = int(input("Введите размерность списка №1 ->"))
            n2 = int(input("Введите размерность списка №2 ->"))
        except:
            print("Что-то пошло не так при вводе данных")
            return

        print("*Заполение списка №1*")
        for i in range(n1):
            self.l1.append(input("Введите элемент списка №" + str(i) + " -> "))

        print("*Заполение списка №2*")
        for i in range(n2):
            self.l2.append(input("Введите элемент списка №" + str(i) + " -> "))

    def comparator(self):

        d = {
            True: "Множества списокв совпадают",
            False: "Множества списков НЕ совпадают",
        }

        print(d[set(self.l1) == set(self.l2)])


class Task11(object):
    """
    Дан список. После каждого элемента добавьте предшествующую ему часть списка.
    """

    def __init__(self):
        self.l = input("Введите элементы списка через запятую -> ").split(",")
        self.processing()
        print(self.result)

    def processing(self):
        s = self.l
        counter = -1
        output_list = [s[0]]
        for element_first in s:
            counter += 1
            if counter == 0:
                pass
            else:
                output_list.append(element_first)
                for element_alter in output_list[:counter]:
                    output_list.append(element_alter)
                    counter += 1
        self.result = output_list


class Task12(object):
    """
    Пусть элементы списка хранят символы предложения. Замените каждое вхождение слова 'itma
    threpetitor' на 'silence'.
    """

    def __init__(self):
        self.list = list(
            input("Введите строку для замены 'itmathrepetitor' на 'silence' -> ")
        )
        self.sub_list = list("itmathrepetitor")
        self.replace_list = list("silence")
        self.processing()

    def get_sublist_index(self):

        sub = self.sub_list
        lst = self.list
        sublen = len(sub)
        first = sub[0] if sub else []
        indx = -1

        while True:
            try:
                indx = lst.index(first, indx + 1)
            except ValueError:
                break
            if sub == lst[indx : indx + sublen]:
                return True, indx, indx + len(sub)
        return False, 0, 0

    def processing(self):

        print("Список до замены:\n" + str(self.list))
        processing_flag = True

        while processing_flag == True:
            index_tuple = self.get_sublist_index()
            if index_tuple[0] == True:
                print("Замена подсписка по индексам", index_tuple[1], index_tuple[2])
                del self.list[index_tuple[1] : index_tuple[2]]
                self.list[index_tuple[1] : index_tuple[1]] = self.replace_list
            else:
                processing_flag = False

        print("Список после замены:\n" + str(self.list))


def main():
    d = {
        "1": Task1,
        "2": Task2,
        "3": Task3,
        "4": Task4,
        "5": Task5,
        "6": Task6,
        "7": Task7,
        "8": Task8,
        "9": Task9,
        "10": Task10,
        "11": Task11,
        "12": Task12,
    }

    input_str = input("Введите номер задания ->")
    if input_str in d:
        d[input_str]()
    else:
        print("Такого номера нет!")


if __name__ == "__main__":
    main()
