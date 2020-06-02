"""
В заданном на рисунке 3 бинарном дереве реализовать:
1. графически для заданных элементов добавление чисел: 38, 20, 8, 13, 47.
2. программную реализацию добавления элементов.

3. графически для заданных элементов удаления чисел: 33, 14, 5, 32.
4. программную реализацию удаления элементов.
"""

from sortedbinarytree_module import SortedTree


if __name__ == "__main__":

    items = [21, 7, 32, 5, 14, 4, 6, 2, 12, 9, 18, 27, 25, 24, 30, 37, 34, 39, 33]
    tree = SortedTree()
    for value in items:
        tree.push(value)

    print("Исходное дерево")
    print(tree)


    # Добавляем элементы
    add_list = [38, 20, 8, 13, 47]
    for value in add_list:
        tree.push(value)
    print("Дерево после добавления элементов",add_list)
    print(tree)

    #TODO
    #Удаляем элементы
    remove_list = [33, 14, 5, 32]
    for value in remove_list:
        tree.pull(value)
    
    print("Дерево после удаления элементов", remove_list)
    print(tree)


