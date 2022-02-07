"""
Реализовать создание, запись, чтение и удаление файла с данными о пользователе.
пользователь выбирает действие самостоятельно, а так же указывает путь к размещению файла.
"""
import os


class FileProcessing:
    def __init__(self):

        select_d = {
            "1": self.file_add,
            "2": self.file_remove,
            "3": self.file_read,
            "4": self.file_write,
        }

        self.file_name = input("Введите название файла для записи -> ")
        input_str = ""
        while input_str != "0":
            input_str = input(
                "1. Добавление файла\n2. Удаление файла\n3. Чтение из файла\n4. Запись файла\n0. Выход\n-> "
            )
            if input_str in select_d:
                select_d[input_str]()
            elif input_str != "0":
                print("Нет введёного пункта меню")

    def file_add(self):
        f = open(self.file_name, "w")
        f.close()

    def file_remove(self):
        os.remove(self.file_name)

    def file_write(self):
        """
        Запись исходного выражения в файл
        """

        user_info = input("Введите строку для записи -> ")
        with open(self.file_name, "w") as f:
            f.write(user_info)

    def file_read(self):
        """
        Чтение файла self.file_name
        """
        try:
            with open(self.file_name, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("Ошибка чтения файла. Файла не существует")


if __name__ == "__main__":
    FileProcessing()
