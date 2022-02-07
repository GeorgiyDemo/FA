def search(goods_list):
    try:
        age_input = int(input("Введите возраст для фильтрации -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    search_flag = False
    print("Товары c фильтрацией по возрасту")
    for goods in goods_list:
        if goods.age_calculation(age_input) == True:
            print(goods.get_info() + "\n")
            search_flag = True
    if not search_flag:
        print("Товары не найдены")
