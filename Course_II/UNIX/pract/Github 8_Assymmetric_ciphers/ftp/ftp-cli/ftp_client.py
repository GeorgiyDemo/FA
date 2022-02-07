import base64
import json
import logging
import os
import pickle
import socket
import sys
import threading
from typing import Union

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from validator import port_validation, ip_validation
from crypt_utils import DiffieHellman, FileCrypter

DEFAULT_PORT = 9090
DEFAULT_IP = "127.0.0.1"
END_MESSAGE_FLAG = "CRLF_"
MAIN_STORAGE_DIR = "storage"
FILE_DETECT_FLAG = "DEMKA_FILE_STORAGE"

# Настройки логирования
logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    handlers=[logging.FileHandler("./logs/client.log"), logging.StreamHandler()],
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class Client:
    def __init__(self, server_ip: str, port_number: int, encryption: DiffieHellman) -> None:
        self.server_ip = server_ip
        self.port_number = port_number
        self.encryption = encryption
        self.file_crypter = FileCrypter(encryption.generate_key(encryption.mixed_key))
        self.sock = None
        self.new_connection()

        # Авторизуемся
        self.send_auth()

        # Поток чтения данных от сервера
        t = threading.Thread(target=self.read_message)
        t.daemon = True
        t.start()

        # Работа с данными, поступающими от пользователя
        self.input_processing()

    def new_connection(self):
        """Осуществляет новое соединение по сокету"""

        ip, port = self.server_ip, self.port_number
        sock = socket.socket()
        sock.setblocking(1)
        sock.connect((ip, port))
        self.sock = sock
        logging.info(f"Успешное соединение с сервером {ip}:{port}")

    def send_reg(self, password: str):
        """Логика регистрации пользователя в системе"""
        print("*Новая регистрация в системе*")
        while True:
            input_username = input("Введите ваше имя пользователя (ник) -> ")
            if input_username == "":
                print("Имя пользователя не может быть пустым!")
            else:
                data = json.dumps(
                    {"password": password, "username": input_username, "keys": self.encryption.auth_keys},
                    ensure_ascii=False,
                )
                self.sock.send(data.encode())
                logger.info(f"Отправка данных серверу: '{data}'")

                # Получаем данные с сервера
                response = json.loads(
                    self.sock.recv(4096).decode().replace(END_MESSAGE_FLAG, "")
                )
                if not response["result"]:
                    raise ValueError(
                        f"Не удалось осуществить регистрацию, ответ сервера {response}, более подробно см логи сервера"
                    )
                logger.info("Успешно зарегистрировались")
                break

    def send_auth(self):
        """Логика авторизации клиента"""
        login_iter = 1
        while True:

            # Отдельные строки для объяснения механизма авторизации при первом входе
            req_password_str = "Введите пароль авторизации"
            req_password_str += (
                "\nЕсли это ваш первый вход в систему, то он будет использоваться для последующей авторизации в системе -> "
                if login_iter == 1
                else " -> "
            )

            user_password = input(req_password_str)
            if user_password != "":

                data = json.dumps({"password": user_password}, ensure_ascii=False)
                # Отправляем сообщение
                self.sock.send(data.encode())
                logger.info(f"Отправка данных серверу: '{data}'")

                # Получаем данные с сервера
                response = json.loads(
                    self.sock.recv(4096).decode().replace(END_MESSAGE_FLAG, "")
                )

                # Если успешно авторизовались
                if response["result"]:
                    print(
                        "Авторизация прошла успешно, можете вводить сообщения для отправки:"
                    )
                    break

                # Если авторизация не удалась
                elif response["description"] == "wrong auth":
                    print("Неверный пароль!")
                    # Делаем новое соединение
                    # т.к. сервер рвет соединение, если авторизация не удалась
                    self.new_connection()

                # Если это первый вход с таким ip-адресом, то необходима регистрация
                elif response["description"] == "registration required":
                    self.new_connection()
                    self.send_reg(user_password)
                    self.new_connection()

                else:
                    raise ValueError(
                        f"Получили неожиданный ответ от сервера: {response}"
                    )

            else:
                print("Пароль не может быть пустым")

            login_iter += 1

    def read_message(self):
        """Чтение сообщения"""
        data = ""
        data_enc = ""
        while True:
            # Получаем данные и собираем их по кусочкам
            chunk = self.sock.recv(4096)
            data_enc += pickle.loads(chunk)
            data += self.file_crypter.encryption(pickle.loads(chunk))

            # Если это конец сообщения, то значит, что мы все собрали и можем обратно отдавать клиенту
            if END_MESSAGE_FLAG in data:
                logger.info(f"Прием зашифрованных данных от сервера: '{data_enc}'")
                logger.info(f"Прием расшифрованных данных от сервера: '{data}'")
                data = data.replace(END_MESSAGE_FLAG, "")

                data = json.loads(data)

                is_success_str = "+" if data["result"] else "-"
                result_str = data["description"]

                # Если сервер отдал нам файл
                if FILE_DETECT_FLAG in result_str:
                    file_name, file_content = result_str.split(FILE_DETECT_FLAG)
                    self.server2client_transfer(file_name, file_content)
                    message_str = f"Получили файл {file_name} от сервера"

                # Значит это результат выполнения команды
                else:
                    logger.info(f"Получили результат выполнения команды")
                    print(f"({is_success_str}) {result_str}")
                data, data_enc = "", ""

            # Если приняли часть данных - сообщаем
            else:
                logger.info(f"Приняли часть данных от сервера: '{data}'")

    def send_message(self, message: str):
        """Отправка сообщения"""

        # Добавляем флаг конца сообщения (по-другому я не знаю как передавать больше 4096 и не разрывать соединение)
        message += END_MESSAGE_FLAG
        # Отправляем сообщение
        message_new = self.file_crypter.encryption(message)
        logger.info(f"Отправка данных серверу: '{message}'")
        logger.info(f"В зашифрованном виде: '{message_new}'")
        self.sock.send(pickle.dumps(message_new))

    def input_processing(self):
        """Обработка ввода сообщений пользователя"""

        while True:
            msg = input()
            # Если сообщение exit
            if msg == "exit":
                break

            # Если это копирование файла, то вызывается отдельная логика на стороне клиента
            if "copy" in msg:
                msg = self.client2server_transfer(msg)

            # Т.к. client2server_transfer может отдавать None
            if msg:
                self.send_message(msg)

    # Давайте условимся на том, что все файлы лежат на одном уровне в директории storage
    def client2server_transfer(self, msg_path: str) -> Union[str, None]:
        """Метод для чтения и энкодинга файла с патча в набор байтов"""

        # Пытаемся обработать патч
        try:
            path = msg_path.split(" ")[1]
            root_name = path.split(os.sep)[-1]
            with open(f"{MAIN_STORAGE_DIR}{os.sep}{path}", "rb") as file:
                return root_name + FILE_DETECT_FLAG + base64.b64encode(file.read()).decode("utf-8")

        # Если не удалось обработать патч
        except (ValueError, FileNotFoundError, IndexError, IsADirectoryError):

            filelist = os.listdir(MAIN_STORAGE_DIR)
            r = "\n".join(filelist)
            print(
                f"\nЧто-то пошло не так при копировании файла с клиента на сервер.\nДоступные файлы в локальной директории {MAIN_STORAGE_DIR}:\n{r}"
            )
            return None

    def server2client_transfer(self, file_name: str, file_content: str):
        """Логика копирования файла с сервера на клиент"""
        try:
            content = base64.b64decode(file_content)
            with open(f"{MAIN_STORAGE_DIR}{os.sep}{file_name}", "w+") as f:
                f.write(content.decode("utf-8"))

        except Exception as e:
            print(str(e))

    def __del__(self):
        if self.sock:
            self.sock.close()
        logger.info("Разрыв соединения с сервером")


def main():
    with open("./key.txt", "r") as file:
        data = file.read()
    p, g, a = map(int, data.split(" "))
    encryption = DiffieHellman(a=a, p=p, g=g)
    port_input = input("Введите номер порта сервера -> ")
    port_flag = port_validation(port_input)
    # Если некорректный ввод
    if not port_flag:
        port_input = DEFAULT_PORT
        print(f"Выставили порт {port_input} по умолчанию")

    ip_input = input("Введите ip-адрес сервера -> ")
    ip_flag = ip_validation(ip_input)
    # Если некорректный ввод
    if not ip_flag:
        ip_input = DEFAULT_IP
        print(f"Выставили ip-адрес {ip_input} по умолчанию")

    client = Client(ip_input, int(port_input), encryption)


if __name__ == "__main__":
    main()
