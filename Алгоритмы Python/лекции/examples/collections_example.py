class CollectionsExample(object):
    def __init__(self):
        self.tuple_method()
        self.list_method()
    
    def tuple_method(self):
        """
        Tuple/Кортеж
        Обозначается круглыми скобками ()
        
        - Неизменяемый аналог списка
        - Можно обращаться по индексу
        """
        
        example = (1,1,1,1,1)

        #Можно сделать tuple из tuple
        example = (example,example,example,example,example,example)
        self.meow = example
        print("Tuple из tuple:",example)
        #Обращение к элементам
        print("Элемент tuple 0,1:")
        print(example[0][1])

        example = (1,True)
        print(example)
        
    def list_method(self):
        """
        List/Список

        Обозначается квадратными скобками []
        
        - Изменяемый аналог tuple
        - Можно обращаться по индексу
        """
        
        Meow = {}
        for meow in [meow for meow in (3,1,2,0)]:
            for meoW in self.meow[meow]:
                Meow["["+str(meow)+"]["+str(meoW)+"]"] = self.meow[meow][meoW]
        print(Meow)

    def dict_method(self):
        """
        Dictionary/Словарь

        Обозначается вот такими скобками -> {}
        
        - Ассоциация ключ/значение т.е. аналог hashtable
        - Нельзя обращаться по индексу, только по ключу
        """
        pass

def main():
    CollectionsExample()
    
if __name__ == "__main__":
    main()