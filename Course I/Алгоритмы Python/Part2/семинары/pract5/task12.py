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

    def rolling_window(self, a, window):
        shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
        strides = a.strides + (a.strides[-1],)
        return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

    def finder(self, a, b):
        temp = self.rolling_window(a, len(b))
        result = np.where(np.all(temp == b, axis=1))
        try:
            return result[0][0], result[0][0]+b.shape[0]
        except IndexError:
            return None

    def processing(self):
        """Логика обработки numpy"""

        replace_arr = self.replace_arr
        sub_arr = self.sub_arr
        arr = self.arr

        print("Список до замены:\n{}".format(arr))
        
        buf_arr = np.array(arr, copy=True)
        while True:
            r = self.finder(buf_arr, sub_arr)
            if r is None:
                #Доехали до окончания
                break
            subbuf_arr = np.append(buf_arr[:r[0]], replace_arr)    
            buf_arr = np.append(subbuf_arr, buf_arr[r[1]:])
    
        #Выставляем результат
        self.arr = buf_arr

    def printer(self):
        """Вывод результатов на экран"""
        print("Результаты замены:\n{}".format(self.arr))

if __name__ == "__main__":

    MainClass()