

al="абвгдеёжзийклмнопрстуфхцчшщъыьэюя:)(;,.?0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

step=int(input('введите шаг:='))
s=input('введите шифруемое:=')

string_1 = al[step:]
string_2 = al[:step]
all_string = string_1 + string_2

#деёжзийклмнопрстуфхцчшщъыьэюяабвг
out = ""
for meow in s:
    buf_index = al.index(meow)
    new_symbol = all_string[buf_index]
    out += new_symbol
print("Зашифрованное: ", out)

income = ""
for x in out:
    buf_index = all_string.index(x)
    new_symbol = al[buf_index]
    income += new_symbol
print("Расшифрованное: ", income)

