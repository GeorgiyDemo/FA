from random import randrange


class Task3Class:
    def __init__(self):
        try:
            d = {"1": self.user_input, "2": self.random_input, }
            self.main_list = []
            self.list_len = int(input("Введите длинну последовательности -> "))
            method_number = input("Как вы хотите заполнить последовательность?\n1. Вручную\n2. Автоматически\n-> ")
            if method_number in d:
                d[method_number]()
                self.out_list()
            else:
                print("Некорректный ввод")
        except Exception as e:
            print("Возникла ошибка: ", e)

    def number_checker(self, e):
        try:
            return int(e)
        except ValueError:
            return e

    def user_input(self):
        for i in range(self.list_len):
            locale_element = self.number_checker(input("Введите элемент №" + str(i + 1) + " -> "))
            self.main_list.append(locale_element)

    def random_input(self):
        self.main_list = [randrange(-10, 10) for _ in range(self.list_len)]

    def out_list(self):
        print("Полученная последовательность:")
        print(self.main_list)
