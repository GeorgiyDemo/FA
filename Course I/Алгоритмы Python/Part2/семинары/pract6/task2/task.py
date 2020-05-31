"""
Выполнить графовое представление и программную реализацию с помощью бинарного дерева следующие вычисления:
"""

class BinaryTree:
    """Улучшенный класс бинарного дерева"""

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



class Str2Tree:
    """ Класс для перевода строки в бинарное дерево"""
    
    def __init__(self, exp):
        
        self.exp = list(exp.replace(" ", ""))
        self.tree = BinaryTree()
        self.processing()

    def digital_checker(self, number):
        """Проверка значения на число"""
        try:
            int(number)
            return True
        except ValueError:
            return False

    def processing(self):

        tree = self.tree
        current = tree

        for token in self.exp:

            if token == "(":
                # добавляем новый узел в качестве левого узла
                current = current.insert_left()
            
            if token in ["+","−","/","*"]:
                # устанавливаем значение в текущем узле
                current.set_root_val(token)
                # добавляем узел в качестве правого узла и спускаемся в него.
                current = current.insert_right()

            if self.digital_checker(token):
                # устанавливаем значение в текущем узле
                current.set_root_val(token)
                # переходим к родительскому узлу. 
                current = current.get_parent()

            if token == ")":
                #переходим к родителю текущего узла. 
                current = current.get_parent()
        
        self.tree = tree

#TODO
class Tree2Result:
    """Вычисление выражений на основе бинарного дерева"""
    def __init__(self, binarytree_obj):
        if not isinstance(binarytree_obj, BinaryTree):
            raise ValueError("Объект не является объектом класса BinaryTree!")
        
    
    def counter(self, token, value=0):
        
        #Значит это число и мы достигли самого дна
        if token.get_left_child().get_root_val() == None and token.get_right_child().get_root_val() == None:
            return
        
        operation = token.get_root_val()
        first_value = token.get_left_child().get_root_val()
        second_value = token.get_second_child().get_root_val()
        

        value += eval(first_value+operation+second_value)
        print(value)
        self.counter()




        else:
            

        super().__init__()
if __name__ == "__main__":
    obj = Str2Tree("(3+(4*5))")
    print(obj.tree)