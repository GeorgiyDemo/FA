"""
Выполнить графовое представление и программную реализацию с помощью бинарного дерева следующие вычисления:
"""
import operator


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

class Str2Tree:
    """ Класс для перевода строки в бинарное дерево"""

    def __init__(self, exp):
        self.exp = ["("]+list(exp.replace(" ", ""))+[")"]
        print(self.exp)
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

            elif token in ["+", "-", "/", "*"]:
                # устанавливаем значение в текущем узле
                current.set_root_val(token)
                # добавляем узел в качестве правого узла и спускаемся в него.
                current = current.insert_right()

            elif self.digital_checker(token):
                # устанавливаем значение в текущем узле
                current.set_root_val(int(token))
                # переходим к родительскому узлу.
                current = current.get_parent()

            elif token == ")":
                # переходим к родителю текущего узла.
                current = current.get_parent()

            else:
                print(token)
                raise ValueError("Я не понимаю что это")

        self.tree = tree


class Tree2Result:
    """Вычисление выражений на основе бинарного дерева"""

    def __init__(self, binarytree_obj):
        if not isinstance(binarytree_obj, BinaryTree):
            raise ValueError("Объект не является объектом класса BinaryTree!")

        self.result = self.processing(binarytree_obj)

    def processing(self, token):
        """Обход бинарного дерева в обратном порядке"""
        operators = {'+': operator.add, '-': operator.sub,
                     '*': operator.mul, '/': operator.truediv}

        # Левые/правые значения
        left_value = token.get_left_child()
        right_value = token.get_right_child()

        # Если оба есть - падаем ниже
        if left_value and right_value:
            fn = operators[token.get_root_val()]
            # Отдаем результат выражения
            return fn(self.processing(left_value), self.processing(right_value))
        else:
            # Иначе, если уже некуда падать, отдаем текущее значение
            return token.get_root_val()


if __name__ == "__main__":
    exp_list = ["2+2", "(2+3)*4", "(7+8)*(2-1)",
                "(7+8)*(2-1)+7", "((7+8)*(5-2))/(2-1)"]

    for e in exp_list:

        print("\nВыражение: {}".format(e))
        obj = Str2Tree(e)
        print("Разложение: {}".format(obj.tree))
        r_obj = Tree2Result(obj.tree)
        print("Результат вычисления: {}".format(r_obj.result))
        print("Результат по eval: {}".format(eval(e)))
