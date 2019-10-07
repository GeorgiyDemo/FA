import random
import collections

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

        self.result = "Повторяющиеся значения:\n" + "".join(str(x) + " " for x in result)
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
        m = [[random.randint(10,99) for c in range(self.m)] for r in range(self.n)]
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
                print("Столбец №"+str(k+1)+" - значений нет")
            else:
                print("Столбец №"+str(k+1)+" - повторение значения "+str(v)+" раз(а)")
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
    
    #TODO СДЕЛАТЬ В ОДНУ СТРОЧКУ
    def matrix_input(self):
        l = []
        for i in range(self.n):
            l.append([])
            for j in range(self.n):
                l[i].append(self.check_digit(input("Введите элемент ["+str(i)+"]["+str(j)+"] ->")))
        
        print("\nИсходная матрица:")
        for e in l:
            print(e)
        self.out_l = l


    def symmetry_detect(self):
        
        d = {
            True : "Список является симметричным",
            False : "Список НЕ является симметричным"
        }

        l = self.out_l
        flag = True
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i][j] != l[j][i]:
                    flag = False
        print(d[flag])
#TODO
class Task5(object):
    """
    Список задается пользователем с клавиатуры.
    Определите, можно ли удалить из списка каких-нибудь два элемента так, 
    чтобы новый список оказался упорядоченным
    """
    def __init__(self):
        pass
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
        print("Введенный list:\n"+str(self.books_list))
        
    def add_new_value(self):
        self.new_book = input("Введите название книги для добавления в существующий список ->")
        self.add_book_to_list()
    
    def add_book_to_list(self):
        buf_list = [e.lower() for e in self.books_list]
        input_element = self.new_book.lower()

        for i in range(len(buf_list)): 
            if buf_list[i] > input_element: 
                index = i 
                break
        
        print("Индекс для вставки:",index)
        out_list = self.books_list[:index] + [self.new_book] + self.books_list[index:] 
        print("Результирующий list:\n"+str(out_list))
    
        # Driver function 
        #list = [1, 2, 4] 
        #n = 3
        
        #print(insert(list, n)) 
#TODO Task9
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

        self.l = [random.randint(-10,10) for _ in range(n)]
        print(self.l)
        self.l.sort(key=lambda kot: (kot>0, kot))
        print(self.l)
        #self.l = [random.randint(10,99) for r in range(self.n)]

class Task10(object):
    """
    Даны два списка. Определите, совпадают ли множества их элементов.  
    """
    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.input_data()
    
    def input_data(self):

        try:
            n1 = int(input("Введите размерность списка №1 ->"))
            n2 = int(input("Введите размерность списка №2 ->"))
        except:
            print("Что-то пошло не так при вводе данных")
            return
        
        print("*Заполение списка №1*")
        for i in range(n1):
            self.l1.append(input("Введите элемент списка №"+str(i)+" -> "))
        
        print("*Заполение списка №2")
        for i in range(n2):
            self.l2.append(input("Введите элемент списка №"+str(i)+" -> "))
    
    def comparator(self):
        
        d = {
            True : "Множества списокв совпадают",
            False : "Множества списков НЕ совпадают",
        }

        print(d[collections.Counter(self.l1) == collections.Counter(self.l2)])
 

def main():
    #Task1()
    #Task2()
    #Task3()
    #Task4()
    #TODO TASK 5
    #Task5()
    #Task6()
    #Task7()
    #Task8()
    #TODO TASK 9
    #Task9()
    Task10()


if __name__ == "__main__":
    main()
