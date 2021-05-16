import json
import logging
import os
import pickle
import random
import socket
import sys
import threading
from json.decoder import JSONDecodeError
from typing import Dict, Union, Any

import sha3

from data_processing import DataProcessing
from file_module import FTPFileProcessing

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from validator import port_validation, check_port_open
from crypt_utils import DiffieHellman, FileCrypter

END_MESSAGE_FLAG = "CRLF_"
FILE_DETECT_FLAG = "DEMKA_FILE_STORAGE"
DEFAULT_PORT = 9090
LOGGER_FILE = "./logs/server.log"

# Настройки логирования
logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    handlers=[logging.FileHandler(LOGGER_FILE)],
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)


def hash(password: str) -> str:
    """Хеширование данных"""
    return sha3.sha3_224(password.encode("utf-8")).hexdigest()


class Server:
    """Класс с логикой сервера"""

    def __init__(self, port_number: int) -> None:

        logger.info(f"Запуск сервера..")
        self.port_number = port_number
        self.sock = None
        self.database = DataProcessing()
        self.socket_init()

        # Список авторизации
        self.authenticated_list = []
        self.authenticated_keys_dict = {}
        # Список ip, которым надо пройти регистрацию
        self.reg_list = []

        self.ip2username_dict = {}

        logger.info(f"Сервер инициализировался, слушает порт {port_number}")

        self.connection_thread = None
        self.play_command()

        self.input_processing()

    def connection_processing(self):
        """
        Метод ожидания подключений клиентов
        Запускается в отдельном потоке
        """
        # Ожидаем новое соединение
        while self.receive_data:
            # Новое соединение
            conn, addr = self.sock.accept()

            logger.info(f"Новое соединение от {addr[0]}")
            t = threading.Thread(target=self.server_router, args=(conn, addr))
            t.daemon = True
            t.start()

    def input_processing(self):
        """
        Метод ввода команд для управления сервером
        1. Отключение сервера (завершение программы);
        2. Пауза (остановка прослушивание порта);
        3. Показ логов;
        4. Очистка логов;
        5. Очистка файла идентификации.
        """
        commands_dict = {
            "exit": {"command": self.exit_command, "description": "Выход из программы"},
            "pause": {
                "command": self.stop_command,
                "description": "Приостановить получение новых соединений",
            },
            "stop": {
                "command": self.stop_command,
                "description": "Приостановить получение новых соединений",
            },
            "play": {
                "command": self.play_command,
                "description": "Продолжить получение новых соединений",
            },
            "start": {
                "command": self.play_command,
                "description": "Продолжить получение новых соединений",
            },
            "start logs": {
                "command": self.start_logs_command,
                "description": "Выводить логи в консоли",
            },
            "stop logs": {
                "command": self.stop_logs_command,
                "description": "Не выводить логи в консоли",
            },
            "clear auth": {
                "command": self.clear_auth_command,
                "description": "Отчистка файла для авторизации пользователей",
            },
            "clear logs": {
                "command": self.clear_logs_command,
                "description": "Отчистка файла логирования",
            },
        }

        while True:
            command_str = input()
            if command_str in commands_dict:
                commands_dict[command_str]["command"]()
            else:
                commands_str = "\n".join(
                    [f"{k} - {v['description']}" for k, v in commands_dict.items()]
                )
                print(f"Команда не найдена\nДоступные команды:\n{commands_str}")

    def exit_command(self):
        """Обработчик завершения работы сервера"""
        logger.info("Завершаем работу сервера")
        sys.exit()

    def stop_command(self):
        """Команда приостановки"""
        if self.connection_thread is None:
            raise ValueError(
                "Нельзя остановить поток подключений, если он не был запущен!"
            )
        self.receive_data = False
        logger.info("Приостановили поток получения данных клиентов")

    def clear_auth_command(self):
        """Отчистка файла авторизации"""
        self.database.clear()
        logger.info("Отчистили файл аворизации пользователей")

    def start_logs_command(self):
        """Показывает логи"""
        if stream_handler not in logger.handlers:
            logger.addHandler(stream_handler)
            logger.info("Возобновили показ логов в консоли")

    def stop_logs_command(self):
        """Стопает показ логов в консоли"""
        if stream_handler in logger.handlers:
            logger.removeHandler(stream_handler)
            logger.info("Приостановили показ логов в консоли")

    def clear_logs_command(self):
        """Отчистка файла логов"""
        open(LOGGER_FILE, "w").close()
        logger.info("Отчистили файл логов")

    def play_command(self):
        # Поток обработки подлючений от клиентов
        self.receive_data = True
        t = threading.Thread(target=self.connection_processing)
        t.daemon = True
        t.start()
        self.connection_thread = t

    def send_message(self, conn, data: Union[str, Dict[str, Any]], ip: str) -> None:
        """Отправка данных"""
        data_text = data
        if type(data) == dict:
            data = json.dumps(data, ensure_ascii=False)

        data += END_MESSAGE_FLAG

        if ip in self.authenticated_list:
            file_crypter = self.authenticated_keys_dict[ip]
            message_new = file_crypter.encryption(data)
            conn.send(pickle.dumps(message_new))
            logger.info(f"Сообщение {data_text} было отправлено клиенту {ip} в зашифрованном виде")
            logger.info(f"Шифрованное сообщение: {message_new}")
        else:
            conn.send(data.encode())
            logger.info(f"Сообщение {data_text} было отправлено клиенту {ip} в открытом виде")

    def socket_init(self):
        """Инициализация сокета"""
        sock = socket.socket()
        sock.bind(("", self.port_number))
        sock.listen(0)
        # Наш сокет
        self.sock = sock

    def new_event_logic(self, conn, client_ip):
        """
        Логика обработки новых событий, которые приходят с клиента
        """
        data = ""

        # Имя пользователя по его ip
        username = self.ip2username_dict[client_ip]
        # Экземпляр класса для работы с файлами конкретного пользователя
        userfiles_logic = FTPFileProcessing(username)

        while True:
            # Получаем данные и собираем их по кусочкам
            chunk = conn.recv(4096)

            # Если вообще ничего не пришло - это конец всего соединения
            if not chunk:
                break

            if client_ip in self.authenticated_list:
                data += self.authenticated_keys_dict[client_ip].encryption(pickle.loads(chunk))
            else:
                data += chunk.decode()
            # Если это конец сообщения, то значит, что мы все собрали и можем отдавать данные каждому соединению
            if END_MESSAGE_FLAG in data:

                data = data.replace(END_MESSAGE_FLAG, "")

                # Проверяем то, что это: файл или команда

                # Это файл
                if FILE_DETECT_FLAG in data:
                    logger.info(
                        f"Получили файл {data} от клиента {client_ip} ({username})"
                    )
                    # Записываем файл

                    file_name, file_content = data.split(FILE_DETECT_FLAG)
                    transfer_flag = userfiles_logic.client2server_transfer(
                        file_name, file_content
                    )
                    if transfer_flag:
                        out_data = {"result": True, "description": "file received"}
                    else:
                        out_data = {"result": False, "description": "file saving error"}
                    self.send_message(conn, out_data, client_ip)

                # Команда для получения файла пользователя с сервера
                elif "get" in data:

                    description, is_result = userfiles_logic.server2client_transfer(
                        data
                    )
                    out_data = {"result": is_result, "description": description}
                    self.send_message(conn, out_data, client_ip)

                # Это одна из стандартных команд FTPFileProcessing
                else:

                    logger.info(
                        f"Получили команду {data} от клиента {client_ip} ({username})"
                    )

                    command = data.split(" ")

                    # Остановка работы программы
                    if command[0] == "exit":
                        break

                    # Получаем результат существования команды
                    result = userfiles_logic.router(command[0])

                    out_data = {"result": None, "description": None}

                    # Если есть такая команда
                    if result:
                        try:
                            description_str = result(*command[1:])
                            out_data = {"result": True, "description": description_str}

                        except TypeError:
                            description_str = f"Команда {command[0]} была вызвана с некорректными аргументами"
                            out_data = {"result": False, "description": description_str}
                    else:
                        commands_str = "\n".join(
                            [
                                f"{key} - {value}"
                                for (
                                key,
                                value,
                            ) in userfiles_logic.get_commands().items()
                            ]
                        )
                        description_str = f"Команда {command[0]} не найдена! Список команд:\n{commands_str}"
                        out_data = {"result": False, "description": description_str}

                    self.send_message(conn, out_data, client_ip)

                # Обнуляем буфер сообщений
                data = ""

            # Значит пришла только часть большого сообщения
            else:
                logger.info(f"Приняли часть данных от клиента {client_ip}: '{data}'")

    def reg_logic(self, conn, addr):
        """
        Логика регистрации пользователя
        """
        newuser_ip = addr[0]
        try:
            data = json.loads(conn.recv(4096).decode())
        except JSONDecodeError:
            if newuser_ip in self.reg_list:
                self.reg_list.remove(newuser_ip)
            return
        newuser_password, newuser_username = hash(data["password"]), data["username"]
        p, g, A = data["keys"]
        encryption = DiffieHellman(a=A, p=p, g=g)

        server_mixed_key = encryption.mixed_key
        newuser_key = encryption.generate_key(server_mixed_key)

        self.database.user_reg(newuser_ip, newuser_password, newuser_username, newuser_key)
        logger.info(f"Клиент {newuser_ip} -> регистрация прошла успешно")
        create_flag = FTPFileProcessing.new_user_reg(newuser_username)
        if create_flag:
            logger.info(
                f"Клиент {newuser_ip} -> создали root-директорию {newuser_username}"
            )
        else:
            logger.error(
                f"Клиент {newuser_ip} -> не удалось создать root-директорию {newuser_username}"
            )

        data = {"result": True}
        if newuser_ip in self.reg_list:
            self.reg_list.remove(newuser_ip)
            logger.info(f"Удалили клиента {newuser_ip} из списка регистрации")

        self.send_message(conn, data, newuser_ip)
        logger.info(f"Клиент {newuser_ip}. Отправили данные о результате регистрации")

    def auth_logic(self, conn, addr):
        """
        Логика авторизации клиента
        Запрос авторизации у нас априори меньше 4096, так что никакой цикл не запускаем
        """
        try:
            user_password = hash(json.loads(conn.recv(4096).decode())["password"])
        except JSONDecodeError:
            return
        client_ip = addr[0]

        # Проверяем на существование данных
        auth_result, username, key = self.database.user_auth(client_ip, user_password)

        # Если авторизация прошла успешно
        if auth_result == 1:
            logger.info(f"Клиент {client_ip} -> авторизация прошла успешно")
            data = {"result": True, "body": {"username": username}}

        # Если авторизация не удалась, но пользователь с таким ip существует
        elif auth_result == 0:
            logger.info(f"Клиент {client_ip} -> авторизация не удалась")
            data = {"result": False, "description": "wrong auth"}
        # Если пользователя с таким ip не существует, то необходима регистрация
        else:
            logger.info(
                f"Клиент {client_ip} -> необходима предварительная регистрация в системе"
            )
            data = {"result": False, "description": "registration required"}
            if client_ip not in self.reg_list:
                self.reg_list.append(client_ip)
                logger.info(f"Добавили клиента {client_ip} в список регистрации")

        self.send_message(conn, data, client_ip)
        logger.info(f"Клиент {client_ip}. Отправили данные о результате авторизации")

        # Если была успешная авторизация - принимаем последующие сообщения от пользователя
        if auth_result == 1:
            if client_ip not in self.authenticated_list:
                self.authenticated_list.append(client_ip)
                self.ip2username_dict[client_ip] = username
                self.authenticated_keys_dict[client_ip] = FileCrypter(key)
                logger.info(f"Добавили клиента {client_ip} в список авторизации")
            self.new_event_logic(conn, client_ip)

    def server_router(self, conn, addr):
        """
        Роутинг в зависимости от авторизации клиента
        """
        logger.info("Server router работает в отдельном потоке!")
        client_ip = addr[0]

        # Если клиенту нужна авторизация
        if client_ip in self.reg_list:
            self.reg_logic(conn, addr)

        # Если ip не авторизован - надо авторизовать
        elif client_ip not in self.authenticated_list:
            self.auth_logic(conn, addr)

        # Если уже был авторизован
        else:
            self.new_event_logic(conn, client_ip)

        logger.info(f"Отключение клиента {client_ip}")
        # Если клиент был в списке авторизации - удаляем его
        if client_ip in self.authenticated_list:
            self.authenticated_list.remove(client_ip)
            del self.ip2username_dict[client_ip]
            del self.authenticated_keys_dict[client_ip]
            logger.info(f"Удалили клиента {client_ip} из списка авторизации")

    def __del__(self):
        logger.info(f"Остановка сервера")


def main():
    port_input = input("Введите номер порта для сервера -> ")
    # Тут проверка на то, занят ли порт
    port_flag = port_validation(port_input, check_open=True)

    if not port_flag:

        # Если порт по-умолчанию уже занят, то перебираем свободные порты
        if not check_port_open(DEFAULT_PORT):
            print(
                f"Порт по умолчанию {DEFAULT_PORT} уже занят! Подбираем рандомный порт.."
            )
            stop_flag = False
            while not stop_flag:
                current_port = random.randint(49152, 65535)
                print(f"Сгенерировали рандомный порт {current_port}")
                stop_flag = check_port_open(current_port)

            port_input = current_port
        else:
            port_input = DEFAULT_PORT
        print(f"Выставили порт {port_input} по умолчанию")

    server = Server(int(port_input))


if __name__ == "__main__":
    main()
