import socket
from time import sleep
from config import IP_ADDR, MESSAGE

sock = socket.socket()
sock.setblocking(1)
sock.connect((IP_ADDR, 9090))

# msg = input()
sock.send(MESSAGE.encode())

data = sock.recv(1024)
sock.close()

print(data.decode())

"""
8. Соединение с сервером;
9. Разрыв соединения с сервером;
10. Отправка данных серверу;
11. Прием данных от сервера.
"""
