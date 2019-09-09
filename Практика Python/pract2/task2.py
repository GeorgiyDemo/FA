
class WordClass(object):
    
    def __init__(self, word):
        """
        Конструктор с вводом данных
        """
        self.GLOBAL_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.word = word
        self.buf_str = ""
        try:
            k = int(input("Введите сдвиг K -> "))
            s = str(input("Введите строку -> "))
        
        except:
            print("Что-то пошло не так при вводе данных")
            return

        self.generator()

        #out = ""
        #for char in s:
        #    out += self.set_index(char, k)
        #print("Зашифрованный ключ: " + out)

    
    def generator(self):
        s = self.GLOBAL_STR
        word = self.word
        for char in word:
            s.replace(char,"")
        self.buf_str = word + s
        print(self.buf_str)
        

    def set_index(self, char, k):
        """
        Метод для шифрования данных c использованием кодового слова
        """
        s = self.GLOBAL_STR
        index = s.find(char)

        
        

        if index+k >= len(s):
            return s[index+k-len(s)]
        else:
            return s[index+k]


if __name__ == "__main__":
    WordClass("WORD")