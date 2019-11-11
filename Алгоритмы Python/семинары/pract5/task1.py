"""
Реализовать решение квадратного уравнения через дискриминант
"""
import math

class DescrSolver():

    def __init__(self, input_str):
        self.input_str = input_str
        self.parse_exp()
        self.get_descriminant()

    def is_digital(self, number):
        try:
            float(number)
            return True
        except:
            return False
        
    def parse_exp(self):
        input_str = self.input_str
        
        #Определяем коэффициент a
        symbols = 1
        return_flag = False
        while return_flag == False:
            
            index_a = input_str[:symbols]
            if self.is_digital(index_a) == False:
                return_flag = True

            symbols += 1

        index_a = input_str[:symbols-2]

        #Определяем коэффициент b
        symbols = input_str.rindex("x")
        buf_index_b = input_str[:symbols]
        symbols = 1
        return_flag = False
        while return_flag == False:

            index_b = buf_index_b[symbols:]            

            if self.is_digital(index_b) == True:
                return_flag = True
            
            symbols += 1

        #Определяем коэффициент c
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

        print("Коэффициент a =",index_a)
        print("Коэффициент b =",index_b)
        print("Коэффициент c =",index_c)

    def get_descriminant(self):
        a = self.index_a
        b = self.index_b
        c = self.index_c

        D = b ** 2 - 4 * a * c
        print("D =",D)

        if D == 0:
            A1 = -b/(2*a)
            A2 = A1
            print("\nОтвет: ")
            print("Корень А1 =",A1)
            print("Корень A2 =",A2)

        elif D > 0:
            A1 = (-b + math.sqrt(D)) / (2 * a)
            A2 = (-b - math.sqrt(D)) / (2 * a)
            print("\nОтвет: ")
            print("Корень А1 =",A1)
            print("Корень A2 =",A2)
        
        else:
            print("Нет решения, D < 0")

if __name__ == "__main__":

    input_str = input("Введите квадратное выражение вида ax^2+bx+c=0 -> ")
    DescrSolver(input_str)