"""
Задача 12:
Пусть элементы списка/массива хранят символы предложения. Замените каждое вхождение слова
"itmathrepetitor" на "silence".
"""
import numpy as np

class MainClass(object):

    def __init__(self):
        input_str = input("Введите строку для замены 'itmathrepetitor' на 'silence' -> ")
        self.arr = np.array(list(input_str))
        self.sub_arr = np.array(list("itmathrepetitor"))
        self.replace_list = np.array(list("silence"))
        self.processing()

    def get_sublist_index(self):

        sub = self.sub_arr
        arr = self.arr
        sublen = len(sub)
        print(sub[0])
        first = sub[0] if sub else []
        indx = -1

        while True:
            try:
                indx = arr.index(first, indx + 1)
            except ValueError:
                break
            if sub == arr[indx: indx + sublen]:
                return True, indx, indx + len(sub)
        return False, 0, 0

    def processing(self):

        print("Список до замены:\n{}".format(self.arr))
        processing_flag = True

        while processing_flag:
            index_tuple = self.get_sublist_index()
            if index_tuple[0]:
                print("Замена подсписка по индексам", index_tuple[1], index_tuple[2])
                del self.arr[index_tuple[1]:index_tuple[2]]
                self.arr[index_tuple[1]:index_tuple[1]] = self.replace_list
            else:
                processing_flag = False

        print("Список после замены:\n" + str(self.arr))

if __name__ == "__main__":
    MainClass()