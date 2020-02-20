#isinstance() - проверка на то, относится ли класс к базовому классу или к его наследникам
#issubclass() - можно проверить, является ля один класс потомком другого
#assert @property


def will_do_something():
    ...

class Animal():
    def __init__(self):
        pass

class Koshkas(Animal):
    def __init__(self):
        pass

class Human():
    def __init__(self):
        pass

#TODO очень удобная штука
class Ship:
    next_index = 0

    @classmethod
    def generate_next_index(cls):
        index = cls.next_index
        cls.next_index += 1
        return index

    def __init__(self):
        self.index = Ship.generate_next_index()
    
    @staticmethod
    def is_from_same_epoch(sh1, sh2):
        return abs(sh1.index - sh2.index) < 10


if __name__ == "__main__":

    animal_obj = Animal()
    koshkas_obj = Koshkas()
    print(isinstance(animal_obj, Animal))
    print(isinstance(koshkas_obj, Animal))
    print(isinstance(koshkas_obj, Human))

    #
    s1 = Ship()
    print(s1.index)

    fleet = [Ship() for _ in range(15)]
    for sh in fleet:
        print(sh.index)

    Ship.next_index = 1000

    s = [e.next_index for e in fleet]
    print(s)
    print("Без объекта вызов: ", Ship.next_index)
    print(will_do_something())
    
