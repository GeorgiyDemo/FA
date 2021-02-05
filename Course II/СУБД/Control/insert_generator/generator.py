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

    #TODO
    def client_generator(self):
        """Генерация клиента"""
        #_id 
        #_first_name
        #_last_name
        #_email
        #_phone
        #_document_title
        #_document_file
        #_document_text
        #_document_comments
        #_special_requests
        pass

    def order_generator(self):
        """Генерация заказа клиента"""
        #_id
        #_order_date
        #_cost  <- рассчитывается в программе
        pass

    def product_count_generator(self):
        #_count
        pass 

    def product_generator(self):
        """Генерация заказанных клиентом продукта""" 
        #_id
        #_title
        #_price
        pass
    
    def booking_generator(self):
        """Генерация бронированя клиента"""
        #_id
        #_date_in
        #_date_out
        #_cost
        pass

    def house_generator(self) -> models.House:
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

        return models.House(house_id, house_name, house_price, house_ac, house_tv, house_safe, house_description, house_type)

    
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
    #Генерируем дома
    for _ in range(10):
        house = gen.house_generator()
        connection.write(house.to_sql())
        print(connection.fetch("SELECT * FROM houses"))


    
    #result = connection.fetch("SELECT * FROM CLIENTS")
    #print(result)
    #print(type(result))

    #mystring = "INSERT INTO clients (id, first_name, last_name, email, phone, document_title, documant_file, document_text, document_comments) VALUES (2, ""
    #connection.write("")


if __name__ == "__main__":
    main()