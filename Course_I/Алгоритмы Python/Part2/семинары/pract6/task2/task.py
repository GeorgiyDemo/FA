"""
Выполнить графовое представление и программную реализацию с помощью бинарного дерева следующие вычисления:
"""
import operator
from tree_module import BinaryTree


class Str2Tree:
    """ Класс для перевода строки в бинарное дерево"""

    def __init__(self, exp):
        self.exp = ["("] + list(exp.replace(" ", "")) + [")"]
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
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

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
    exp_list = ["2+2", "(2+3)*4", "(7+8)*(2-1)", "(7+8)*(2-1)+7", "((7+8)*(5-2))/(2-1)"]

    for e in exp_list:

        print("\nВыражение: {}".format(e))
        obj = Str2Tree(e)
        print("Разложение: {}".format(obj.tree))
        r_obj = Tree2Result(obj.tree)
        print("Результат вычисления: {}".format(r_obj.result))
        print("Результат по eval: {}".format(eval(e)))
