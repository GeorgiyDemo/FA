import pickle
import socket

from crypt_utils import DiffieHellman, FileCrypter

HOST = '127.0.0.1'
PORT = 8081


def main():
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(1)

    crypter = None
    while True:
        conn, addr = sock.accept()

        msg = conn.recv(4096)
        # Получаем данные от клиента
        data = pickle.loads(msg)

        print(type(data))
        if type(data) == tuple:
            p, g, A = data

            diffie_hellman = DiffieHellman(a=A, p=p, g=g)
            server_mixed_key = diffie_hellman.mixed_key
            private_key = diffie_hellman.generate_key(server_mixed_key)
            crypter = FileCrypter(private_key)
            print(server_mixed_key)
            print(private_key)

        elif type(data) == str:
            result = crypter.encryption(data)
            print(result)

        else:
            raise ValueError(f"Был принят некорректный тип data: {type(data)}")


if __name__ == "__main__":
    main()
