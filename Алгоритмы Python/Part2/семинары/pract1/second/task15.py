"""
Задача 15. Создайте класс ПРОГРЕССИЯ с методами вычисления N-го элемента прогрессии,
ее суммы и методом, выводящим сумму на экран.
Создайте дочерние классы: АРИФМЕТИЧЕСКАЯ, ГЕОМЕТРИЧЕСКАЯ со своими методами вычисления.
Создайте список п прогрессий и выведите сумму каждой из них экран.
"""

class ProgressionClass:
    def __init__(self, a1, a2, n):
        self.a1 = a1
        self.a2 = a2
        self.n = n        
    
    def calculate(self):
        ...

    def info(self):
        ...

class ArithmeticClass(ProgressionClass):
    def __init__(self, a1, a2, n):
        super().__init__(a1, a2, n)
        self.calculate()

    def calculate(self):
        self.s = (self.a1 + self.a2)*self.n/2

    def info(self):
        return "[Арифметическая прогрессия]\n1-й элемент: "+str(self.a1)+"\n2-й элемент: "+str(self.a2)+"\nШаг: "+str(self.n)+"Сумма:"+str(self.s)

class GeometricClass(ProgressionClass):
    def __init__(self, b1, q):
        self.b1 = b1
        self.q = q
        self.geometric()

    def calculate(self):
        self.S = self.b1 / (1 - self.q)
        return self.S

    def info(self):
        return "[Геометрическая прогрессия]\n1-й элемент: "+str(self.a1)+"\n2-й элемент: "+str(self.a2)+"\nШаг: "+str(self.n)+"Сумма:"+str(self.s)


Arithmetic(6, 25.5, 40).info()
Geometric(27, 1/3).info()

def main():
    pass
if __name__ == "__main__":
    main()