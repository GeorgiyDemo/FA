import pymysql
import models
import random

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

    def __init__(self) -> None:
        self.fake_ru = Faker("ru_RU")
        self.fake_en = Faker("en_GB")
    
    def get_number_range(self, n) -> str:
        """Отдает n рандомных цифр"""
        result = ""
        for _ in range(n): result += str(random.choice(range(10)))
        return result

    #TODO
    def client_generator(self) -> models.Client:
        """Генерация клиента"""

        #Текущий ID
        cli_id = Generator.CURRENT_CLIENT_ID
        Generator.CURRENT_CLIENT_ID += 1

        #Работаем с именами. Случайно выбираем русское имя в транслите или типичное английское
        names_list = [self.fake_ru.name().replace("'","").split(" "), self.fake_en.name().replace("'","").split(" ")]
        current_name_list = random.choice(names_list)
        if len(current_name_list) == 4:
            _, first_name, last_name, _ = current_name_list
        elif len(current_name_list) == 3:
            first_name, _, last_name = current_name_list
        else:
            first_name, last_name = current_name_list

        email = self.fake_ru.email()
        phone = self.fake_ru.phone_number()
        document_title = "Паспорт"

        #Рандомные байты
        document_file = "0x"+bytearray(random.getrandbits(8) for _ in range(100)).hex()
        document_text = f"ID {self.get_number_range(4)} {self.get_number_range(8)}"

        document_comments = random.choice((None,"срок действия заканчивется","ok"))

        return models.Client(cli_id, first_name, last_name, email, phone, document_title, document_file, document_text, document_comments)

    def order_generator(self, client_id : int) -> models.Order:
        """Генерация заказа клиента"""
        order_id = Generator.CURRENT_ORDER_ID
        Generator.CURRENT_ORDER_ID += 1
        order_date = self.fake_ru.date_time_between(start_date='-2y', end_date='now')
        cost = None # <- рассчитывается позже в программе
        return models.Order(order_id,order_date, client_id, cost)

    def product_count_generator(self, product_id : int, order_id : int) -> models.ProductCount:
        """Генерация кол-ва заказанных продуктов"""
        count = random.randint(1,100)
        return models.ProductCount(count, product_id, order_id) 

    def product_generator(self) -> models.Product:
        """Генерация заказанных клиентом продукта"""
        product_id = Generator.CURRENT_PRODUCT_ID
        Generator.CURRENT_PRODUCT_ID += 1
        title = self.fake_ru.words(1)[0]
        price = round(random.uniform(2.0, 1000.9),2)
        return models.Product(product_id, title, price)
    
    def booking_generator(self):
        """Генерация бронированя клиента"""
        #_id
        #_date_in
        #_date_out
        #_cost
        pass

    def house_generator(self, booking_id : int = None) -> models.House:
        """Генерация дома"""
        
        house_types = ("Вилла", "Бунгало", "Таунхаус", "Пентхаус", "Коттедж")
        
        #Текущий ID
        house_id = Generator.CURRENT_HOUSE_ID
        Generator.CURRENT_HOUSE_ID += 1
        
        #Название и тип дома
        buf_name = " ".join(self.fake_en.words(2)).upper()
        house_type = random.choice(house_types)
        house_name = f"{house_type} {buf_name}"

        #Цена
        house_price = random.randint(3500, 15000)

        #Доп опции
        house_ac = random.choice((0,1))
        house_tv = random.choice((0,1))
        house_safe = random.choice((0,1))

        house_description = f"Описание для дома с id {house_id}"

        return models.House(house_id, house_name, house_price, house_ac, house_tv, house_safe, house_description, house_type, booking_id)

    
    def staff_generator(self):
        """Генерация обслуживающего персонала отеля"""
        #_id
        #_first_name
        #_last_name
        #_position
        #_type - staff_booking или staff_house (staff относится либо к бронированиям, либо к обслуживанию дома)
        #_phone
        pass

def main():

    HOST = "127.0.0.1"
    USER = "root"
    PASSWORD = "tiger"
    DB = "CONTROL_FA"
    
    #Осуществляем подключение
    locale_dict = {"host": HOST, "user":USER, "password" : PASSWORD, "db" : DB, "cursorclass" : pymysql.cursors.DictCursor}
    connection = MySQLConnector(locale_dict)
    
    #Инициализация генератора данных 
    gen = Generator()

    #Генерируем пользователей
    for _ in range(100):
        client = gen.client_generator()
        connection.write(client.to_sql())
        print(f"Записали клиента {client.id} -> {client.first_name} {client.last_name}")

        #Добавляем заказы пользователя
        if random.choice((True, False)):
            for i in range(random.randint(1,20)):
                curent_order = gen.order_generator(client.id)
                #Общая стоимость заказа
                order_cost = 0
                
                #Добавляем продукты в заказ
                for i in range(random.randint(1,20)):
                    product = gen.product_generator()
                    connection.write(product.to_sql())
                    #Добавляем кол-во продуктов
                    products_count = gen.product_count_generator(product.id,curent_order.id)
                    connection.write(products_count.to_sql())
                    order_cost += (product.price * products_count.count)
                
                curent_order.cost = order_cost
                connection.write(curent_order.to_sql())
                    




    #Генерируем дома
    for _ in range(10):
        house = gen.house_generator()
        connection.write(house.to_sql())
        print(f"Записали дом {house.id} -> {house.name}")
    
    #result = connection.fetch("SELECT * FROM CLIENTS")
    #print(result)
    #print(type(result))

    #mystring = "INSERT INTO clients (id, first_name, last_name, email, phone, document_title, documant_file, document_text, document_comments) VALUES (2, ""
    #connection.write("")


if __name__ == "__main__":
    main()