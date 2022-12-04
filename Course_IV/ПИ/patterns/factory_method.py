"""
    Фабричный метод

"""

from abc import ABCMeta, abstractmethod


class PizzaPart(metaclass=ABCMeta):
    """Это абстрактный класс, он же Product из классического паттерна"""
    @abstractmethod
    def describe(self):
        pass


class CheesePart(PizzaPart):
    """Это и следующие это ConcreteProduct из классического паттерна"""
    def describe(self):
        print("Сыр")


class PepperoniPart(PizzaPart):
    def describe(self):
        print("Пепперони")


class PineapplePart(PizzaPart):
    def describe(self):
        print("Ананас")


class SeafoodPart(PizzaPart):
    def describe(self):
        print("Морепродукты")


class Pizza(metaclass=ABCMeta):
    """Это Creator из классического паттерна"""
    def __init__(self):
        self.parts = []
        self.create_pizza()

    @abstractmethod
    def create_pizza(self):
        pass

    def get_parts(self):
        return self.parts

    def add_part(self, part):
        self.parts.append(part)


class Pizza1(Pizza):
    """Это ConcreteCreator (один из)"""
    def create_pizza(self):
        self.add_part(PepperoniPart())
        self.add_part(PineapplePart())


class Pizza2(Pizza):
    """Это ConcreteCreator (один из)"""
    def create_pizza(self):
        self.add_part(PepperoniPart())
        self.add_part(PepperoniPart())
        self.add_part(PineapplePart())


class Pizza3(Pizza):
    """Это ConcreteCreator (один из)"""
    def create_pizza(self):
        self.add_part(PepperoniPart())
        self.add_part(PepperoniPart())
        self.add_part(PineapplePart())
        self.add_part(SeafoodPart())


pizza_type = input("Выберите вариант пиццы [1, 2 или 3]")
pizza = eval("Pizza"+str(pizza_type))()

print("Creating Pizza..", type(pizza).__name__)
print("Pizza has parts --", pizza.get_parts())

