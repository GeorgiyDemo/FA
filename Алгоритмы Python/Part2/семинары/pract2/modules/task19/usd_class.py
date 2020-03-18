from .currency_class import CurrencyClass
class USDClass(CurrencyClass):
    def __init__(self, balance):
        self.currency = super().usd_currency
        self.balance = balance
    def converter(self):
        return round(self.balance * self.currency, 2)
    def info(self):
        return "[USD]\nКол-во USD: " + str(self.balance) + "\nКурс обмена: " + str(self.currency) + "\nСконвертированная валюта в RUB: " + str(self.converter())