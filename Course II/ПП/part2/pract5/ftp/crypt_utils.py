class FileCrypter:
    def __init__(self, key: int):
        self.key = key

    def encryption(self, message: str) -> str:
        """
        Шифрует сообщение ключом key

        Каждый символ возводит в степень этого ключа
        :param message: исходное сообщение
        :return: зашифрованное/расшифрованное сообщение
        """
        return "".join([chr(ord(message[i]) ^ self.key) for i in range(len(message))])


class DiffieHellman:

    def __init__(self, a: int, p: int, g: int):
        self._a = a
        self._p = p
        self._g = g

    @property
    def mixed_key(self):
        """
        :return: смешанный ключ
        """
        return self._g ** self._a % self._p

    def generate_key(self, mixed_key):
        """
        :param mixed_key: смешанный ключ
        :return: приватный ключ
        """
        return mixed_key ** self._a % self._p

    @property
    def auth_keys(self):
        """Получение элементов для передачи на сторону сервера"""
        return self._p, self._g, self.mixed_key
