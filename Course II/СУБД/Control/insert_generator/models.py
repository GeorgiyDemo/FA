from abc import ABCMeta, abstractmethod

class SQLModel(metaclass=ABCMeta):
    @abstractmethod
    def to_sql(self) -> str:
        pass

    def __str__(self):
        return str(self.__dict__)

class House(SQLModel):
    """Дом"""
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
    def __init__(self, id : int, first_name : str, last_name : str, email : str, phone : str, document_title : str, document_file : bytearray, document_text : str, document_comments : str = None, special_requests : str = None):
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
