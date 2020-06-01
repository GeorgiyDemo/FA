"""
Выполнить прямой обход (в ручном режиме и программную реализацию) бинарного дерева, представленного на рисунке 2.
Выполнить обратный обход (в ручном режиме и программную реализацию) бинарного дерева, представленного на рисунке 2.
Выполнить симметричный обход (в ручном режиме и программную реализацию) бинарного дерева, представленного на рисунке 2.
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
        return '{} ({}, {})'.format(self.get_root_val(), str(self.get_left_child()), str(self.get_right_child()))


class Orders:
    """Стат методы для обхода дерева"""
        
    @staticmethod
    def preorder(tree):
        """Прямой обход дерева"""
        if tree:
            print(tree.get_root_val())
            Orders.preorder(tree.get_left_child())
            Orders.preorder(tree.get_right_child())

    @staticmethod
    def inorder(tree):
        """Симметричный обход дерева"""
        if tree != None:
            Orders.inorder(tree.get_left_child())
            print(tree.get_root_val())
            Orders.inorder(tree.get_right_child())

    @staticmethod
    def postorder(tree):
        """Обратный обход"""
        if tree != None:
            Orders.postorder(tree.get_left_child())
            Orders.postorder(tree.get_right_child())
            print(tree.get_root_val())

def main():
    # Элемент на 1 уровне
    A = BinaryTree('A')

    #Элементы на 2 уровне
    B = A.insert_left('B')
    C = A.insert_right('C')

    #Элементы на 3 уровне
    D = B.insert_left("D")
    E = B.insert_right("E")
    F = C.insert_right("F")

    #Элементы на 4 уровне
    E.insert_left("G")
    F.insert_left("H")
    F.insert_right("I")

    print(A)

    #Обход в прямом порядке
    print("Прямой обход дерева:")
    Orders.preorder(A)

    #Обратный обход 
    print("Обратный обход дерева:")
    Orders.postorder(A)

    #Cимметричный обход 
    print("Cимметричный обход дерева:")
    Orders.inorder(A)

if __name__ == "__main__":
    main()