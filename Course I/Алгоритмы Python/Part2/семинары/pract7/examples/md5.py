import hashlib

hash_object = hashlib.md5(b"Hello World")
print(hash_object.hexdigest())

mystring = input("Enter String to hash: ")

# Предположительно по умолчанию UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())
