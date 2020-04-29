"""
Задача 12:
Пусть элементы списка/массива хранят символы предложения. Замените каждое вхождение слова
"itmathrepetitor" на "silence".
"""
import numpy as np



def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

def findFirst_numpy(a, b):
    temp = rolling_window(a, len(b))
    result = np.where(np.all(temp == b, axis=1))
    print(result)
    print(type(result))
    if result != []:
        return result[0][0], result[0][0]+b.shape[0]
    return None


class MainClass(object):

    def __init__(self):
        self.arr = np.array(list(input("Введите строку для замены 'itmathrepetitor' на 'silence' -> ")))
        self.sub_arr = np.array(list("itmathrepetitor"))
        self.replace_arr = np.array(list("silence"))
        self.processing()
        #self.printer()

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
        
        #Получаем все индексы до замены

        stop_flag = False
        indexes_arr = np.array([])
        buf_arr = np.array(arr, copy=True)
        while not stop_flag:
            r = findFirst_numpy(buf_arr, sub_arr)
            print(r)
            if r is None:
                #Доехали до окончания
                break
            subbuf_arr = np.append(buf_arr[:r[0]],replace_arr)    
            buf_arr = np.append(subbuf_arr,buf_arr[r[1]:])
            print(buf_arr)
        
        
        #Выставляем результат
        #self.arr = arr

    def printer(self):
        """Вывод результатов на экран"""
        print("Результаты замены:\n{}".format(self.arr))

if __name__ == "__main__":

    MainClass()
