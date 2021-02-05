from abc import ABCMeta, abstractmethod

class SQLModel(metaclass=ABCMeta):
    @abstractmethod
    def to_sql(self) -> str:
        pass

    def __str__(self):
        return str(self.__dict__)

class House(SQLModel):
    def __init__(self, id : int, name : str, price : float, ac : int, tv : int, safe : int, description : str = None, _type: str = None) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.ac = ac
        self.tv = tv
        self.safe = safe
        self.description = description
        self.type = _type

    def to_sql(self) -> str:
        return f"INSERT INTO houses (id, name, price, ac, tv, safe, description, type) VALUES ('{self.id}','{self.name}',{self.price},{self.ac},{self.tv},{self.safe},'{self.description}','{self.type}')"
