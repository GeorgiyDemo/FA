"""
Выполнить собственную программную реализацию любой хеш функции.
"""

import hashlib

from mymd5 import MD5


def main():
    input_string = input("Введите строку для хеширования -> ")
    md5_hash = MD5.hash(input_string)
    print("Хеш MD5 собственной реализации\n{}".format(md5_hash))
    result = hashlib.md5(input_string.encode())
    print("Хеш MD5 из hashlib\n{}".format(result.hexdigest()))


if __name__ == "__main__":
    main()
