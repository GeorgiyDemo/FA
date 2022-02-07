"""
Реализовать двух алфавитный шифр Цезаря для шифрования и 
дешифрование строки любой длины и заданным ключем,
используется латинский алфавит и цифры, а так же только нижний регистр.
"""

dictionaries = {
    0: "abcdefghijklmnopqrstuvwxyz0123456789",
    1: "abc0123456789ldefghijkmnopqrstuvwxyz",
}


def check_values(check_str):
    """
    Метод для возврата значения boolen того,
    чтоб символы кодируемого слова содержались в алфавитах
    """

    bool_flag = True
    for char in check_str:
        for d in dictionaries:
            if char not in dictionaries[d]:
                bool_flag = False

    return bool_flag


class PolyWordClass(object):
    def __init__(self, s, key):

        self.s = s
        self.key = key

        # Шифруем слово
        self.main_encoded()

        # Расшифровка слова
        self.main_decoded()

    def char_encoded(self, d, char):
        """
        Метод для шифрования данных по классическому шифру Цезаря
        (взял со своего задания №1)
        """
        k = self.key
        index = d.find(char)

        # Если длина ключа больше самой строки
        if k > len(d):
            k = k - len(d)

        if index + k >= len(d):
            return d[index + k - len(d)]
        else:
            return d[index + k]

    def char_decoded(self, d, char):
        """
        Метод для расшифровки данных по классическому шифру Цезаря
        (взял со своего задания №1)
        """
        k = self.key
        index = d.find(char)

        # Если длина ключа больше самой строки
        if k > len(d):
            k = k - len(d)

        if index - k >= len(d):
            return d[index - k + len(d)]
        else:
            return d[index - k]

    def main_encoded(self):

        """
        Метод для определения того, какой словарь необходимо использовать
        В данном случае идёт чередование по вызову dict dictionaries (масло масленное)
        в зависмости от чётности переменной цикла i
        """

        input_str = self.s
        out = ""
        for i in range(len(input_str)):
            out += self.char_encoded(dictionaries[i % 2], input_str[i])
        self.encoded = out

    def main_decoded(self):

        """
        Метод аналогичен main_encoded, но только с
        вызовом self.char_decoded вместо self.char_encoded
        """

        input_str = self.encoded
        out = ""
        for i in range(len(input_str)):
            out += self.char_decoded(dictionaries[i % 2], input_str[i])
        self.decoded = out


def main():
    try:

        k = int(input("Введите сдвиг -> "))
        s = str(input("Введите строку -> "))

    except:
        print("Что-то пошло не так при вводе данных")
        return

    if check_values(s) == False:
        print("Нет символов введенной строки в исходном алфавите!")
        return

    obj = PolyWordClass(s, k)

    print("\n**Шифрование**\nРезультат: " + obj.encoded)
    print("\n**Расшифровка**\nРезультат: " + obj.decoded)


if __name__ == "__main__":
    main()
