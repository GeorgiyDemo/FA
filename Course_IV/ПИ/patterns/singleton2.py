"""
    Альтернатива классическому Singleton. GOF определяют Singleton как класс позволяющий создать
    один и только один свой экземпляр, паттерн Monostate предполагает создание множества экземпляров
    с синхронизированным состоянием. С прикладной точки зрения это одно и то же - обращение к любому
    из экземпляров дает один результат
"""


class Monostate:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


b = Monostate()
b1 = Monostate()
b.x = 4

print("Monostate Object 'b': ", b)  # b и b1 это разные объекты
print("Monostate Object 'b1': ", b1)
print("Object State 'b':", b.__dict__)  # но b и b1 имеют общее состояние
print("Object State 'b1':", b1.__dict__)
