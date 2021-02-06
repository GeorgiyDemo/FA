import datatime

from abc import ABCMeta, abstractmethod
from pydantic import validate_arguments

class SQLModel(metaclass=ABCMeta):
    @abstractmethod
    def to_sql(self) -> str:
        pass

    def __str__(self):
        return str(self.__dict__)

class House(SQLModel):
    """Дом"""
    @validate_arguments
    def __init__(self, id : int, name : str, price : float, ac : int, tv : int, safe : int, description : str = None, _type: str = None, booking_id: int = None) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.ac = ac
        self.tv = tv
        self.safe = safe
        self.description = description
        self.type = _type
        self.booking_id = booking_id

    def to_sql(self) -> str:
        description = "'"+self.description+"'" if self.description is not None else "NULL"
        _type = "'"+self.type+"'" if self.type is not None else "NULL"
        booking_id = self.booking_id if self.booking_id is not None else "NULL"

        return f"INSERT INTO houses (id, name, price, ac, tv, safe, description, type, booking_id)\
            VALUES ({self.id},'{self.name}',{self.price},{self.ac},{self.tv},{self.safe},{description},{_type},{booking_id})"

class Client(SQLModel):
    """Клиент"""
    @validate_arguments
    def __init__(self, id : int, first_name : str, last_name : str, email : str, phone : str, document_title : str, document_file : bytes, document_text : str, document_comments : str = None, special_requests : str = None) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.document_title = document_title
        self.document_file = document_file
        self.document_text = document_text
        self.document_comments = document_comments
        self.special_requests = special_requests

    def to_sql(self) -> str:
        document_comments = "'"+self.document_comments+"'" if self.document_comments is not None else "NULL"
        special_requests = "'"+self.special_requests+"'" if self.special_requests is not None else "NULL"
        return f"INSERT INTO clients (id, first_name, last_name, email, phone, document_title, document_file, document_text, document_comments, special_requests)\
        VALUES ({self.id},'{self.first_name}','{self.last_name}','{self.email}','{self.phone}','{self.document_title}',{self.document_file},'{self.document_text}',{document_comments},{special_requests})"


class Order(SQLModel):
    """Заказ"""
    @validate_arguments
    def __init__(self, id : int, order_date: datatime.datatime, client_id : int, cost : float = None) -> None:
        self.id = id
        self.order_date = order_date.strftime('%Y-%m-%d %H:%M:%S')
        self.client_id = client_id
        self.cost = cost
    
    def to_sql(self) -> str:
        if self.cost is None:
            raise ValueError("Сначала необходимо выставить цену")

        return f"INSERTO INTO orders VALUES ({self.id},'{self.order_date}',{self.client_id},{self.cost})"

class Product(SQLModel):
    @validate_arguments
    def __init__(self, _id : int, title : str, price : float) -> None:
        self.id = _id
        self.title = title
        self.price = price
    
    def to_sql(self) -> str:
        return f"INSERT INTO products VALUES ({self.id},'{self.title}',{self.price})"

class ProductCount(SQLModel):
    @validate_arguments
    def __init__(self, count : int, product_id : int, order_id : int):
        self.count = count
        self.product_id = product_id
        self.order_id = order_id

    def to_sql(self) -> str:
        return f"INSERT INTO products_count(count, product_id, order_id) VALUES ({self.count}, {self.product_id}, {self.order_id})"