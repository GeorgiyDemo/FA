class CurrencyClass:
    eur_currency = 85.46  # курс на 18.03.2020, хах
    usd_currency = 77.87

    def __init__(self, balance, exchange):
        self.balance = balance
        self.exchange = exchange

    def converter(self):
        return round(self.balance * self.exchange, 2)

    def info(self):
        return (
            "[Родительский класс валюты]\nКол-во: "
            + str(self.balance)
            + "\nКурс обмена: "
            + str(self.exchange)
            + "\nСконвертированная валюта: "
            + str(self.converter())
        )
