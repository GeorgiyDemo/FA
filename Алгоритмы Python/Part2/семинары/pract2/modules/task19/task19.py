"""
Задача 14. Создайте класс ВАЛЮТА с методами перевода денежной суммы в рубли и вывода на экран.
Создайте дочерние классы ДОЛЛАР, ЕВРО со своими методами перевода и вывода на экран.
Создайте список п валютных денежных сумм и выведите полную информацию о них на экран.
"""

from random import randint


class CurrencyClass:
    """
    Родительский класс с абстрактной валютой
    """
    # Стат поля
    eur_currency = 70.94
    usd_currency = 65.27

    def __init__(self, balance, exchange):
        self.balance = balance
        self.exchange = exchange

    def converter(self):
        return self.balance * self.exchange

    def info(self):
        return "[Родительский класс валюты]\nКол-во: " + str(self.balance) + "\nКурс обмена: " + str(
            self.exchange) + "\nСконвертированная валюта: " + str(self.converter())


class EURClass(CurrencyClass):
    """
    Класс для работы с EUR
    """

    def __init__(self, balance):
        self.currency = super().eur_currency
        self.balance = balance

    def converter(self):
        return self.balance * self.currency

    def info(self):
        return "[EUR]\nКол-во EUR: " + str(self.balance) + "\nКурс обмена: " + str(
            self.currency) + "\nСконвертированная валюта в RUB: " + str(self.converter())


class USDClass(CurrencyClass):
    """
    Класс для работы с USD
    """

    def __init__(self, balance):
        self.currency = super().usd_currency
        self.balance = balance

    def converter(self):
        return self.balance * self.currency

    def info(self):
        return "[USD]\nКол-во USD: " + str(self.balance) + "\nКурс обмена: " + str(
            self.currency) + "\nСконвертированная валюта в RUB: " + str(self.converter())


def main():
    try:
        n = int(input("Введите кол-во валютных денежных сумм -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: EURClass,
        2: USDClass,
    }

    currency_list = [d[randint(1, 2)](randint(1, 1000)) for _ in range(n)]
    for c in currency_list:
        print(c.info() + "\n")


if __name__ == "__main__":
    main()