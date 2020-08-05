"""
Реализовать шифр с использованием кодового слова,
используется латинский алфавит с верхним регистром.
"""

# pip3 install collections
# Нужон для подсчёта кол-ва символов в строке
import collections

GLOBAL_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class UtilClass(object):
    @staticmethod
    def check_dubl(check_str):
        """
        Метод для провери на то, чтоб не было дубликатов символов в строке
        """
        d = collections.defaultdict(int)
        for c in check_str:
            d[c] += 1

        for e in d:
            if d[e] != 1:
                return False

        return True

    @staticmethod
    def check_values(check_str):

        """
        Метод для возврата значения того, 
        чтоб символы кодового слова содержались в исходном алфавите  
        """

        bool_flag = True
        for char in check_str:
            if char not in GLOBAL_STR:
                bool_flag = False
        return bool_flag


class WordClass(object):
    def __init__(self, keyword, s):
        """
        Конструктор с вводом данных
        """
        self.keyword = keyword
        self.s = s
        self.result = ""
        self.buf_str = ""

        # Создаем новый сгенерированный алфавит в self.buf_str
        self.generator()

        # Шифруем слово
        self.encrypter()

    def generator(self):

        s = GLOBAL_STR
        print("\nИсходный алфавит:\n" + s)
        keyword = self.keyword
        for char in keyword:
            s = s.replace(char, "")
        self.buf_str = keyword + s
        print("\nСгенерировали новый алфавит замены:\n" + self.buf_str)

    def encrypter(self):

        """
        Метод для шифрования данных c использованием кодового слова
        
        """
        # Исходная строка
        input_str = self.s

        # Алфафит замены (старый)
        old_str = GLOBAL_STR

        # Алфавит замены (новый)
        buf_str = self.buf_str

        out = ""
        for char in input_str:
            out += buf_str[old_str.find(char)]
        print("\nРезультат:\n" + out)


def main():
    try:
        keyword = str(input("Введите кодовое слово -> "))
        s = str(input("Введите строку -> "))

    except:
        print("Что-то пошло не так при вводе данных")
        return

    if UtilClass.check_values(keyword) == False:
        print("Нет символов кодового слова в исходном алфавите!")
        return

    if UtilClass.check_dubl(keyword) == False:
        print(
            "Есть дубликат символов в введенной строке!\nТакие слова как WOOD, BOOK и т.д. нельзя использовать"
        )
        return

    WordClass(keyword, s)


if __name__ == "__main__":
    main()
