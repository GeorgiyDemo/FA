"""
Дан текстовый файл. Создайте двусвязный список, каждый элемент которого содержит
количество символов в соответствующей строке текста.
"""

TXT_FILE = "./text.txt"


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
        with open(TXT_FILE, "r") as stream:
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

        obj_list = []
        for txt in self.text:
            obj_list.append(Node(len(txt)))
            print("Занесли len '" + txt + "' " + str(len(txt)))

        for i in range(len(obj_list) - 1):
            obj_list[i].next = obj_list[i + 1]
            obj_list[i + 1].previous = obj_list[i]

        for i in range(len(obj_list)):
            print("-------\n*Элемент №" + str(i) + "*")
            print("Проход с начала в конец (next)")
            self.print_backward_next(obj_list[i])
            print("Проход с конца в начало (previous)")
            self.print_backward_previous(obj_list[i])


if __name__ == "__main__":
    ProcessingClass()
