"""
Реализовать создание, запись, чтение и удаление файла с данными о пользователе.
пользователь выбирает действие самостоятельно, а так же указывает путь к размещению файла.

Обработать ошибки

"""
import os
from random import randint


class MetaClass():
    def __init__(self):
        d = {
            0: AttributeError,
            1: IOError,
            2: IndexError,
            3: KeyError,
        }
        key = randint(0, 3)
        self.random_class = d[key]


class ExceptionClass(IndexError):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        print("ExceptionClass __str__")
        return self.description


class FileProcessing():
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
                "1. Добавление файла\n2. Удаление файла\n3. Чтение из файла\n4. Запись файла\n0. Выход\n-> ")
            try:
                select_d[input_str]()
            except KeyError:
                if input_str != "0":
                    print("Нет введёного пункта меню")

    def file_add(self):

        f = open(self.file_name, "w")
        f.close()

    def file_remove(self):
        try:
            os.remove(self.file_name)

            if self.random_riser():
                o = MetaClass()
                raise o.random_class("ну привет")

        except (IOError, OSError) as e:
            print("Ошибки удаления файла", e)
        except KeyError as e:
            print("KeyError:", e)
        except Exception as e:
            print("Вас посетила ошибка", type(e).__name__)

    def file_write(self):
        """
        Запись исходного выражения в файл
        """

        user_info = input("Введите строку для записи -> ")
        with open(self.file_name, "w") as f:
            f.write(user_info)

    def random_riser(self):
        """
        Метод для рандомной отдачи 1 или 0
        Необходим для выкидывания ошибки
        """
        return bool(randint(0, 1))

    def file_read(self):
        """
        Чтение файла self.file_name
        """
        try:
            with open(self.file_name, "r") as f:
                print(f.read())

            if self.random_riser():
                o = MetaClass()
                raise o.random_class("ну привет")

        except FileNotFoundError:
            print("Ошибка чтения файла. Файла не существует")
        except Exception as e:
            print("Вас посетила ошибка", type(e).__name__)


if __name__ == "__main__":
    try:
        FileProcessing()
        raise ExceptionClass("привет, я кастомная ошибка")
    except ExceptionClass as e:
        print(e)
    except KeyboardInterrupt:
        print("\nВыход из программы, удачи!")
