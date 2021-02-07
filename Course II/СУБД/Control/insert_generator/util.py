"""Отдельный модуль с фуекциями-утилитами для генерации"""
import random
from typing import Any, List, Tuple
from faker import Faker
import datetime


class СircleCollection:
    def __init__(self, data: List[Any] = []) -> None:
        self.data = data
        self._index = 0

    def get(self) -> Any:
        if self._index == len(self.data):
            self._index = 0
        item = self.data[self._index]
        self._index += 1
        return item

    def put(self, value: Any) -> None:
        self.data.append(value)

    def __str__(self) -> str:
        return f"Элементы СircleCollection:\n{self.data}"


class RandomData:
    def __init__(self) -> None:
        self.fake_ru = Faker("ru_RU")
        self.fake_en = Faker("en_GB")

    def get_number_range(self, n) -> str:
        """Отдает n рандомных цифр"""

        result = ""
        for _ in range(n):
            result += str(random.choice(range(10)))
        return result

    def get_random_name(self) -> Tuple:
        """Возвращает рандомное русское/английское имя"""

        names_list = [
            self.fake_ru.name().replace("'", "").split(" "),
            self.fake_en.name().replace("'", "").split(" "),
        ]
        current_name_list = random.choice(names_list)
        if len(current_name_list) == 4:
            _, first_name, last_name, _ = current_name_list
        elif len(current_name_list) == 3:
            first_name, _, last_name = current_name_list
        else:
            first_name, last_name = current_name_list
        return (first_name, last_name)

    def data_range_generator(self) -> Tuple:
        """Генератор дат для бронирования"""
        date_in = self.fake_ru.date_time_between(start_date="-2y", end_date="now")
        date_out = date_in + datetime.timedelta(days=random.randint(1, 25))
        return date_in, date_out


if __name__ == "__main__":

    check_list = list([8] * 5)
    round_collection = СircleCollection(check_list)
    for i in range(20):
        print(round_collection.get())
    print(round_collection)

    round_collection = СircleCollection()
    for i in range(5):
        round_collection.put(i)
        round_collection.put(999)
    print(round_collection)
    for i in range(100):
        print(round_collection.get())

    random_data = RandomData()
    date_in, date_out = random_data.data_range_generator()
    print("Дата заезда:", date_in)
    print("Дата выезда:", date_out)

    days = date_out - date_in
    days = days.days
    print(days)
    print(type(days))
