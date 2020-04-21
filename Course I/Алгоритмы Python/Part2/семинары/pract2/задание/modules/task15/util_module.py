def display(transport_list):
    for transport in transport_list:
        print(transport.info() + "\n")


def search(transport_list):
    search_flag = False
    try:
        x1_input = int(input("Введите координату x1 -> "))
        y1_input = int(input("Ввдетие координату y1 -> "))
        x2_input = int(input("Введите координату x2 -> "))
        y2_input = int(input("Ввдетие координату y2 -> "))
        if x1_input < x2_input: x2_input, x1_input = x1_input, x2_input
        if y1_input < y2_input: y2_input, y1_input = y1_input, y2_input
    except ValueError:
        print("Некорректный ввод данных")
        return
    l = ([x1_input, y1_input], [x2_input, y2_input])
    print("\n*ТС, которые сейчас находятся в пределах заданных координат*")
    for transport in transport_list:
        if transport.coords_detector(l):
            print(transport.info() + "\n")
            search_flag = True
    if not search_flag: print("ТС не найдены")
