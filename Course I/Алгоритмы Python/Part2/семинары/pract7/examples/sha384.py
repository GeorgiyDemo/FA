import hashlib

hash_object = hashlib.sha384(b'Hello World')
hex_dig = hash_object.hexdigest()

print(hex_dig)
