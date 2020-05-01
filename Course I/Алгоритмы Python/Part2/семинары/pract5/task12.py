"""
Задача 12:
Пусть элементы списка/массива хранят символы предложения. Замените каждое вхождение слова
"itmathrepetitor" на "silence".
Используется ВСЕ, чтоб точно понять, что более подходящее
"""

import numpy as np
import timeit
import array as ar

class ArrClass:
    def __init__(self, arr):
        self.arr = ar.array('u', arr)
        self.old_arr = ar.array('u', 'itmathrepetitor')
        self.new_arr = ar.array('u', 'silence')

        self.processing()
        self.printer()

    def processing(self):

        old = self.old_arr
        new = self.new_arr
        a = self.arr

        for i in range(len(a) - len(old) + 1):
            if a[i:i + len(old)] == old:
                a[i:i + len(old)] = new
        
        self.arr = a
    
    def printer(self):
        """Вывод результатов на экран"""
        print("Результаты замены:\n{}".format(self.arr))


class ListClass:

    def __init__(self, l):
        self.list = list(l)
        self.sub_list = list("itmathrepetitor")
        self.replace_list = list("silence")
        self.processing()

    def get_sublist_index(self):

        sub = self.sub_list
        lst = self.list
        sublen = len(sub)
        first = sub[0] if sub else []
        indx = -1

        while True:
            try:
                indx = lst.index(first, indx + 1)
            except ValueError:
                break
            if sub == lst[indx: indx + sublen]:
                return True, indx, indx + len(sub)
        return False, 0, 0

    def processing(self):

        print("Список до замены:\n" + str(self.list))
        processing_flag = True

        while processing_flag == True:
            index_tuple = self.get_sublist_index()
            if index_tuple[0] == True:
                print("Замена подсписка по индексам", index_tuple[1], index_tuple[2])
                del self.list[index_tuple[1]:index_tuple[2]]
                self.list[index_tuple[1]:index_tuple[1]] = self.replace_list
            else:
                processing_flag = False

        print("Список после замены:\n" + str(self.list))

#Не всегда работает

class NumpyClass(object):

    def __init__(self, l):
        self.arr = np.array(list(l +' '))
        self.sub_arr = np.array(list("itmathrepetitor"))
        self.replace_arr = np.array(list("silence"))
        self.processing()
        self.printer()

    def rolling_window(self, a, window):
        shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
        temp_array = np.array([])
        for step in range(shape[0]):
            temp_array = np.concatenate((temp_array, a[step:shape[-1]+step]))
        return np.reshape(temp_array, shape)

    def finder(self, a, b):
        temp = self.rolling_window(a, len(b))
        try:
            warnings.simplefilter(action='ignore', category=FutureWarning)
            result = np.where(np.all(b == temp, axis=1))
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
            try:
                r = self.finder(buf_arr, sub_arr)
                if r is None:
                    #Доехали до окончания
                    break
                subbuf_arr = np.append(buf_arr[:r[0]], replace_arr)    
                buf_arr = np.append(subbuf_arr, buf_arr[r[1]:])
            except Exception:
                break
    
        #Выставляем результат
        self.arr = buf_arr[:-1]

    def printer(self):
        """Вывод результатов на экран"""
        print("Результаты замены:\n{}".format(self.arr))


if __name__ == "__main__":
    s = input("Введите строку для замены 'itmathrepetitor' на 'silence' -> ")

    a = timeit.default_timer()
    ListClass(s)
    print('\nВремя на работу с помощью list', timeit.default_timer()-a)
    a = timeit.default_timer()
    ArrClass(s)
    print('\nВремя на работу с помощью array', timeit.default_timer()-a)
    a = timeit.default_timer()
    NumpyClass(s)
    print('\nВремя на работу с помощью numpy', timeit.default_timer()-a)