from currency_class import CurrencyClass
class EURClass(CurrencyClass):
    def __init__(self, balance):
        self.currency = super().eur_currency
        self.balance = balance
    def converter(self):
        return self.balance * self.currency
    def info(self):
        return "[EUR]\nКол-во EUR: " + str(self.balance) + "\nКурс обмена: " + str(self.currency) + "\nСконвертированная валюта в RUB: " + str(self.converter())