"""
  Абстрактная фабрика (AbstractFactory) - шаблон направленый на создание СЕМЕЙСТВ типовых объектов
  | Factory method                              | Abstract Factory                                      |
  -------------------------------------------------------------------------------------------------------
  | клиент получает метод для создания объектов | Содержит один или более методов для создания СЕМЕЙСТВ |
  |                                             | связанных объектов                                    |
  -------------------------------------------------------------------------------------------------------
  | использует наследование и подклассы         | использует композицию для делегирования работы другим |
  |                                             | классам                                               |
  -------------------------------------------------------------------------------------------------------
  | создается один продукт                      | создается семейство продуктов                         |
  -------------------------------------------------------------------------------------------------------
"""


from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_noveg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_noveg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_noveg_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Готовим ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " добавляем цыпленка к", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Готовим ", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " добавляем бекон к", type(VegPizza).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.create_noveg_pizza()
            self.VegPizza = self.factory.create_veg_pizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.make_pizzas()
