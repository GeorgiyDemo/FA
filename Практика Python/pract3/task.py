"""
Базовая часть (выполняется всеми самостоятельно!):
Написать калькулятор для строковых выражений вида 
'<число> <операция> <число>', 
где <число> - не отрицательное целое число меньшее 100, 
записанное словами, например "тридцать четыре", <арифметическая операция> -
 одна из операций "плюс", "минус", "умножить". 
 
 Результат выполнения операции вернуть в виде текстового представления числа.
  Пример calc("двадцать пять плюс тринадцать") -> "тридцать восемь"
Оформить калькулятор в виде функции, которая принимает на вход строку и возвращает строку.

6)	Добавить возможность оперировать с дробями (правильными и смешанными). Реализовать поддержку сложения, вычитания и умножения, дробей. Результат операций не должен представлять неправильную дробь, такие результаты нужно превращать в смешанные дроби. Пример: calc("один и четыре пятых плюс шесть седьмых ") -> "два и двадцать три тридцать пятых". 
"""


class String2NumClass():
    def __init__(self, number_string):
        self.arr_1 = [['ноль'], ['один', 'одна'], ['два', 'две'], ['три'], ['четыре'], ['пять'], ['шесть'], ['семь'],
                      ['восемь'], ['девять']]
        self.arr_2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                      "семнадцать", "восемнадцать", "девятнадцать"]
        self.arr_3_4 = [
            ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
             "девяносто"],
            ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]]
        self.arr_5 = ["тысяч", "миллион", "миллиард", "триллион", "квадриллион", "квинтиллион", "секстилион",
                      "септилион", "окталион"]
        self.number_string = number_string
        self.processing()

    def processing(self):
        """
        Преобразование строки числительного к числу
        """
        number_string = self.number_string

        if type(number_string) != str or number_string == "":
            self.result = None

        check_words = number_string.lower().split()

        result = 0
        result_temp = 0
        for word in check_words:
            found = False
            for i, test_number in enumerate(self.arr_1):
                for test_number_variant in test_number:
                    if test_number_variant == word:
                        result_temp += i
                        found = True
                        break

                if found:
                    break

            if found:
                continue

            for i, test_number in enumerate(self.arr_2):
                if word == test_number:
                    result_temp = result_temp + (i + 1) + 10
                    found = True
                    break

            if found:
                continue

            for i, temp_arr in enumerate(self.arr_3_4):
                for j, test_number in enumerate(temp_arr):
                    if word == test_number:
                        result_temp = result_temp + (j + 1) * (10 ** (i + 1))
                        found = True
                        break

                if found:
                    break

            if found:
                continue

            for i, test_multiplier in enumerate(self.arr_5):
                if word == test_multiplier or word == "{}{}".format(test_multiplier, 'а') \
                        or word == "{}{}".format(test_multiplier, 'ов') or word == "{}{}".format(test_multiplier, 'и'):
                    result += result_temp * (1000 ** (i + 1))
                    result_temp = 0
                    found = True
                    break

            if found:
                continue

            self.result = None

        self.result = (result + result_temp)


class MainClass():
    def __init__(self, input_str):

        self.input_str = input_str
        self.operations_list = {"плюс": "+", "минус": "-", "умножить": "*"}
        self.r_operations_list = {"+": "плюс", "-": "минус", "*": "умножить"}
        self.splitter()
        self.number_collector()
        self.processing()

    def processing(self):
        """
        Финальный процессинг через eval всего выражения + вывод
        """
        n = self.collectored_numbers
        result = str(eval(n[0] + self.operation + n[1]))
        operation = self.r_operations_list[self.operation]
        print("Число №1: " + n[0] + "\nЧисло №2: " + n[1])
        print("Операция: " + operation + "\nРезультат: " + result)

    def number_collector(self):
        """
        Метод для 'собирания' сложного числа из его подкомпонентов
        Пример: двадцать четыре -> двадцать (20) + четыре (4)
        """

        input_str = self.input_str

        collectored_numbers = []
        for numbers in input_str:
            locale_number = 0
            buf_number_list = numbers.split(" ")
            for number in buf_number_list:
                o = String2NumClass(number)
                locale_number += o.result
            collectored_numbers.append(str(locale_number))
        self.collectored_numbers = collectored_numbers

    def splitter(self):
        """
        Метод для разделения строки на знак операции
        """
        operations_list = self.operations_list
        input_str = self.input_str

        for s_str in operations_list:
            if s_str in input_str:
                self.operation = operations_list[s_str]
                self.input_str = input_str.split(s_str)


if __name__ == "__main__":
    input_str = input("Введите строку -> ")
    MainClass(input_str)
