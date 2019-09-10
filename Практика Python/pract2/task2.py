"""
Реализовать шифр с использованием кодового слова,
используется латинский алфавит с верхним регистром.
"""

GLOBAL_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_values(check_str):
    
    """
    Функция для возврата значения того, 
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
        self.buf_str = ""

        #Создаем новый сгенерированный алфавит в self.buf_str
        self.generator()

        #Шифруем слово
        self.encrypter()
    
    def generator(self):
        
        s = GLOBAL_STR
        print("Исходный алфавит:\n"+s)
        keyword = self.keyword
        for char in keyword:
            s = s.replace(char,"")
        self.buf_str = keyword + s
        print("Сгенерировали новый алфавит замены:\n"+self.buf_str)

    def encrypter(self):
        
        """
        Метод для шифрования данных c использованием кодового слова
        
        """
        #Исходная строка
        input_str = self.s

        #Алфавит замены
        buf_str = self.buf_str

        out = ""
        for i in range(len(input_str)):
            out += buf_str[i]
        print(out)


def main():
    try:
        keyword = str(input("Введите кодовое слово -> "))
        s = str(input("Введите строку -> "))
        
    except:
        print("Что-то пошло не так при вводе данных")
        return
    if check_values(keyword) == False:
        print("Нет символов кодового слова в исходном алфавите!")
        return

    WordClass(keyword, s)

if __name__ == "__main__":
    main()