"""
  Фасад - посредник, скрывающий сложность реализации за простым интерфейсом
"""


class Agent(object):

    def __init__(self):
        print("Агент:: Попробую организовать\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.ticketSeller = TicketSeller()
        self.ticketSeller.get_tickets()

        self.driver = Driver()
        self.driver.drive_to_hotel()

        print("Готово!\n")


class Hotelier(object):
    def __init__(self):
        print("Бронируем отель>? --")

    def __isAvailable(self):
        print("Есть места на дату?")
        return True

    def book_hotel(self):
        if self.__isAvailable():
            print("Регистрирую бронь\n\n")


class TicketSeller(object):
    def __init__(self):
        print("Нужны билеты? --")

    def get_tickets(self):
        print("Резервирую билеты\n\n")


class Driver(object):
    def __init__(self):
        print("Нужна встреча в аэропорту --")

    def drive_to_hotel(self):
        print("Поездка забронирована\n\n")


class You(object):
    def __init__(self):
        print("You:: Так, нужно организовать поездку??!!!")

    def ask_agent(self):
        print("You:: Вызываю агента\n\n")

        a = Agent()
        a.arrange()

    def __del__(self):
        print("You:: Все отлично!")


you = You()
you.ask_agent()