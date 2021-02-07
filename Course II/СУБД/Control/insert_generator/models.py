import datetime

from abc import ABCMeta, abstractmethod
from pydantic import validate_arguments


class SQLModel(metaclass=ABCMeta):
    @abstractmethod
    def insert(self) -> str:
        pass

    def __str__(self):
        return str(self.__dict__)


class House(SQLModel):
    """Дом"""

    @validate_arguments
    def __init__(
        self,
        id: int,
        name: str,
        price: float,
        ac: int,
        tv: int,
        safe: int,
        description: str = None,
        type_: str = None,
        booking_id: int = None,
    ) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.ac = ac
        self.tv = tv
        self.safe = safe
        self.description = description
        self.type = type_
        self.booking_id = booking_id

    def insert(self) -> str:
        description = (
            "'" + self.description + "'" if self.description is not None else "NULL"
        )
        type_ = "'" + self.type + "'" if self.type is not None else "NULL"
        booking_id = self.booking_id if self.booking_id is not None else "NULL"
        return f"INSERT INTO houses (id, name, price, ac, tv, safe, description, type, booking_id) VALUES ({self.id},'{self.name}',{self.price},{self.ac},{self.tv},{self.safe},{description},{type_},{booking_id})"

    def update(self) -> str:
        if self.booking_id is None:
            raise ValueError("booking_id не может быть None при обновлении")
        return f"UPDATE houses SET booking_id={self.booking_id} WHERE id={self.id}"


class Client(SQLModel):
    """Клиент"""

    @validate_arguments
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        document_title: str,
        document_file: str,
        document_text: str,
        document_comments: str = None,
        special_requests: str = None,
    ) -> None:
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

    def insert(self) -> str:
        document_comments = (
            "'" + self.document_comments + "'"
            if self.document_comments is not None
            else "NULL"
        )
        special_requests = (
            "'" + self.special_requests + "'"
            if self.special_requests is not None
            else "NULL"
        )

        return_str = "INSERT INTO clients (id, first_name, last_name, email, phone, document_title, document_file, document_text, document_comments, special_requests) VALUES "
        return_str += f"({self.id},'{self.first_name}','{self.last_name}','{self.email}','{self.phone}','{self.document_title}',{self.document_file},'{self.document_text}',{document_comments},{special_requests})"

        return return_str


class Order(SQLModel):
    """Заказ"""

    @validate_arguments
    def __init__(
        self, id: int, order_date: datetime.datetime, client_id: int, cost: float = None
    ) -> None:
        self.id = id
        self.order_date = order_date.strftime("%Y-%m-%d %H:%M:%S")
        self.client_id = client_id
        self.cost = cost

    def insert(self) -> str:
        cost = self.cost
        if cost is None:
            cost = 0
        return f"INSERT INTO orders VALUES ({self.id},'{self.order_date}',{self.client_id},{cost})"

    def update(self) -> str:
        if self.cost is None:
            raise ValueError("Сначала необходимо выставить цену")
        return f"UPDATE orders SET cost={self.cost} WHERE id={self.id}"


class Product(SQLModel):
    @validate_arguments
    def __init__(self, id_: int, title: str, price: float) -> None:
        self.id = id_
        self.title = title
        self.price = price

    def insert(self) -> str:
        return f"INSERT INTO products VALUES ({self.id},'{self.title}',{self.price})"


class ProductCount(SQLModel):
    @validate_arguments
    def __init__(self, count: int, product_id: int, order_id: int):
        self.count = count
        self.product_id = product_id
        self.order_id = order_id

    def insert(self) -> str:
        return f"INSERT INTO products_count(count, product_id, order_id) VALUES ({self.count}, {self.product_id}, {self.order_id})"


class Staff(SQLModel):
    def __init__(
        self,
        id_: int,
        first_name: str,
        last_name: str,
        position: str,
        type_: str,
        phone: str,
    ) -> None:
        pass
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.type = type_
        self.phone = phone

    def insert(self) -> str:
        return f"INSERT INTO staffs(id, first_name, last_name, position, type, phone) VALUES ({self.id}, '{self.first_name}','{self.last_name}','{self.position}','{self.type}','{self.phone}')"


class Booking(SQLModel):
    @validate_arguments
    def __init__(
        self,
        id_: int,
        date_in: datetime.datetime,
        date_out: datetime.datetime,
        client_id: int,
        staff_id: int,
        cost: float = None,
    ) -> None:
        self.id = id_
        self.date_in = date_in
        self.date_out = date_out
        self.client_id = client_id
        self.staff_id = staff_id
        self.cost = cost

    def insert(self) -> str:
        cost = self.cost
        if cost is None:
            cost = 0
        return f"INSERT INTO bookings (id, date_in, date_out, cost, client_id, staff_id) VALUES ({self.id}, '{self.date_in}','{self.date_out}',{cost}, {self.client_id}, {self.staff_id})"

    def update(self) -> str:
        if self.cost is None:
            raise ValueError("Сначала необходимо выставить цену")
        return f"UPDATE bookings SET cost={self.cost} WHERE id={self.id}"
