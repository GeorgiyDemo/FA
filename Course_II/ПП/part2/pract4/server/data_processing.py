from typing import Tuple, Union

import yaml


class DataProcessing:
    """Класс для работы с коллекцией пользователей в yaml"""

    def __init__(self) -> None:
        self.file_path = "./data/users.yml"
        self.data = []
        self.read_collection()

    def read_collection(self):
        """Чтение данных с файла в self.data"""
        with open(self.file_path, "r") as stream:
            data = yaml.safe_load(stream)
            if data is None:
                data = []
            self.data = data

    def write_collection(self):
        """Запись данных с self.data в файл"""
        with open(self.file_path, "w") as stream:
            yaml.dump(self.data, stream)

    def user_auth(self, ip: str, password: str) -> Tuple[int, Union[str, None]]:
        """
        Метод авторизации пользователя в системе

        1 - авторизация прошла успешно
        0 - авторизация неудачная
        -1 - необходима регистрация пользователя
        """
        for user in self.data:
            if user["ip_addr"] == ip and user["password"] == password:
                return 1, user["username"]

        for user in self.data:
            if user["ip_addr"] == ip:
                return 0, None

        return -1, None

    def user_reg(self, ip: str, password: str, username: str) -> None:
        """Метод регистрации пользователей"""
        self.data.append({"ip_addr": ip, "password": password, "username": username})
        self.write_collection()

    def clear(self):
        """Отчищает файл авторизации от всех записей"""
        self.data = []
        self.write_collection()
