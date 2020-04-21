"""
Реализовать шифр с использованием кодового слова,
используется латинский алфавит с верхним регистром.
"""

global_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
input_string = input("Введите кодовое слово -> ")

d = {}

# Объявили
for s in input_string:
    d[s] = 0

# Занесли значения
for s in input_string:
    d[s] += 1

# Проверили значения значения
check_flag = True
for element in d:
    if d[element] > 1:
        check_flag = False

if check_flag == False:
    print("Внимание, повтор значений!")

ecrypt_string = input("Введите строку для шифрования ->")

print("Старый алфавит", global_string)

buf_string = global_string
for s in input_string:
    buf_string = buf_string.replace(s, "")

buf_string = input_string + buf_string

out_string = ""
for c in ecrypt_string:
    old_index = global_string.find(c)
    new_char = buf_string[old_index]
    out_string += new_char

print(out_string)
