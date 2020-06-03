import hashlib

hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()

print(hex_dig)
