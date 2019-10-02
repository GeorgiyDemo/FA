"""
Реализовать программу, при помощи которой 2 игрока могут играть в игру «Клондайк». Правила игры следующие. Игра ведётся на игровом поле размером 10 на 10 клеток. Игроки по очереди выставляют в любую свободную клетку по отметке, и тот игрок, после чьего хода получилась цепочка длиной хотя бы в 3 отметке, проигрывает. При этом в цепочке считаются как свои отметки, так и отметки соперника, у игровых фишек как бы нет хозяина. Цепочка - это ряд фишек, следующая фишка в котором примыкает к предыдущей с любого из 8-ми направлений. (описание правил игры:  )
Взаимодействие с программой производится через консоль. Игровое поле изображается в виде 10 текстовых строк и перерисовывается при каждом изменении состояния поля. При запросе данных от пользователя программа сообщает, что ожидает от пользователя (например, координаты очередного хода) и проверяет корректность ввода. Программа должна уметь автоматически определять окончание партии и ее победителя.
Сама программа НЕ ходит, т.е. не пытается ставить в клетки отметки с целью выиграть игру.

"""
def check_input(string):
    try:
        input_list = string.split(",")
        return (True, int(input_list[0]), int(input_list[1]))
    except:
        return (False, 0, 0)

class CheckWinClass(object):
    def __init__(self, matrix, x, y):
        self.matrix = matrix
        self.ignore = []
        self.total = 0
        self.check_finish_game(x,y)

    def check_dots(self, x, y):
        d=[]
        d.append((x-1,y-1))
        d.append((x,y))
        d.append((x-1,y+1))
        d.append((x,y+1))
        d.append((x,y-1))
        d.append((x+1,y))
        d.append((x+1,y+1))
        d.append((x+1,y-1))
        return d

    def contain(self, item, arr):
        for elem in arr:
            if elem[0]==item[0] and elem[1]==item[1]:
                return True
        return False

    def check_finish_game(self,x,y):
        self.ignore+=[(x,y)]
        if self.matrix[x][y] == 1:
            self.total+=1
            for dot in self.check_dots(x,y):
                if self.contain((dot[0],dot[1]),self.ignore):
                    continue
                else:
                    self.check_finish_game(dot[0],dot[1])
        else:
            return

class MainClass(object):
    def __init__(self):
        self.matrix_generation()
        #TODO До того, пока нет 3 фишек подряд, пока while True
        while True:
            self.enter_number()

    def matrix_generation(self):
        out_list = [[0 for c in range(10)] for r in range(10)]
        self.matrix = out_list
        self.show_matrix()

    def check_finish_game(self, x, y):
        obj = CheckWinClass(self.matrix, x,y)
        if obj.total > 2:
            print("Вы проиграли")

        #Цепочка - это ряд фишек, следующая фишка в котором примыкает к предыдущей с любого из 8-ми направлений. (описание правил игры:  )
        # после чьего хода получилась цепочка длиной хотя бы в 3 отметке,
        
    def change_matrix(self, x, y):

        try:

            if self.matrix[x][y] == 0:
                self.matrix[x][y] = 1
                self.show_matrix()
            else:
                print("[!] Нельзя поставить фишку! Она уже там находится")
        
        except IndexError:
            print("[!] Неправильные координаты")
        
        #Проверка на то, закончилась ли игра
        self.check_finish_game(x,y)

    def show_matrix(self):
        print("Игровое поле:\n   0  1  2  3  4  5  6  7  8  9")
        for i in range(len(self.matrix)):
            print(i,self.matrix[i])

    def enter_number(self):
        check_tuple = check_input(input("Введите координаты по x,y для постановки фишки через запятую ->"))
        if check_tuple[0] == False:
            print("[!] Неправильный ввод")
        else:
            self.change_matrix(int(check_tuple[1]), int(check_tuple[2]))

def main():
    MainClass()

if __name__ == "__main__":
    main()