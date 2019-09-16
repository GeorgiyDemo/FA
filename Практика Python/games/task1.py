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


class MainClass():
    def __init__(self):
        self.matrix_generation()
        #TODO До того, пока нет 3 фишек подряд, пока while True
        while True:
            self.enter_number()

    def matrix_generation(self):
        out_list = [[0 for c in range(10)] for r in range(10)]
        self.matrix = out_list
        self.show_matrix()

    def check_finish_game(self):
        pass
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
        self.check_finish_game()

    def show_matrix(self):
        print("Игровое поле:")
        for i in range(len(self.matrix)):
            print(self.matrix[i])

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