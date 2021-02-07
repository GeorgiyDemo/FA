import pymysql
import models
import random
import queue
from util import СircleCollection, RandomData

from faker import Faker
from db_logic import MySQLConnector


class Generator:
    """Генерация данных"""

    CURRENT_CLIENT_ID = 1
    CURRENT_ORDER_ID = 1
    CURRENT_PRODUCT_ID = 1
    CURRENT_BOOKING_ID = 1
    CURRENT_HOUSE_ID = 1
    CURRENT_STAFF_ID = 1

    def __init__(self, data_gen: RandomData) -> None:
        self.data_gen = data_gen
        self.fake_ru = data_gen.fake_ru
        self.fake_en = data_gen.fake_en

    def client_generator(self) -> models.Client:
        """Генерация клиента"""

        # Текущий ID
        cli_id = Generator.CURRENT_CLIENT_ID
        Generator.CURRENT_CLIENT_ID += 1

        # Работаем с именами
        first_name, last_name = self.data_gen.get_random_name()

        email = self.fake_ru.email()
        phone = self.fake_ru.phone_number()
        document_title = "Паспорт"

        # Рандомные байты
        document_file = (
            "0x" + bytearray(random.getrandbits(8) for _ in range(100)).hex()
        )
        document_text = f"ID {self.data_gen.get_number_range(4)} {self.data_gen.get_number_range(8)}"

        document_comments = random.choice((None, "срок действия заканчивется", "ok"))

        return models.Client(
            cli_id,
            first_name,
            last_name,
            email,
            phone,
            document_title,
            document_file,
            document_text,
            document_comments,
        )

    def order_generator(self, client_id: int) -> models.Order:
        """Генерация заказа клиента"""

        order_id = Generator.CURRENT_ORDER_ID
        Generator.CURRENT_ORDER_ID += 1
        order_date = self.fake_ru.date_time_between(start_date="-2y", end_date="now")
        cost = None  # <- рассчитывается позже в программе
        return models.Order(order_id, order_date, client_id, cost)

    def product_count_generator(
        self, product_id: int, order_id: int
    ) -> models.ProductCount:
        """Генерация кол-ва заказанных продуктов"""

        count = random.randint(1, 15)
        return models.ProductCount(count, product_id, order_id)

    def product_generator(self) -> models.Product:
        """Генерация заказанных клиентом продукта"""

        product_id = Generator.CURRENT_PRODUCT_ID
        Generator.CURRENT_PRODUCT_ID += 1
        title = self.fake_ru.words(1)[0]
        price = round(random.uniform(2.0, 1000.9), 2)
        return models.Product(product_id, title, price)

    def booking_generator(self, client_id: int, staff_id: int) -> models.Booking:
        """Генерация бронированя клиента"""

        booking_id = Generator.CURRENT_BOOKING_ID
        Generator.CURRENT_BOOKING_ID += 1
        date_in, date_out = self.data_gen.data_range_generator()
        cost = None
        return models.Booking(booking_id, date_in, date_out, client_id, staff_id, cost)

    def house_generator(self, booking_id: int = None) -> models.House:
        """Генерация дома"""

        house_types = ("Вилла", "Бунгало", "Таунхаус", "Пентхаус", "Коттедж")

        # Текущий ID
        house_id = Generator.CURRENT_HOUSE_ID
        Generator.CURRENT_HOUSE_ID += 1

        # Название и тип дома
        buf_name = " ".join(self.fake_en.words(2)).upper()
        house_type = random.choice(house_types)
        house_name = f"{house_type} {buf_name}"

        # Цена
        house_price = round(random.uniform(1500.0, 8000.9), 2)

        # Доп опции
        house_ac = random.choice((0, 1))
        house_tv = random.choice((0, 1))
        house_safe = random.choice((0, 1))

        house_description = f"Описание для дома с id {house_id}"

        return models.House(
            house_id,
            house_name,
            house_price,
            house_ac,
            house_tv,
            house_safe,
            house_description,
            house_type,
            booking_id,
        )

    def staff_generator(self) -> models.Staff:
        """Генерация обслуживающего персонала отеля"""

        staff_id = Generator.CURRENT_STAFF_ID
        Generator.CURRENT_STAFF_ID += 1

        # Работаем с именами
        first_name, last_name = self.data_gen.get_random_name()

        type_ = random.choice(("staff_booking", "staff_house"))
        if type_ == "staff_house":
            position = random.choice(
                (
                    "старший обслуживающий персонал",
                    "обслуживающий персонал",
                    "младший обслуживающий персонал",
                )
            )
        else:
            position = random.choice(("менеджер", "администратор"))
        phone = self.fake_ru.phone_number()
        return models.Staff(staff_id, first_name, last_name, position, type_, phone)

    def staffs_houses_generator(self, house_id : int, staff_id : int) -> models.StaffsHouses:
        return models.StaffsHouses(house_id, staff_id)

def main():

    HOST = "127.0.0.1"
    USER = "root"
    PASSWORD = "tiger"
    DB = "CONTROL_FA"

    # Осуществляем подключение
    locale_dict = {
        "host": HOST,
        "user": USER,
        "password": PASSWORD,
        "db": DB,
        "cursorclass": pymysql.cursors.DictCursor,
    }
    connection = MySQLConnector(locale_dict)

    # Инициализация генератора данных
    gen = Generator(RandomData())

    staffs_dict = {
        "staff_booking": СircleCollection(),
        "staff_house": СircleCollection(),
    }
    houses_queue = queue.Queue()
    houses_list = []

    # Генерируем обслуживающий персонал
    for _ in range(30):
        staff = gen.staff_generator()
        connection.write(staff.insert())
        staffs_dict[staff.type].put(staff)

    # Генерируем дома
    for _ in range(200):
        house = gen.house_generator()
        connection.write(house.insert())
        # Заносим в очередь (для бронирований)
        houses_queue.put(house)
        # Заносим в список (для назначени сотрудников)
        houses_list.append(house)

        print(f"Записали дом {house.id} -> {house.name}")

    # Генерируем пользователей
    for _ in range(40):
        client = gen.client_generator()
        connection.write(client.insert())
        print(f"Записали клиента {client.id} -> {client.first_name} {client.last_name}")

        # Добавляем заказы пользователя
        if random.choice((True, False)):
            for _ in range(random.randint(1, 20)):
                curent_order = gen.order_generator(client.id)
                connection.write(curent_order.insert())
                # Общая стоимость заказа
                order_cost = 0

                # Добавляем продукты в заказ
                for _ in range(random.randint(1, 20)):
                    product = gen.product_generator()
                    connection.write(product.insert())
                    # Добавляем кол-во продуктов
                    products_count = gen.product_count_generator(
                        product.id, curent_order.id
                    )
                    connection.write(products_count.insert())
                    order_cost += product.price * products_count.count

                curent_order.cost = order_cost
                connection.write(curent_order.update())

        # Добавляем бронирование для пользователя
        if random.choice((True, False)):
            for _ in range(random.randint(1, 5)):

                # Берем администратора
                current_staff = staffs_dict["staff_booking"].get()

                # Создаем бронирование
                current_booking = gen.booking_generator(client.id, current_staff.id)
                connection.write(current_booking.insert())

                #Аттачим дома
                prices_sum = 0
                for i in range(random.randint(1,4)):


                    # Берем дом
                    current_house = houses_queue.get_nowait()

                    # Обновляем FK для дома
                    current_house.booking_id = current_booking.id
                    connection.write(current_house.update())

                    #Добавляем цену дома к сумме
                    prices_sum += current_house.price

                # Обновляем стоимость бронирования
                days = current_booking.date_out - current_booking.date_in
                # Стоимость = цена дома * кол-во дней бронирования
                current_booking.cost = prices_sum * days.days
                connection.write(current_booking.update())

                # TODO: Один человек может обслуживать несколько домов и один дом может обслуживаться несколькими людьми.

    #Цикл по каждому дому
    for house in houses_list:

        # 1 дом могут обслуживать до 4 сотрудников
        for _ in range(random.randint(1,4)):

            current_staff = staffs_dict["staff_booking"].get()
            current_staffs_houses = gen.staffs_houses_generator(house.id, current_staff.id)
            
            #Записываем данные связывающей таблицы
            connection.write(current_staffs_houses.insert())
    
    print("Сгенерировали все данные")

if __name__ == "__main__":
    main()