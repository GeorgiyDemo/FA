""""
Реализовать шифр Виженера, который состоит из последовательности нескольких шифров
Цезаря с различными значениями сдвига. Для зашифровывания может использоваться таблица алфавитов,
называемая tabula recta или квадрат (таблица) Виженера. 
Строка для шифрования должна быть на основе латинского алфавита, 
ключевое слово вводится с клавиатуры.
"""


def filter_input(s):
    """
    Метод для фильтрации
    Позволяет вводить только английские символы
    """

    try:
        s.encode(encoding="utf-8").decode("ascii")
        return True
    except:
        return False


def dict_generator():
    """
    Создание словаря символов для шифрованного слова из char
    //можно указать до 257, но тогда пойдут спецсимволы
    - Возвращает сгенерированный словарь
    """
    d = {}
    for i in range(128):
        d[i] = chr(i)
    return d


def crypter(w, k):
    """
    Сравнение кол-ва итераций с длинной ключа на основе индекса w и общего индекса k
    - Возвращает tuple с двумя словарями
    """
    outdict = {}
    sum_outdict = {}
    buf = 0

    for i in range(len(w)):

        sum_outdict[i] = w[i] + k[buf], w[i] - k[buf]
        outdict[i] = w[i], k[buf]
        buf += 1
        if buf >= len(k):
            buf = 0

    return (outdict, sum_outdict)


class VigenereClass(object):
    """
    Основной класс для шифрования строк согласно шифру Виженера
    """

    def __init__(self, w, k):

        self.w = w
        self.k = k

        self.input_d = dict_generator()

        self.k_indexes = self.encode_index(k)
        self.w_indexes = self.encode_index(w)

        self.encoded_list = self.full_encode(self.w_indexes, self.k_indexes)
        self.encoded = "".join(self.decode_index(self.encoded_list))

        self.decoded_list = self.full_decode(self.encoded_list, self.k_indexes)
        self.decoded = "".join(self.decode_index(self.decoded_list))

    def encode_index(self, input_word):
        """
        Получение букв в словаре и присвоение им индексов
        - Возвращает список с индексами элементов словаря
        """
        input_d = self.input_d
        outlist = []
        for char in range(len(input_word)):
            for element in input_d:
                if input_word[char] == input_d[element]:
                    outlist.append(element)
        return outlist

    def decode_index(self, input_list):
        """
        Дешифровка индексов на символы
        - Возвращает список list с символами
        """
        input_d = self.input_d
        outlist = []
        for i in range(len(input_list)):
            for element in input_d:
                if input_list[i] == element:
                    outlist.append(input_d[element])
        return outlist

    def full_encode(self, w, k):
        """
        Шифрование строк на основе сравнения индексов ключа и шифруемого слова
        - Возвращает список индексов list
        """
        input_d = self.input_d
        d = crypter(w, k)
        compared_dict = d[0]
        summed_dict = d[1]
        outlist = []

        for e in compared_dict:
            outlist.append(summed_dict[e][0] % len(input_d))
        return outlist

    def full_decode(self, w, k):
        """
        Расшифровка строк строк на основе сравнения индексов ключа и шифруемого слова
        - Возвращает список индексов list
        """
        input_d = self.input_d
        d = crypter(w, k)
        compared_dict = d[0]
        summed_dict = d[1]
        outlist = []

        for e in compared_dict:
            new_element = (summed_dict[e][1] + len(input_d)) % len(input_d)
            outlist.append(new_element)

        return outlist


def main():
    s = str(input("Введите строку для шифрования -> "))
    k = str(input("Введите ключ -> "))
    if filter_input(s) == False or filter_input(k) == False:
        print("Строки в задании могут содержать только английские символы!")
        return

    obj = VigenereClass(s, k)

    print("\n**Входные данные**")
    print("Слово: ", obj.w, "\nИндексы слова: ", obj.w_indexes)
    print("Ключ: ", obj.k, "\nИндексы ключа: ", obj.k_indexes)

    print("\n**Шифрование**")
    print("List: ", obj.encoded_list, "\nСлово: ", obj.encoded)

    print("\n**Расшифровка**")
    print("List: ", obj.decoded_list, "\nСлово: ", obj.decoded)


if __name__ == "__main__":
    main()
