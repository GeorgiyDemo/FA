""""
Реализовать шифр Виженера, который состоит из последовательности нескольких шифров
Цезаря с различными значениями сдвига. Для зашифровывания может использоваться таблица алфавитов,
называемая tabula recta или квадрат (таблица) Виженера. 
Строка для шифрования должна быть на основе латинского алфавита, 
ключевое слово вводится с клавиатуры.
"""

def dict_generator():
    """
    Создание словаря символов для шифрованного слова из char
    //можно указать до 257, но тогда пойдут спецсимволы
    - Возвращает сгенерированный словарь
    """
    d = {}
    for i in range(129):
        d[i] = chr(i)
    return d

###########################################################################
def comparator( w, k):
        
    """
    Сравнение
    """

    outdict = {}
    buf_index = 0
    all_index = 0

    for i in w:
        outdict[all_index] = [i,k[buf_index]]
        all_index += 1
        buf_index += 1
        if (buf_index >= len(k)):
            buf_index = 0 
    return outdict 
###########################################################################

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
        compared_dict = comparator(w, k)
        outlist = []

        ########################################################################
        for value in compared_dict:
            go = (compared_dict[value][0]+compared_dict[value][1]) % len(input_d)
            outlist.append(go) 
        ########################################################################
        return outlist

    def full_decode(self, w, k):
        """
        Расшифровка строк строк на основе сравнения индексов ключа и шифруемого слова
        - Возвращает список индексов list
        """
        input_d = self.input_d 
        compared_dict = comparator(w, k)
        outlist = []
        
        ########################################################################
        for value in compared_dict:
            go = (compared_dict[value][0]-compared_dict[value][1]+len(input_d)) % len(input_d)
            outlist.append(go)
        ########################################################################
        
        return outlist

def main():

    obj = VigenereClass("meowmeowmeowmeow", "meow")
    
    print("\n**Входные данные**")
    print('Слово: ', obj.w, "\nИндексы слова: ", obj.w_indexes)
    print('Ключ: ', obj.k, "\nИндексы ключа: ", obj.k_indexes)

    print("\n**Шифрование**")
    print("List: ", obj.encoded_list, "\nСлово: ", obj.encoded)

    print("\n**Расшифровка**")
    print("List: ", obj.decoded_list, "\nСлово: ", obj.decoded)

if __name__ == "__main__":
    main()
