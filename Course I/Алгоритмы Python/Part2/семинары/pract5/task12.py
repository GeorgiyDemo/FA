"""
Задача 12:
Пусть элементы списка/массива хранят символы предложения. Замените каждое вхождение слова
"itmathrepetitor" на "silence".
"""
import numpy as np



class MainClass(object):

    def __init__(self):
        self.arr = np.array(list(input("Введите строку для замены 'itmathrepetitor' на 'silence' -> ")))
        self.sub_arr = np.array(list("itmathrepetitor"))
        self.replace_arr = np.array(list("silence"))
        self.processing()
        self.printer()

    def get_replacechar(self):
        """Генерация буферного символа, чтоб размер маски не изменялся"""
        replace_chars = np.array(["0","@","#","_","-","|"])
        for char in replace_chars:
            if char not in self.arr:
                return char
        
        raise ValueError("Мне нужно больше разделителей!", "Что за странный текст ты ввел, и главное, зачем?")

    def processing(self):
        """
        Логика обработки массива numpy
        - Получаем маску соответствия subarray
        - Увеличиваем кол-во знаков для соответствия маске (т.к. "itmathrepetitor" длиннее "silence")
        - Формирования массива замены символов на основе маски
        - Наложение маски
        - Удаление буферных символов
        """
        
        replace_arr = self.replace_arr
        sub_arr = self.sub_arr
        arr = self.arr

        print("Список до замены:\n{}".format(arr))
        print("Длинна:",arr.shape)

        #Получаем маску subarrays
        mask = np.isin(arr, sub_arr)
        print("МАСКА",mask)
        #Увеличиваем кол-во знаков в replace_arr
        #Выбираем буферный символ, которого нет в исходной строке
        char = self.get_replacechar()

        #Один элемент для замены последовательности True
        replace_item = np.append(replace_arr,[char for _ in range(sub_arr.shape[0] - replace_arr.shape[0])])

        #Формируем массив замены replace_arr по маске mask
        replace_arr = np.array([])
        index = 0
        for i in np.arange(mask.shape[0]):
            if index == replace_item.shape[0]:
                index = 0
            if mask[i]:
                replace_arr = np.append(replace_arr,replace_item[index])
                index += 1            
        

        #Меняем данные в массиве по маске
        arr[mask] = replace_arr

        #Удаляем буферные элементы
        arr = arr[arr != char]

        #Выставляем результат
        self.arr = arr

    def printer(self):
        """Вывод результатов на экран"""
        print("Результаты замены:\n{}".format(self.arr))

if __name__ == "__main__":

    MainClass()
