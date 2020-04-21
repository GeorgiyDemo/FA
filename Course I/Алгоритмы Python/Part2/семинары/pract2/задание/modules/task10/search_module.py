def displaying(goods_list):
    for goods in goods_list:
        print(goods.get_info() + "\n")


def search(goods_list):
    try:
        price_input = float(input("Введите цену -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    search_flag = False
    print("Товары, которые вы можете себе позволить:")
    for goods in goods_list:
        if goods.opportunity_detector(price_input) == True:
            print(goods.get_info() + "\n")
            search_flag = True
    if not search_flag:
        print("Товары не найдены")
