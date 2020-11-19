
class Generator:
    """Генерация поля"""
    def __init__(self,n,m):
        matrix = []
        for i in range(n):
            matrix[i].append([])
            for j in range(m):
                matrix[i][j].append(0)
        print(matrix)
                
        

class Field:
    """Класс поля"""
    
    def __init__(self, x, y,isbomb=False, value=0) -> None:
        self.x = x
        self.y = y
        self.isbomb = isbomb
        self.value = value

    def click():
        """Нажатие на поле"""
        pass


def main():
    gen = Generator(10, 10)


if __name__ == "__main__":
    main()