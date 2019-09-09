
class CtsezarClass(object):
    
    def __init__(self):
        """
        Конструктор с вводом данных
        """
        self.GLOBAL_STR = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцшщъыьэюя0123456789 .,;...?:!()-|\"«»\'"
        
        try:
            k = int(input("Введите сдвиг K -> "))
            s = str(input("Введите строку -> "))
        except:
            print("Что-то пошло не так при вводе данных")
            return

        out = ""
        for char in s:
            out += self.set_index(char, k)
        print("Зашифрованный ключ: " + out)

        s1 = ""
        for char in out:
            s1 += self.get_index(char, k)
        print("Расшифрованный ключ: " + s1)
        
    def set_index(self, char, k):
        """
        Метод для шифрования данных по шифру Цезаря
        """
        s = self.GLOBAL_STR
        index = s.find(char)

        #Если длина ключа больше самой строки
        if k > len(s):
            k = k-len(s)

        if index+k >= len(s):
            return s[index+k-len(s)]
        else:
            return s[index+k]

    def get_index(self, char, k):
        """
        Метод для расшифровки данных по шифру Цезаря
        """
        s = self.GLOBAL_STR
        index = s.find(char)

        #Если длина ключа больше самой строки
        if k > len(s):
            k = k-len(s)

        if index-k >= len(s):
            return s[index-k+len(s)]
        else:
            return s[index-k]


if __name__ == "__main__":
    CtsezarClass()