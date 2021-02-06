import pymysql.cursors
from typing import Dict, Tuple, Union, List


class MySQLConnector:
    def __init__(self, params: Dict) -> None:
        self.connection = pymysql.connect(**params)

    def write(self, sql_command: str) -> None:
        """Запись данных"""
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        self.connection.commit()

    def fetch(self, sql_command: str) -> Union[Tuple, List[Dict]]:
        """Получение данных"""
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


def main():

    HOST = "127.0.0.1"
    USER = ""
    PASSWORD = ""
    DB = "CONTROL_FA"

    locale_dict = {
        "host": HOST,
        "user": USER,
        "password": PASSWORD,
        "db": DB,
        "cursorclass": pymysql.cursors.DictCursor,
    }
    connection = MySQLConnector(locale_dict)

    result = connection.fetch("SELECT * FROM CLIENTS")


if __name__ == "__main__":
    main()
