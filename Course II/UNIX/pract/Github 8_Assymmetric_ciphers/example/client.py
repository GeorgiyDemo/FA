import pickle
import socket

from crypt_utils import DiffieHellman, FileCrypter

HOST = '127.0.0.1'
PORT = 8081


def main():
    sock = socket.socket()
    sock.connect((HOST, PORT))

    p = 54
    g = 53
    a = 63  # это можно хранить в txt

    diffie_hellman = DiffieHellman(a=a, p=p, g=g)
    client_mixed_key = diffie_hellman.mixed_key
    private_key = diffie_hellman.generate_key(client_mixed_key)
    print(client_mixed_key)
    print(private_key)

    sock.send(pickle.dumps((p, g, client_mixed_key)))
    sock.close()

    sock = socket.socket()
    sock.connect((HOST, PORT))
    crypter = FileCrypter(private_key)
    result = crypter.encryption("ТЕСТ ТЕСТ")
    print(result)
    sock.send(pickle.dumps(result))

    result = crypter.encryption(result)
    print(result)

    sock.close()


if __name__ == "__main__":
    main()
