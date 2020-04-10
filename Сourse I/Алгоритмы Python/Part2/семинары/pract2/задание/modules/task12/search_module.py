def search(obj_list):
    try:
        input_name = input("Введите фамилию для поиска -> ")
    except ValueError:
        print("Некорректный ввод данных")
        return

    print("\n*Абоненты системы с фамилией \"" + input_name + "\"*")

    search_flag = False
    for obj in obj_list:
        if obj.search(input_name):
            search_flag = True
            print(obj.out_info() + "\n")

    if not search_flag:
        print("Абоненты не найдены")
