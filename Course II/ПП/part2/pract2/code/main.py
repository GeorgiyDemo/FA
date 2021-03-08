import os
import shutil
import pathlib
from typing import Dict


class Colors:
    """Хранение цветов"""
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class PathStorage:
    """Хранение информации о пути"""

    def __init__(self) -> None:
        self.__storage = ["storage"]

    def add_path(self, path: str) -> None:
        """Добавляет файл в иерархию каталогов"""
        # Если хотим выйти на уровень выше
        if ".." in path and len(self.__storage) != 1:
            self.__storage.pop(-1)
        # Если хотим выйти за пределы выдуманного мира
        elif ".." in path:
            print("Вы хотите выйти за пределы песочницы!")
        # Значит хотим перейти на уровень ниже
        else:
            self.__storage.append(path)

    def file2path(self, file_name: str) -> str:
        """Возвращает указанный файл в текущей иерархии каталогов"""
        locale_storage = self.__storage.copy()
        locale_storage.append(file_name)
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + "/" + "/".join(locale_storage)

    @property
    def path(self):
        """Возвращает текущую иерархию каталогов"""
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + "/" + "/".join(self.__storage)

    @property
    def upper_path(self):
        """Возвращает директорию выше текущей"""
        abs_path = pathlib.Path(__file__).parent.absolute()
        print(self.__storage[1:])
        return str(abs_path) + "/" + "/".join(self.__storage[:1])


class FileProcessing:
    """Работа с файлами"""

    @staticmethod
    def get_commands() -> Dict[str, str]:
        """Получает список всех команд"""

        commands_dict = {
            "cd": "Перемещение между папками",
            "ls": "Вывод содержимого текущей папки на экран",
            "mkdir": "Создание папки",
            "rmdir": "Удаление папки",
            "create": "Создание файла",
            "rename": "Переименование файла/папки",
            "read": "Чтение файла",
            "remove": "Удаление файла",
            "copy": "Копирование файла/папки",
            "move": "Перемещение файла/папки",
            "write": "Запись в файл",
        }

        return commands_dict

    def __init__(self) -> None:
        self.storage = PathStorage()

    def mkdir(self, filename: str):
        """Создание папки (с указанием имени)"""
        current_path = self.storage.file2path(filename)
        try:
            os.mkdir(current_path)
        except FileNotFoundError:
            os.makedirs(current_path)
        except FileExistsError:
            print(f"Директория {filename} уже существует")

    def rmdir(self, filename: str):
        """Удаление папки по имени"""
        current_path = self.storage.file2path(filename)
        try:
            os.rmdir(current_path)
        except OSError:
            try:
                shutil.rmtree(current_path, ignore_errors=False, onerror=None)
            except FileNotFoundError:
                print(f"Директории {filename} не существует")
            except NotADirectoryError:
                print(f"Файл {filename} не является директорией")
        except FileNotFoundError:
            print(f"Директории {filename} не существует")
        except NotADirectoryError:
            print(f"Файл {filename} не является директорией")

    def cd(self, filename: str):
        """
        Перемещение между папками

        - заход в папку по имени
        - выход на уровень вверх
        - в пределах рабочей папки
        """
        self.storage.add_path(filename)
        current_path = self.storage.path

        try:
            os.chdir(current_path)
        except FileNotFoundError:
            self.storage.add_path("../")
            print(f"Директории {filename} не существует")
        except NotADirectoryError:
            self.storage.add_path("../")
            print(f"Файл {filename} не является директорией")

    def ls(self):
        """
        Вывод содержимого текущей директории на экран
        """
        current_path = self.storage.path
        filelist = os.listdir(current_path)
        for i in range(len(filelist)):
            if os.path.isdir(self.storage.file2path(filelist[i])):
                filelist[i] = f"[dir] {Colors.OKCYAN}{filelist[i]}{Colors.ENDC}"
            elif os.path.isfile(self.storage.file2path(filelist[i])):
                filelist[i] = f"[file] {Colors.WARNING}{filelist[i]}{Colors.ENDC}"

        r = "\n".join(filelist)
        print(f"Содержимое {current_path}:\n{r}")

    def touch(self, filename: str):
        """Создание пустых файлов с указанием имени"""
        current_path = self.storage.file2path(filename)
        try:
            open(current_path, "a").close()
        except IsADirectoryError:
            print(f"Файл {filename} уже был создан и это директория")

    def cat(self, filename: str) -> str:
        """Просмотр содержимого текстового файла"""
        current_path = self.storage.file2path(filename)
        try:
            with open(current_path, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        except IsADirectoryError:
            print(f"Файл {filename} является директорией")

    def rename(self, filename_old: str, filename_new: str):
        """Переименование файлов"""

        path_old = self.storage.file2path(filename_old)
        path_new = self.storage.file2path(filename_new)

        # Проверка на то, чтоб файл с новым именем не существовал
        try:
            if not os.path.isfile(path_new):
                os.rename(path_old, path_new)
            else:
                raise IsADirectoryError
        except FileNotFoundError:
            print(f"Указанного файла {filename_old} не существует")
        except IsADirectoryError:
            print(f"Файл с названием {filename_new} уже существует")

    def rm(self, filename: str):
        """Удаление файлов по имени"""
        path = self.storage.file2path(filename)
        if os.path.isfile(path):
            os.remove(path)
        else:
            print(f"Файла {filename} не существует")

    # TODO копирование директории на одном уровне
    def cp(self, filename: str, path: str):
        """Копирование файлов из одной папки в другую"""
        path_old = self.storage.file2path(filename)
        # Копирование на уровень выше
        if ".." in path:
            path_new = self.storage.upper_path + "/" + filename
        else:
            # Проверяем на то, что это за тип файла
            buff = self.storage.file2path(path)

            # Если конечный путь папка - закидываем туда файл
            if os.path.isdir(buff):
                path_new = self.storage.file2path(path + "/" + filename)
            else:
                # Значит это копирование на одном уровне
                path_new = self.storage.file2path(path)
        try:
            shutil.copyfile(path_old, path_new)
        # Если это директория - копируем директорию
        except IsADirectoryError:
            shutil.copytree(path_old, path_new)
        except FileNotFoundError:
            print(f"Файл {filename} не найден")

    def mv(self, filename: str, path: str):
        """Перемещение файлов"""
        path_old = self.storage.file2path(filename)
        if ".." in path:
            path_new = self.storage.upper_path + "/" + filename
        else:
            # Проверяем на то, что это за тип файла
            buff = self.storage.file2path(path)
            # Если директория - закидываем туда файл
            if os.path.isdir(buff):
                path_new = self.storage.file2path(path + "/" + filename)
            else:
                # Значит это перемещение на одном уровне
                path_new = self.storage.file2path(path)
        try:
            shutil.move(path_old, path_new)
        except FileNotFoundError:
            print(f"Файл {filename} не найден")

    def write(self, filename: str, *data: str):
        """Запись текста в файл"""
        text = " ".join(data)
        path = self.storage.file2path(filename)
        try:
            with open(path, "a") as file:
                file.write(text)
        except IsADirectoryError:
            print(f"Указанный файл {filename} является директорией")

    def router(self, command: str):
        """Ассоциация между командами и методами FileProcessing"""

        commands = [
            self.cd,
            self.ls,
            self.mkdir,
            self.rmdir,
            self.touch,
            self.rename,
            self.cat,
            self.rm,
            self.cp,
            self.mv,
            self.write,
        ]
        item_dict = dict(zip(FileProcessing.get_commands().keys(), commands))
        return item_dict.get(command, None)


def main():
    # Экземпляр обработчика файлов
    file_processing = FileProcessing()

    while True:

        command = input("\nВведите команду -> ").split(" ")

        # Остановка работы программы
        if command[0] == "exit":
            break

        # Получаем результат существования команды
        result = file_processing.router(command[0])
        # Если есть такая команда
        if result:
            try:
                result(*command[1:])
            except TypeError:
                print(f"Команда {command[0]} была вызвана с некорректными аргументами")

        else:
            commands_str = "\n".join(
                [
                    f"{Colors.OKGREEN}{key}{Colors.ENDC} - {value}"
                    for (key, value) in FileProcessing.get_commands().items()
                ]
            )
            print(f"Команда {command[0]} не найдена! Список команд:\n{commands_str}")

    print("Произведен выход из программы.")


if __name__ == "__main__":
    main()
