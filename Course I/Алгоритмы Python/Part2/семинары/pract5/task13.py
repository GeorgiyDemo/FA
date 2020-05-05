"""
Задача 13*:
Дан текстовый файл. Создайте двусвязный список (или массив), каждый элемент которого
содержит количество символов в соответствующей строке текста.
"""
"""
Дан текстовый файл. Создайте двусвязный список, каждый элемент которого содержит
количество символов в соответствующей строке текста.
"""
import numpy as np

TXT_FILE = "./task13.txt"


class Node(object):

    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.value)


class ProcessingClass(object):

    def __init__(self):
        self.file2text()
        self.processing()

    def file2text(self):
        with open(TXT_FILE, 'r') as stream:
            list_m = stream.readlines()
            self.text = [e.replace("\n", "") for e in list_m]

    def print_backward_previous(self, lst):
        if lst == None:
            return
        head = lst
        tail = lst.next
        self.print_backward_previous(tail)
        print(head, head.previous)

    def print_backward_next(self, lst):
        if lst == None:
            return
        head = lst
        tail = lst.next
        self.print_backward_next(tail)
        print(head, head.next)

    def processing(self):

        obj_arr = np.array([])
        for txt in self.text:
            obj_arr = np.append(obj_arr, Node(len(txt)))
            print("Занесли '" + txt + "' " + str(len(txt)))

        for i in np.arange(obj_arr.shape[0] - 1):
            obj_arr[i].next = obj_arr[i + 1]
            obj_arr[i + 1].previous = obj_arr[i]

        for i in np.arange(obj_arr.shape[0]):
            print("-------\n*Элемент №" + str(i) + "*")
            print("Проход с начала в конец (next)")
            self.print_backward_next(obj_arr[i])
            print("Проход с конца в начало (previous)")
            self.print_backward_previous(obj_arr[i])


if __name__ == "__main__":
    ProcessingClass()
