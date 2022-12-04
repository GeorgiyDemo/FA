"""
Proxy, в общем случае - это система, которая является посредником между клиентом и поставщиком.
Клиент - это тот, кто делает запрос, а поставщик предоставляет ресурсы в ответ на запрос. В веб-мире
мы могли бы сравнить это с прокси-сервером. Клиенты (пользователи Интернет), когда они делают запрос на
веб-сайт, сначала подключаются к прокси-серверу, запрашивая ресурсы, такие как веб-страница.
Прокси-сервер внутренне оценивает этот запрос, отправляет его на соответствующий сервер и
получает обратно ответ, который затем доставляется клиенту. Таким образом, прокси-сервер
инкапсулирует запросы, обеспечивает конфиденциальность и хорошо работает в распределенных архитектурах.

В контексте шаблонов проектирования Proxy - это класс, который действует как интерфейс к реальным
объектам. Объекты могут быть нескольких типов, таких как сетевые подключения, большие объекты
в памяти и файле и так далее. Proxy - это объект-оболочка или агент, который обертывает реальный
объект. Прокси может предоставлять дополнительную функциональность объекту, который он обертывает,
при этом не меняя код объекта. Основное намерение Proxy заключается в предоставлении заглушки для другого
объекта, чтобы контролировать доступ к реальному объекту

"""


from abc import ABCMeta, abstractmethod


class You:
    def __init__(self):
        print("You:: Покупаю новый MacBook!")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: Вау! Процессор m2 реально хорош :-)")

        else:
            print("You:: Нужно зарабатывать больше :(")


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card  # Пусть номер карты это номер счета
        return self.account

    def __has_funds(self):
        print("Bank:: Проверка что на счете ", self.__get_account(), "достаточно средств")
        return True

    def set_сard(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print("Bank:: Осуществляется платеж")
            return True
        else:
            print("Bank:: Недостаточно средств!")
            return False


class DebitCard(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Запрос номера карты: ")

        self.bank.set_сard(card)
        return self.bank.do_pay()


you = You()
you.make_payment()