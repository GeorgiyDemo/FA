"""
Задача 10. Создайте класс ТРАНСПОРТ с методами,
позволяющими вывести на экран информацию о транспортном средстве, а также определить,
находится ли транспортное средство в пределах заданных координат.

Создайте дочерние классы
САМОЛЕТ (марка, координаты, количество пассажиров, максимальная скорость, максимаьнльная высота),
АВТОМОБИЛЬ (марка, координаты, номер, год выпуска),
КОРАБЛЬ (название, координаты, количество пассажиров, максимальная скорость, порт приписки)
со своими методами вывода информации на экран и определения присутствия
транспортного средства в пределах заданных координат.

Создайте список из п транспортных средств, выведите полную информацию из базы на экран,
а также организуйте поиск транспортных средств, которые сейчас находятся в пределах заданных координат.
"""

from random import randint

from faker import Faker


class TransportClass():
    """
    Родительский класс транспорт
    """

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def coords_detector(self, coord_list):
        # Пример coord_list: ([x_begin,y_begin],[x_end,y_end])
        y_list, x_list = coord_list
        y1, y2 = y_list
        x1, x2 = x_list

        locale_x, locale_y = self.coords

        if x1 < locale_x < x2 and y1 < locale_y < y2:
            return True
        return False

    def coords_formater_str(self):
        x, y = self.coords
        return "[" + str(x) + ", " + str(y) + "]"

    def info(self):
        return "[Родительский класс транспорт]\nМодель: " + self.name + "\nКоординаты: " + self.coords_formater_str()


class AirplaneClass(TransportClass):
    """
    Класс Самолет
    """

    def __init__(self, name, coords, passengers_number, max_speed, max_height):
        super().__init__(name, coords)
        self.passengers_number = passengers_number
        self.max_speed = max_speed
        self.max_height = max_height

    def info(self):
        return "[Класс самолёт]\nМодель: " + self.name + "\nКоординаты: " + self.coords_formater_str() + "\nКол-во пассажиров: " + str(
            self.passengers_number) + "\nМакс. скорость: " + str(self.max_speed) + "\nМакс. высота: " + str(
            self.max_height)


class CarClass(TransportClass):
    """
    Класс автомобиль
    """

    def __init__(self, name, coords, number, year):
        super().__init__(name, coords)
        self.number = number
        self.year = year

    def info(self):
        return "[Класс автомобиль]\nМодель: " + self.name + "\nКоординаты: " + self.coords_formater_str() + "\nНомер: " + str(
            self.number) + "\nГод выпуска: " + str(self.year)


class ShipClass(TransportClass):
    """
    Класс Корабль
    """

    def __init__(self, name, coords, passengers_number, max_speed, destination_name):
        super().__init__(name, coords)
        self.passengers_number = passengers_number
        self.max_speed = max_speed
        self.destination_name = destination_name

    def info(self):
        return "[Класс корабль]\nМодель: " + self.name + "\nКоординаты: " + self.coords_formater_str() + "\nКол-во пассажиров: " + str(
            self.passengers_number) + "\nМакс. скорость: " + str(
            self.max_speed) + "\nПорт приписки: " + self.destination_name


def main():
    """
    Создайте список из п транспортных средств, выведите полную информацию из базы на экран,
    а также организуйте поиск транспортных средств, которые сейчас находятся в пределах заданных координат.
    """
    try:
        n = int(input("Введите кол-во транспортных средств -> "))

    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: TransportClass,
        2: AirplaneClass,
        3: CarClass,
        4: ShipClass,
    }

    fake = Faker(['ru_RU'])
    transport_list = []
    for _ in range(n):
        r_int = randint(1, 4)

        d_args = {
            1: (fake.word(), [randint(1, 100), randint(1, 100)]),
            2: (
            fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), randint(1000, 6000)),
            3: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(1960, 2020)),
            4: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), fake.word()),
        }

        transport_list.append(d[r_int](*d_args[r_int]))

    for transport in transport_list:
        print(transport.info() + "\n")

    # поиск транспортных средств, которые сейчас находятся в пределах заданных координат.
    search_flag = False
    # TODO Задание координат
    try:
        x1_input = int(input("Введите координату x1 -> "))
        y1_input = int(input("Ввдетие координату y1 -> "))

        x2_input = int(input("Введите координату x2 -> "))
        y2_input = int(input("Ввдетие координату y2 -> "))

        if x1_input < x2_input:
            x2_input, x1_input = x1_input, x2_input

        if y1_input < y2_input:
            y2_input, y1_input = y1_input, y2_input

    except ValueError:
        print("Некорректный ввод данных")
        return

    l = ([x1_input, y1_input], [x2_input, y2_input])
    print("\n*ТС, которые сейчас находятся в пределах заданных координат*")
    for transport in transport_list:
        if transport.coords_detector(l):
            print(transport.info() + "\n")
            search_flag = True

    if not search_flag:
        print("ТС не найдены")


if __name__ == "__main__":
    main()
