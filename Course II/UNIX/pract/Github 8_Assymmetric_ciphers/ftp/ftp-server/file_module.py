import base64
import os
import pathlib
import shutil
from typing import Dict, Tuple

MAIN_STORAGE_DIR = "storage"
FILE_DETECT_FLAG = "DEMKA_FILE_STORAGE"


class PathStorage:
    """Хранение информации о пути"""

    def __init__(self, sep: str, username: str) -> None:
        self.sep = sep
        self.username = username
        self.__storage = [MAIN_STORAGE_DIR, username]

    def add_path(self, path: str) -> None:
        """Добавляет файл в иерархию каталогов"""
        # Если хотим выйти на уровень выше
        if ".." in path and len(self.__storage) != 2:
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
        return str(abs_path) + self.sep + self.sep.join(locale_storage)

    @property
    def path(self):
        """Возвращает текущую иерархию каталогов"""
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(self.__storage)

    @property
    def upper_path(self):
        """Возвращает директорию выше текущей"""
        abs_path = pathlib.Path(__file__).parent.absolute()
        print(self.__storage[1:])
        return str(abs_path) + self.sep + self.sep.join(self.__storage[:1])


class FTPFileProcessing:
    """Работа с файлами"""

    @staticmethod
    def new_user_reg(username: str) -> bool:
        """Создание директории зарегистрированного пользоввателя"""
        current_path = [MAIN_STORAGE_DIR, username]
        path_str = os.sep.join(current_path)
        try:
            os.mkdir(path_str)
        except FileNotFoundError:
            os.makedirs(path_str)
        except FileExistsError:
            return False
        return True

    @staticmethod
    def get_commands() -> Dict[str, str]:
        """Получает список всех команд"""

        commands_dict = {
            "cd": "Перемещение между папками",
            "ls": "Вывод содержимого текущей папки на экран",
            "mkdir": "Создание папки",
            "rmdir": "Удаление папки",
            "touch": "Создание файла",
            "rename": "Переименование файла/папки",
            "cat": "Чтение файла",
            "remove": "Удаление файла",
            "cp": "Копирование файла/папки",
            "mv": "Перемещение файла/папки",
            "write": "Запись в файл",
        }

        return commands_dict

    def __init__(self, username: str) -> None:
        self.sep = os.sep
        self.username = username
        self.storage = PathStorage(self.sep, username)

    def client2server_transfer(self, file_name: str, file_content: str) -> bool:
        """Логика копирования файла с клиента на сервер"""
        current_path = self.storage.file2path(file_name)
        try:
            content = base64.b64decode(file_content)
            with open(current_path, "w+") as f:
                f.write(content.decode("utf-8"))
            return True
        except Exception as e:
            print(str(e))
            return False

    def server2client_transfer(self, msg_path: str) -> Tuple[str, bool]:
        """
        Метод для чтения и энкодинга файла с патча в набор байтов
        Нужен для передачи файла с сервера на клент
        """
        is_error = True
        content = ""
        try:
            filename = msg_path.split(" ")[1]
            current_path = self.storage.file2path(filename)
            try:
                with open(current_path, "rb") as file:
                    content = (
                            filename
                            + FILE_DETECT_FLAG
                            + base64.b64encode(file.read()).decode("utf-8")
                    )
                    is_error = False

            except IsADirectoryError:
                content = f"Файл {filename} является директорией"

        # Если не удалось обработать патч
        except (ValueError, FileNotFoundError, IndexError, IsADirectoryError):

            filelist = os.listdir(self.storage.path)
            r = "\n".join(filelist)
            content = f"\nЧто-то пошло не так при копировании файла с клиента на сервер.\nДоступные файлы в локальной директории {self.storage.path}:\n{r}"

        return content, not is_error

    def mkdir(self, filename: str) -> str:
        """Создание папки (с указанием имени)"""
        result_str = ""
        current_path = self.storage.file2path(filename)
        try:
            os.mkdir(current_path)
        except FileNotFoundError:
            os.makedirs(current_path)
        except FileExistsError:
            result_str = f"Директория {filename} уже существует"
        return result_str

    def rmdir(self, filename: str) -> str:
        """Удаление папки по имени"""
        result_str = ""
        current_path = self.storage.file2path(filename)
        try:
            os.rmdir(current_path)
        except OSError:
            try:
                shutil.rmtree(current_path, ignore_errors=False, onerror=None)
            except FileNotFoundError:
                result_str = f"Директории {filename} не существует"
            except NotADirectoryError:
                result_str = f"Файл {filename} не является директорией"
        except FileNotFoundError:
            result_str = f"Директории {filename} не существует"
        except NotADirectoryError:
            result_str = f"Файл {filename} не является директорией"

        return result_str

    def cd(self, filename: str) -> str:
        """
        Перемещение между папками

        - заход в папку по имени
        - выход на уровень вверх
        - в пределах рабочей папки
        """
        result_str = ""
        self.storage.add_path(filename)
        current_path = self.storage.path

        try:
            os.chdir(current_path)
        except FileNotFoundError:
            self.storage.add_path(f"..{self.sep}")
            result_str = f"Директории {filename} не существует"
        except NotADirectoryError:
            self.storage.add_path(f"..{self.sep}")
            result_str = f"Файл {filename} не является директорией"

        return result_str

    def ls(self) -> str:
        """
        Вывод содержимого текущей директории на экран
        """
        current_path = self.storage.path
        filelist = os.listdir(current_path)
        for i in range(len(filelist)):
            if os.path.isdir(self.storage.file2path(filelist[i])):
                filelist[i] = f"[dir] {filelist[i]}"
            elif os.path.isfile(self.storage.file2path(filelist[i])):
                filelist[i] = f"[file] {filelist[i]}"

        r = "\n".join(filelist)
        return f"Содержимое {current_path}:\n{r}"

    def touch(self, filename: str) -> str:
        """Создание пустых файлов с указанием имени"""
        result_str = ""
        current_path = self.storage.file2path(filename)
        try:
            open(current_path, "a").close()
        except IsADirectoryError:
            result_str = f"Файл {filename} уже был создан и это директория"
        return result_str

    def cat(self, filename: str) -> str:
        """Просмотр содержимого текстового файла"""
        result_str = ""
        current_path = self.storage.file2path(filename)
        try:
            with open(current_path, "r") as file:
                result_str = file.read()
        except FileNotFoundError:
            result_str = f"Файл {filename} не найден"
        except IsADirectoryError:
            result_str = f"Файл {filename} является директорией"
        return result_str

    def rename(self, filename_old: str, filename_new: str) -> str:
        """Переименование файлов"""
        result_str = ""
        path_old = self.storage.file2path(filename_old)
        path_new = self.storage.file2path(filename_new)

        # Проверка на то, чтоб файл с новым именем не существовал
        try:
            if not os.path.isfile(path_new):
                os.rename(path_old, path_new)
            else:
                raise IsADirectoryError
        except FileNotFoundError:
            result_str = f"Указанного файла {filename_old} не существует"
        except IsADirectoryError:
            result_str = f"Файл с названием {filename_new} уже существует"
        return result_str

    def rm(self, filename: str) -> str:
        """Удаление файлов по имени"""
        result_str = ""
        path = self.storage.file2path(filename)
        if os.path.isfile(path):
            os.remove(path)
        else:
            result_str = f"Файла {filename} не существует"
        return result_str

    def cp(self, filename: str, path: str) -> str:
        """Копирование файлов из одной папки в другую"""
        result_str = ""
        path_old = self.storage.file2path(filename)
        # Копирование на уровень выше
        if ".." in path:
            path_new = self.storage.upper_path + self.sep + filename
        else:
            # Проверяем на то, что это за тип файла
            buff = self.storage.file2path(path)

            # Если конечный путь папка - закидываем туда файл
            if os.path.isdir(buff):
                path_new = self.storage.file2path(path + self.sep + filename)
            else:
                # Значит это копирование на одном уровне
                path_new = self.storage.file2path(path)
        try:
            shutil.copyfile(path_old, path_new)
        # Если это директория - копируем директорию
        except IsADirectoryError:
            shutil.copytree(path_old, path_new)
        except FileNotFoundError:
            result_str = f"Файл {filename} не найден"
        return result_str

    def mv(self, filename: str, path: str) -> str:
        """Перемещение файлов"""
        result_str = ""
        path_old = self.storage.file2path(filename)
        if ".." in path:
            path_new = self.storage.upper_path + self.sep + filename
        else:
            # Проверяем на то, что это за тип файла
            buff = self.storage.file2path(path)
            # Если директория - закидываем туда файл
            if os.path.isdir(buff):
                path_new = self.storage.file2path(path + self.sep + filename)
            else:
                # Значит это перемещение на одном уровне
                path_new = self.storage.file2path(path)
        try:
            shutil.move(path_old, path_new)
        except FileNotFoundError:
            result_str = f"Файл {filename} не найден"
        return result_str

    def write(self, filename: str, *data: str) -> str:
        """Запись текста в файл"""
        result_str = ""
        text = " ".join(data)
        path = self.storage.file2path(filename)
        try:
            with open(path, "a") as file:
                file.write(text)
        except IsADirectoryError:
            result_str = f"Указанный файл {filename} является директорией"
        return result_str

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
        item_dict = dict(zip(FTPFileProcessing.get_commands().keys(), commands))
        return item_dict.get(command, None)
