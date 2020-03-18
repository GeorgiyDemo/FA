from random import randint
from currency_class import CurrencyClass
from eur_class import EURClass
from usd_class import USDClass
def main():
    try:
        n = int(input("Введите кол-во валютных денежных сумм -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {1: EURClass,2: USDClass,}
    currency_list = [d[randint(1, 2)](randint(1, 1000)) for _ in range(n)]
    for c in currency_list: print(c.info() + "\n")