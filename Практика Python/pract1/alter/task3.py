"""
Реализовать двух алфавитный шифр Цезаря для шифрования и 
дешифрование строки любой длины и заданным ключем,
используется латинский алфавит и цифры, а так же только нижний регистр.
"""

alpha1 = "0123456789abcldefghijkmnopqrstuvwxyz"
alpha2 = "abcldefghijkmnopqrstuvwxyz0123456789"
step=int(input('Введите шаг:='))
s=input('Введите строку для шифрования:=')

new_alpha1 = alpha1[step:]+alpha1[:step]
new_alpha2 = alpha2[step:]+alpha2[:step]

out = ""

for i in range(len(s)):
    int_val = i % 2

    if int_val == 0:
        buf_index = alpha1.index(s[i])
        new_symbol = new_alpha1[buf_index]

    elif int_val == 1:
        buf_index = alpha2.index(s[i])
        new_symbol = new_alpha2[buf_index]
    
    out += new_symbol

print(out)