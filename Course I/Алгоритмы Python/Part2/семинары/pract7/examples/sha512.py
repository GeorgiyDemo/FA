import hashlib

hash_object = hashlib.sha512(b'Hello World')
hex_dig = hash_object.hexdigest()

print(hex_dig)
