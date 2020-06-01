"""
Выполнить представление через множества и ленточное представления бинарного дерева, представленного на рис. 1
"""

from tree_module import BinaryTree

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
