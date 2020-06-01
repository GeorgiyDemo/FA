"""
Выполнить представление через множества и ленточное представления бинарного дерева, представленного на рис. 1
"""


class BinaryTree:
    """Класс бинарного дерева"""

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """Вставка элемента слева"""
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
        
        return self.left_child

    def insert_right(self, new_node):
        """Вставка элемента справа"""
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

        return self.right_child

    def get_right_child(self):
        """Получение подэлемента справа"""
        return self.right_child

    def get_left_child(self):
        """Получение подэлемента слева"""
        return self.left_child

    def set_root_val(self, obj):
        """Выставление значения"""
        self.key = obj

    def get_root_val(self):
        """Получение значения"""
        return self.key

    def __str__(self):
        """Вывод структуры на экран"""

        left_val = "-" if self.get_left_child() is None else self.get_left_child()
        right_val = "-" if self.get_right_child() is None else self.get_right_child()

        return '{} ({}, {})'.format(self.get_root_val(), left_val, right_val)

def main():

    # Элемент на 1 уровне
    r = BinaryTree('8')

    #Элементы на 2 уровне
    r_1 = r.insert_left('4')
    r_2 = r.insert_right('12')

    # Элементы на 3 уровне
    r_11 = r_1.insert_left('2')
    r_12 = r_1.insert_right('6')
    r_21 = r_2.insert_left('10')
    r_22 = r_2.insert_right('14')


    # Добавление элементов на 4 уровень

    r_11.insert_left('1')
    r_11.insert_right('3')
    r_12.insert_left('5')
    r_12.insert_right('7')

    r_21.insert_left('9')
    r_21.insert_right('11')
    r_22.insert_left('13')
    r_22.insert_right('15')

    print("Реализованное дерево:")
    print(r)


if __name__ == "__main__":
    main()
