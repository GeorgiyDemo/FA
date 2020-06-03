"""
Выполнить собственную программную реализацию любой хеш функции.
"""


from mymd5 import MD5

def main():

    input_string = ""
    md5_hash = MD5.hash(input_string)
    print(md5_hash)


if __name__ == "__main__":
    main()