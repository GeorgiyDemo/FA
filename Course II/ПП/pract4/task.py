import random

class Generator:
    """Генерация поля"""
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(self.n):
            print("purr1")
            buf_matrix = []
            for j in range(self.m):
                print("purr2")
                buf_matrix.append(Cell(i, j))
            self.matrix.append(buf_matrix)

    def Filling(self):
        print("PURRRR")
        i = 0
        while i <= (self.n + self.m): #Рандомная пропорция на количество бомб на поле
            a = random.randint(0, self.n-1)
            b = random.randint(0, self.m-1)
            if not self.matrix[a][b].isbomb:
                self.matrix[a][b].isbomb = True
                i += 1 #счетчик без for, не бей меня :D
        for i in range(self.n): #Проставляем числа
            for j in range(self.m):
                if not self.matrix[i][j].isbomb: #Считаем бомбы
                    count = 0
                    for a in range(3):
                        for b in range(3):
                            if (0<=(i-1+a)<self.n) and (0<=(j-1+b)<self.m) and (self.matrix[i-1+a][j-1+b].isbomb): count+=1 #Если клетка внутри поля и это бомба, то считаем
                    self.matrix[i][j].value = count
        return self.matrix

                
        
class Cell:
    """Класс клетка, потому что поле это все целиком"""
    
    def __init__(self, x, y, isbomb=False, value=0) -> None:
        self.x = x
        self.y = y
        self.isbomb = isbomb
        self.value = value

    def click(self):
        """Нажатие на клетку"""
        pass


class Field:
    """Класс всего поля"""

    def __init__(self, matrix):
        self.matrix = matrix
    
    def PrintMatrix(self): #Если ты не понял, то это принт
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j].isbomb:
                    print("Б", end=' ')
                else:
                    print(self.matrix[i][j].value, end=' ')
            print('')


def main():
    print("meow")
    Field1 = Field(Generator(10, 10).Filling())
    print("meow2")
    Field1.PrintMatrix()

if __name__ == "__main__":
    main()