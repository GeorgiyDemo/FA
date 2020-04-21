# бинарный режим:
with open("new_file6.txt", "wb") as f:
    f.write(bytes("Строка1\nСтрока2", "utf-8"))
    f.write(bytearray("\nCтpoкaЗ", "utf-8"))

with open("new_file6.txt", "r") as f:
    print(f.read())

import pickle  # подключаем модуль pickle

import yaml

check_elements = {}
for i in range(6):
    check_elements[i] = i

with open('./obj.pickle', 'wb') as f:
    pickle.dump(check_elements, f)

with open("./obj.yml", 'w') as stream:
    yaml.safe_dump(check_elements, stream)
