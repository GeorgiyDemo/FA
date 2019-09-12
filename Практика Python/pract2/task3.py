"""
Реализовать двух алфавитный шифр Цезаря для шифрования и 
дешифрование строки любой длины и заданным ключем,
используется латинский алфавит и цифры, а так же только нижний регистр.
https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BB%D0%B8%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%BD%D1%8B%D0%B9_%D1%88%D0%B8%D1%84%D1%80
"""

dictionaries = {
    0 : "abcdefghijklmnopqrstuvwxyz0123456789",
    1 : "abc0123456789ldefghijkmnopqrstuvwxyz"
}

class PolyWordClass(object):
    
    def __init__(self, s, key):

        self.s = s
        self.key = key

        #Шифруем слово
        self.main_encoded()

        #TODO Расшифровка слова
        self.main_decoded()
        

    

    def char_encoded(self, d, char):
        """
        Метод для шифрования данных по шифру Цезаря
        """
        k = self.key
        index = d.find(char)

        #Если длина ключа больше самой строки
        if k > len(d):
            k = k-len(d)

        if index+k >= len(d):
            return d[index+k-len(d)]
        else:
            return d[index+k]

    def main_encoded(self):
        
        """
        Метод для шифрования данных c использованием кодового слова
        
        """
        #Исходная строка
        input_str = self.s
        out = ""
        for i in range(len(input_str)):
            out += self.char_encoded(dictionaries[i % 2], input_str[i])
        self.encoded = out

    def main_decoded(self):
        self.decoded = "TEST"

def main():
    try:
        k = int(input("Введите сдвиг -> "))
        s = str(input("Введите строку -> "))
        
    except:
        print("Что-то пошло не так при вводе данных")
        return
    
    obj = PolyWordClass(s, k)
    
    print("\n**Шифрование**")
    print("\nРезультат:\n"+obj.encoded)

    print("\n**Расшифровка**")
    print("\nРезультат:\n"+obj.decoded)

if __name__ == "__main__":
    main()