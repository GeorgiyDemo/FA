def display(toy_list):
    for toy in toy_list:
        print(toy.toy_info() + "\n")


def search(toy_list):
    # организуйте поиск игрушек заданного цвета.
    try:
        color_input = input("Введите цвет для поиска игрушек -> ")
    except ValueError:
        print("Некорректный ввод данных")
        return
    search_flag = False
    print("Игрушки c фильтрацией по цвету")
    for toy in toy_list:
        if toy.color_detector(color_input):
            print(toy.toy_info() + "\n")
            search_flag = True
    if not search_flag:
        print("Игрушки не найдены")
