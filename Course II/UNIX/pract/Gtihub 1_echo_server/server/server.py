import json
import logging
import random
import socket
import threading
from typing import Dict, Union, Any

import sha3

from data_processing import DataProcessing
from server_validator import port_validation, check_port_open

END_MESSAGE_FLAG = "CRLF"
DEFAULT_PORT = 9090

# Настройки логирования
logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    handlers=[logging.FileHandler("./logs/server.log"), logging.StreamHandler()],
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def hash(password: str) -> str:
    """Хеширование данных"""
    return sha3.sha3_224(password.encode("utf-8")).hexdigest()


class Server:
    def __init__(self, port_number: int) -> None:

        logging.info(f"Запуск сервера..")
        self.port_number = port_number
        self.sock = None
        self.database = DataProcessing()
        self.socket_init()

        # Список авторизации
        self.authenticated_list = []
        # Список ip, которым надо пройти регистрацию
        self.reg_list = []
        # Список соединений, по которым рассылаются сообщения
        self.connections_list = []

        self.ip2username_dict = {}
        logging.info(f"Сервер инициализировался, слушает порт {port_number}")

        # Ожидаем новое соединение
        while True:
            # Новое соединение
            conn, addr = self.sock.accept()

            # Добавляем новое соединение
            self.connections_list.append((conn, addr))
            logging.info(f"Новое соединение от {addr[0]}")
            t = threading.Thread(target=self.router, args=(conn, addr))
            t.daemon = True
            t.start()

    def send_message(self, conn, data: Union[str, Dict[str, Any]], ip: str) -> None:
        """Отправка данных"""
        data_text = data
        if type(data) == dict:
            data = json.dumps(data, ensure_ascii=False)

        data = data.encode()
        conn.send(data)
        logging.info(f"Сообщение {data_text} было отправлено клиенту {ip}")

    def socket_init(self):
        """Инициализация сокета"""
        sock = socket.socket()
        sock.bind(("", self.port_number))
        sock.listen(0)
        # Наш сокет
        self.sock = sock

    def message_logic(self, conn, client_ip):
        """
        Получение сообщений
        """
        data = ""
        while True:
            # Получаем данные и собираем их по кусочкам
            chunk = conn.recv(1024)
            data += chunk.decode()

            # Если это конец сообщения, то значит, что мы все собрали и можем отдавать данные каждому соединению
            if END_MESSAGE_FLAG in data:

                username = self.ip2username_dict[client_ip]
                logging.info(
                    f"Получили сообщение {data} от клиента {client_ip} ({username})"
                )
                data = {"username": username, "text": data}

                # Рассылка по каждому соединению
                logger.info(
                    f"Текущее кол-во подключений к серверу: {len(self.connections_list)}"
                )
                for connection in self.connections_list:
                    current_conn, current_ip = connection
                    try:
                        self.send_message(current_conn, data, current_ip)
                    # Если вдруг у нас появилсоь соедиение, которое уже неактивно
                    except BrokenPipeError:
                        continue

                # Обнуляемся
                data = ""

            # Значит пришла только часть большого сообщения
            else:
                logger.info(f"Приняли часть данных от клиента {client_ip}: '{data}'")

            # Если вообще ничего не пришло - это конец всего соединения
            if not chunk:
                break

    def reg_logic(self, conn, addr):
        """
        Логика регистрации пользователя
        """
        data = json.loads(conn.recv(1024).decode())
        newuser_password, newuser_username = hash(data["password"]), data["username"]
        newuser_ip = addr[0]
        self.database.user_reg(newuser_ip, newuser_password, newuser_username)
        logger.info(f"Клиент {newuser_ip} -> регистрация прошла успешно")
        data = {"result": True}
        if newuser_ip in self.reg_list:
            self.reg_list.remove(newuser_ip)
            logging.info(f"Удалили клиента {newuser_ip} из списка регистрации")

        self.send_message(conn, data, newuser_ip)
        logger.info(f"Клиент {newuser_ip}. Отправили данные о результате регистрации")

    def auth_logic(self, conn, addr):
        """
        Логика авторизации клиента
        Запрос авторизации у нас априори меньше 1024, так что никакой цикл не запускаем
        """
        user_password = hash(json.loads(conn.recv(1024).decode())["password"])
        client_ip = addr[0]

        # Проверяем на существование данных
        auth_result, username = self.database.user_auth(client_ip, user_password)

        # Если авторизация прошла успешно
        if auth_result == 1:
            logger.info(f"Клиент {client_ip} -> авторизация прошла успешно")
            data = {"result": True, "body": {"username": username}}
            if client_ip not in self.authenticated_list:
                self.authenticated_list.append(client_ip)
                self.ip2username_dict[client_ip] = username
                logging.info(f"Добавили клиента {client_ip} в список авторизации")
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
                logging.info(f"Добавили клиента {client_ip} в список регистрации")

        self.send_message(conn, data, client_ip)
        logger.info(f"Клиент {client_ip}. Отправили данные о результате авторизации")

        # Если была успешная авторизация - принимаем последующие сообщения от пользователя
        if auth_result == 1:
            self.message_logic(conn, client_ip)

    def router(self, conn, addr):
        """
        Роутинг в зависимости от авторизации клиента
        """
        logger.info("Router работает в отдельном потоке!")
        client_ip = addr[0]

        # Если клиенту нужна авторизация
        if client_ip in self.reg_list:
            self.reg_logic(conn, addr)

        # Если ip не авторизован - надо авторизовать
        elif client_ip not in self.authenticated_list:
            self.auth_logic(conn, addr)

        # Если уже был авторизован
        else:
            self.message_logic(conn, client_ip)

        logging.info(f"Отключение клиента {client_ip}")
        self.connections_list.remove((conn, addr))
        # Если клиент был в списке авторизации - удаляем его
        if client_ip in self.authenticated_list:
            self.authenticated_list.remove(client_ip)
            print("Список соединений:")
            print(self.connections_list)
            logging.info(f"Удалили клиента {client_ip} из списка авторизации")

    def __del__(self):
        logging.info(f"Остановка сервера")


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
