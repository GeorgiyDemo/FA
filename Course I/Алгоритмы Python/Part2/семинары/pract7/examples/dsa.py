import hashlib

hash_object = hashlib.new('DSA')
hash_object.update(b'Hello World')

print(hash_object.hexdigest())
