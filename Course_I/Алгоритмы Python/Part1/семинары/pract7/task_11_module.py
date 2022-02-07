class Task11_1:
    """
    Список задается пользователем с клавиатуры.
    Удаление из списка элементов, значения которых уже встречались в предыдущих элементах
    """

    def __init__(self, DEMKA_class):
        self.DEMKA_class = DEMKA_class
        self.processing()

    def check_digit(self, e):
        try:
            return int(e)
        except:
            return e

    def processing(self):
        s = "Введите элементы списка через запятую ->"
        DEMKAlist = self.DEMKA_class([self.check_digit(e) for e in input(s).split(",")])
        r = self.DEMKA_class(set(DEMKAlist))
        print(type(r))
        print("Список без повторных значений: ", r)


class Task11_2:
    """
    Дан список. После каждого элемента добавьте предшествующую ему часть списка.
    """

    def __init__(self, DEMKA_class):
        self.l = DEMKA_class(
            input("Введите элементы списка через запятую -> ").split(",")
        )
        self.processing()
        print(self.result)

    def processing(self):
        s = self.l
        counter = -1
        output_list = [s[0]]
        for element_first in s:
            counter += 1
            if counter == 0:
                pass
            else:
                output_list.append(element_first)
                for element_alter in output_list[:counter]:
                    output_list.append(element_alter)
                    counter += 1
        self.result = output_list
