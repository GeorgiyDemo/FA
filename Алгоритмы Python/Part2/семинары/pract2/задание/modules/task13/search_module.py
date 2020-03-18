# Поиск клиентов, начавших сотрудничать с банком в заданную дату.
def search(bankclients_list):
    try:
        input_date = input("Введите дату для поиска клиентов в формате 01.01.2020 -> ")
        _, _, _ = input_date.split(".")
    except ValueError:
        print("Некорректный ввод данных")
        return
    search_flag = False
    print("Найденные клиенты:")
    for cli in bankclients_list:
        if cli.date_calculation(input_date) == True:
            print(cli.get_info() + "\n")
            search_flag = True
    if not search_flag:
        print("Клиенты не найдены")