import hashlib
import uuid


def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(":")
    return (
        password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
    )


new_pass = input("Введите пароль: ")
hashed_password = hash_password(new_pass)
print("Строка для хранения в базе данных: " + hashed_password)
old_pass = input("Введите пароль еще раз для проверки: ")

if check_password(hashed_password, old_pass):
    print("Вы ввели правильный пароль")
else:
    print("Извините, но пароли не совпадают")
