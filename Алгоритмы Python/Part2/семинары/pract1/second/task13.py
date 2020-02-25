"""
Задача 13. Создайте класс
УРАВНЕНИЕ с методами вычисления корня уравнения и вывода результата на экран.

Создайте дочерние классы ЛИНЕЙНОЕ, КВАДРАТНОЕ со своими методами вычисления корней и вывода на экран.
Создайте список n уравнений и выведите полную информацию об уравнениях на экран.
"""

from random import randint
import math

class EquationClass:
    """
    Базовый класс уравнение
    """
    def __init__(self):
        pass

    def calculation(self):
        ...
        
    def info(self):
        ...

class LinearEquation(EquationClass):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c
        #Поскольку я устал и мне надо сделать просто КАКОЕ-ТО ЛИНЕЙНОЕ УРАВНЕНИЕ
        self.calculation()
    
    def calculation(self):
        #Просто представляем, что вся задача сводится к решению ax+b=c
        self.result = (self.c-self.b)/self.a

    def info(self):
        a = self.a
        b = self.b
        c = self.c
        equation_str = str(a)+"x+"+str(b)+"="+str(c)
        return "*Информация о простом линейном уравнении*\nОбщий вид: "+equation_str+"Коэффициент a = "+str(a)+"\nКоэффициент b = "+str(b)+"\nКоэффициент c = "+str(c)+"\nОтвет:\n"+str(self.result)


class QuadraticEquation(EquationClass):
    """
    Квадратное уравнение
    """

    def __init__(self, input_str):
        self.equation_results_list = []

        self.input_str = input_str
        self.parse_exp()
        self.calculation()

    def is_digital(self, number):
        try:
            float(number)
            return True
        except:
            return False

    def parse_exp(self):
        input_str = self.input_str

        # Определяем коэффициент a
        symbols = 1
        return_flag = False
        while return_flag == False:

            index_a = input_str[:symbols]
            if self.is_digital(index_a) == False and symbols != 1:
                return_flag = True

            symbols += 1

        index_a = input_str[:symbols - 2]

        # Определяем коэффициент b
        symbols = input_str.rindex("x")
        buf_index_b = input_str[:symbols]
        symbols = 1
        return_flag = False
        while return_flag == False:

            index_b = buf_index_b[symbols:]

            if self.is_digital(index_b) == True:
                return_flag = True

            symbols += 1

        # Определяем коэффициент c
        symbols = input_str.rindex("=")
        buf_index_c = input_str[:symbols]
        symbols = 1
        return_flag = False
        while return_flag == False:

            index_c = buf_index_c[symbols:]

            if self.is_digital(index_c) == True:
                return_flag = True

            symbols += 1

        self.index_a = float(index_a)
        self.index_b = float(index_b)
        self.index_c = float(index_c)

    def info(self):
        locale_list = self.equation_results_list
        if len(locale_list) == 1:
            result_msg = "".join(locale_list)
        elif len(locale_list) == 2:
            result_msg = "Корень А1 ="+str(locale_list[0])+"\nКорень А2 ="+str(locale_list[1])
        else:
            result_msg = "Ошибка вычисления"
        return "*Информация о квадратном уравнении*\nОбщий вид: "+self.input_str+"\nКоэффициент a = "+str(self.index_a)+"\nКоэффициент b = "+str(self.index_b)+"\nКоэффициент c = "+str(self.index_c)+"\nОтвет:\n"+result_msg
    
    def calculation(self):
        a = self.index_a
        b = self.index_b
        c = self.index_c

        D = b ** 2 - 4 * a * c
        print("D =", D)

        if D == 0:
            A1 = -b / (2 * a)
            A2 = A1
            self.equation_results_list.append(A1)
            self.equation_results_list.append(A2)

        elif D > 0:
            A1 = (-b + math.sqrt(D)) / (2 * a)
            A2 = (-b - math.sqrt(D)) / (2 * a)
            self.equation_results_list.append(A1)
            self.equation_results_list.append(A2)

        else:
            self.equation_results_list.append("Нет решения, D < 0")

def main():

    #Создайте список n уравнений и выведите полную информацию об уравнениях на экран.
    try:
        n = int(input("Введите количество уравнений -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
        
    d = {
        1 : LinearEquation,
        2 : QuadraticEquation,
    }

    main_list = []

    for _ in range(n):
        
        d_args = {
            1 : [randint(1,1000),randint(1,1000),randint(1,1000)],
            2 : [str(randint(1,1000))+"x^2+"+str(randint(1,1000))+"x+"+str(randint(1,1000))+"=0"],
        }

        r_number = randint(1,2)
        main_list.append(d[r_number](*d_args[r_number]))
    
    for e in main_list:
        print(e.info()+"\n")

if __name__ == "__main__":
    main()