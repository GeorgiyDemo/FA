"""
Выполнить программную реализацию и сравнительный анализ быстродействия поиска элементов с помощью бинарного дерева в заданном массиве элементов:81 77 79 68 10 12 13 20 15 24 27 42 33 51 57.
Для этого:

1. Реализовать представление данных с помощью бинарного дерева;

2. Реализовать поиск элементов в массиве с учетом времени на поиск
3. Реализовать поиск элемента в бинарном дереве с учетом времени на
поиск
4. Реализовать поиск элементов в отсортированном массиве с учетом
времени на поиск

5. Провести сравнительный анализ представления данных в трех
программных реализациях.

"""

class BinaryTree:
    """Класс бинарного дерева"""

    def __init__(self, root=None, parent=None):
        self.key = root
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node=None):
        """Вставка элемента слева"""
        if self.left_child == None:
            self.left_child = BinaryTree(new_node, self)
        else:
            t = BinaryTree(new_node, self)
            t.left_child = self.left_child
            self.left_child = t
        
        return self.left_child

    def insert_right(self, new_node=None):
        """Вставка элемента справа"""
        if self.right_child == None:
            self.right_child = BinaryTree(new_node, self)
        else:
            t = BinaryTree(new_node, self)
            t.right_child = self.right_child
            self.right_child = t

        return self.right_child

    def get_parent(self):
        """Получение узла-родителя"""
        return self.parent

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
    data = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]
    tree = BinaryTree(data[0])
    main_tree = tree
    for e in data[1:]:
        if tree.get_root_val() > e:
            tree = tree.insert_left(e)
        elif tree.get_root_val() < e:
            tree = tree.insert_right(e)

    print(main_tree)





if __name__ == "__main__":
    main()