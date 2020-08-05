from config import IP_ADDR
import socket

sock = socket.socket()
print("Создание сокета")
sock.bind((IP_ADDR, 9090))
print("Связь сокета с данными")
sock.listen(0)
print("Запуск режима прослушивания для сокета")
conn, addr = sock.accept()
print("Подключение для отправки данных клиенту")
print(addr)

msg = ""

while True:
    data = conn.recv(1024)
    if not data:
        break
    msg += data.decode()
    conn.send(data)

print(msg)

conn.close()
