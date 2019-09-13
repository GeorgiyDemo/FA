import math
import matplotlib.pyplot as plt

class GraphClass():

    def __init__(self):
        self.graph()

    def graph(self):

        x = 0.2
        end_cycle = 0.8

        fig = plt.figure()
        while x != end_cycle:

            obj = MathUpper(x)
            plt.scatter(x,obj.result)
            x = round(x + 0.1, 2)
        
        print(fig.axes)
        plt.show()

class MathUpper():
    def __init__(self, x):
        self.x = x
        self.getter()
    
    def getter(self):

        x = self.x
        upper = x**3*math.e**(x-1)
        lower = x**3-math.fabs(x)
        if lower == 0:
            print("Знаменатель равен нулю, деление на 0!")
            self.result = 0
            return

        first = upper/lower
        
        log_sqrt = math.sqrt(x)-x
        
        if log_sqrt >= 0:
            buf_log = math.log(log_sqrt,2)
        else:
            print("Выражение в log[sqrt(x)-x,2] меньше 0!")
            self.result = 0
            return

        self.result = first-buf_log

class CycleClass():
    def __init__(self):
        self.cycle()
    
    def cycle(self):
        x = 0.2
        end_cycle = 0.8

        while x != end_cycle:
            obj = MathUpper(x)
        
            print("x=",x, "result = ",obj.result)
            x = round(x + 0.1, 2)

    pass

def main():

    try:
        x = float(input("Введите x: "))
    except:
        print("Проблема ввода данных!")
        return

    obj = MathUpper(x)
    print("\n*Условные операторы*")
    print("Результат:"+str(obj.result))
    
    print("\n*Операторы цикла*")
    CycleClass()

    GraphClass()

if __name__ == "__main__":
    main()

#операторы цикла - шаг n вводим с клавиатуры