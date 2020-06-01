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
# A merge sort algorithm that is probably bigger than it needs to be.
# Uses binary trees to sort integers.
# Runtime is probably O(NlogN)

from binarytree
class Node:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_root_val(self, obj):
        """Выставление значения"""
        self.value = obj

    def get_root_val(self):
        """Получение значения"""
        return self.value

    def get_right_child(self):
        """Получение подэлемента справа"""
        return self.right_child

    def get_left_child(self):
        """Получение подэлемента слева"""
        return self.left_child

    def compare(self, new_value):
        """Сравнение значений"""
        # If the value is greater or equal
        # Try stick it in the right
        if new_value >= self.value:
            if self.right_child:
                self.right_child.compare(new_value)
            else:
                # Create a node if there is no right yet.
                self.right_child = Node(new_value)

        if new_value < self.value:
            # If the value is less
            # Try stick it in the left
            if self.left_child:
                self.left_child.compare(new_value)
            else:
                # If there is nothing there yet create it
                self.left_child = Node(new_value)

    def sort(self):
        """Сортировка данных"""
        if self.left_child:
            self.left_child = self.left_child.sort()
        else:
            # Otherwise I'm the farthest left
            self.left_child = []

        # If there is something on the right: tell it to sort
        if self.right_child:
            self.right_child = self.right_child.sort()
        else:
            # Otherwise I'm the farthest right
            self.right_child = []

        # Return the sorted left children, me, and the sorted right children.
        return self.left_child + [self.value] + self.right_child

    def __str__(self):
        """Вывод структуры на экран"""

        left_val = "-" if self.left_child is None else self.left_child
        right_val = "-" if self.right_child is None else self.right_child

        return '{} ({}, {})'.format(self.value, left_val, right_val)


class SortedTree:

    def __init__(self):
        self.root = None

    def push(self, value):
        if self.root:
            # If we have a root then throw the value in to compare it.
            self.root.compare(value)
        else:
            # Otherwise start with a new root.
            # This could all be done in the __init__ tbf
            self.root = Node(value)

    def merge(self):
        return self.root.sort()

    def __str__(self):
        return self.root.__str__()

    
# Let's do this!

# Create a semi-random but actually human-biased array of integers.
items = [81, 77, 79, 68, 10, 12, 13, 20, 15, 24, 27, 42, 33, 51, 57]

# Instantiate the top of the tree
tree = SortedTree()
# Push each item into the tree (this is the first N in O(NlogN))
for value in items:
    tree.push(value)

print(tree)
# Merge the results (this is the logN bit)
# Funny thing: this will break if called immediately after instantiating.
print(tree.merge())