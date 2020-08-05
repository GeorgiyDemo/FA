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

6)	Добавить возможность оперировать с дробями. Реализовать поддержку сложения, вычитания и умножения, дробей. 
Пример: calc("один и четыре пятых плюс шесть седьмых ") -> "два и двадцать три тридцать пятых".
"""

import yaml
from pytils import numeral
from word2number import w2n
from yandex.Translater import Translater


class FileClass:
    """
    Возвращает токен Яндекс Переводчика с yaml
    """

    def __init__(self):
        self.read_file()

    def read_file(self):
        with open("./token.yml", "r") as outfile:
            self.content = yaml.safe_load(outfile)["token"]


class TranslaterClass:
    def __init__(self, token, ru_str):
        self.token = token
        self.ru_str = ru_str
        self.translater()

    def translater(self):
        ru_str = self.ru_str
        tr = Translater()
        tr.set_key(self.token)
        tr.set_from_lang("ru")
        tr.set_to_lang("en")
        tr.set_text(ru_str)
        en_str = tr.translate()
        self.result = en_str
        print("Перевод:", self.result)


class String2NumClass:
    """
    Представление прописи в виде числа
    """

    def __init__(self, number_string):
        self.arr_1 = [
            ["ноль"],
            ["один", "одна"],
            ["два", "две"],
            ["три"],
            ["четыре"],
            ["пять"],
            ["шесть"],
            ["семь"],
            ["восемь"],
            ["девять"],
        ]
        self.arr_2 = [
            "одиннадцать",
            "двенадцать",
            "тринадцать",
            "четырнадцать",
            "пятнадцать",
            "шестнадцать",
            "семнадцать",
            "восемнадцать",
            "девятнадцать",
        ]
        self.arr_3_4 = [
            [
                "десять",
                "двадцать",
                "тридцать",
                "сорок",
                "пятьдесят",
                "шестьдесят",
                "семьдесят",
                "восемьдесят",
                "девяносто",
            ],
            [
                "сто",
                "двести",
                "триста",
                "четыреста",
                "пятьсот",
                "шестьсот",
                "семьсот",
                "восемьсот",
                "девятьсот",
            ],
        ]
        self.arr_5 = [
            "тысяч",
            "миллион",
            "миллиард",
            "триллион",
            "квадриллион",
            "квинтиллион",
            "секстилион",
            "септилион",
            "окталион",
        ]
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
                if (
                    word == test_multiplier
                    or word == "{}{}".format(test_multiplier, "а")
                    or word == "{}{}".format(test_multiplier, "ов")
                    or word == "{}{}".format(test_multiplier, "и")
                ):
                    result += result_temp * (1000 ** (i + 1))
                    result_temp = 0
                    found = True
                    break

            if found:
                continue

            self.result = None

        self.result = result + result_temp


class MainClass:
    def __init__(self, input_str):

        obj_token = FileClass()
        self.token = obj_token.content
        self.input_str = input_str
        self.operations_list = {
            "плюс": "+",
            "минус": "-",
            "умножить на": "*",
            "умножить": "*",
        }
        self.r_operations_list = {"+": "сложение", "-": "вычитание", "*": "умножение"}
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
        abs_result = numeral.in_words(float(result))
        print("Число №1: " + n[0] + "\nЧисло №2: " + n[1])
        print("Операция: " + operation + "\nРезультат в виде числа: " + result)
        print("Результат прописью: " + abs_result + "\n")

    def number_collector(self):
        """
        Метод для 'собирания' сложного числа из его подкомпонентов
        Пример: двадцать четыре -> двадцать (20) + четыре (4)
        """

        input_str = self.input_str

        collectored_numbers = []
        detect_word = "целых"
        for numbers in input_str:
            # Тогда это дробь и мы ее переводим, лол
            if detect_word in numbers:

                t_obj = TranslaterClass(self.token, numbers)
                locale_number = w2n.word_to_num(t_obj.result)
                collectored_numbers.append(str(locale_number))

            # Тогда это число и мы его по составным числам считаем
            else:
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

    examples_list = [
        "ноль целых две десятых плюс восемь целых шесть сотых",
        "четыреста пятьдесят пять целых две десятых минус двадцать девять",
    ]
    for e in examples_list:
        print(e)
        MainClass(e)
