from random import randint
from faker import Faker


class CockroachClass():
    """
    Класс таракан
    """
    def __init__(self, name):
        self.name = name
        self.current_location = 0
        self.__speed_generator()

    def movement_changer(self):
        self.movement = bool(randint(0,1))
        #Если было перемещение
        if self.movement:
            self.current_location += self.speed
    
    def __speed_generator(self):
        #Генерация скорости
        self.speed = randint(1,1) #TODO 


class GamerClass():
    pass


class MainClass():
    
    def __init__(self):
        
        self.COCKROACH_COUNT = 4
        self.ITERATIONS_COUNT = 20
        #Хранит объекты тараканов
        self.cockroach_list = []
        fake = Faker(['ru_RU'])

        #Начальная матрица
        self.start_matrix_generator()
        #Генерируем тараканов
        for i in range(self.COCKROACH_COUNT):
            cockroach_obj = CockroachClass(fake.word())
            self.cockroach_list.append(cockroach_obj)
    
        for current_iteration in range(self.ITERATIONS_COUNT):

            self.drawer()
            input()
            self.cockroach_changer()

    
    def start_matrix_generator(self):
        #Начальная матрица
        self.matrix = [[0 for c in range(self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]
        for i in range(len(self.matrix)):
            self.matrix[i][0] = 1

        
    def cockroach_changer(self):
        self.matrix = [[0 for c in range(self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]
        for i in range(len(self.cockroach_list)):
            
            cockroach = self.cockroach_list[i]
            cockroach.movement_changer()
            print("[Таракан '"+str(cockroach.name)+"'] находится на "+str(cockroach.current_location)+", перемещение: "+str(cockroach.movement))
            self.matrix[i][cockroach.current_location] = 1 #TODO Заменить на значек таракана

            


    def drawer(self):
        """
        Отображение на экран
        """
        print("Забег:\n")
        for i in range(len(self.matrix)):
            print(i, self.matrix[i])

        
if __name__ == "__main__":
    obj = MainClass()