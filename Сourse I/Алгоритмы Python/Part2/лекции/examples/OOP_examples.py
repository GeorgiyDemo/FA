class Car(object):
    """Базовый класс для автомобилей"""
    def __init__(self, x): # конструктор класса, используется для инициализации нового объекта
        self.x = x # создаем аттрибут класса        
        
    # метод класса; все методы класса должны в качестве первого атрибута иметь переменную self,
    # в которую автоматически передается ссылка на текущий объект 
    def is_near(self, x2): 
        return abs(self.x - x2) < 2.0 # self.x - обращение к атрибуту класса

# Класс CargoCar с контролем доступа к значениям, выполненным в стиле Python
class CargoCar3(Car): 
    def __init__(self, x, max_load, load):
        self.x = x
        self.__max_load = max_load
        self.__load = load
        assert not(self.is_overloaded()), 'При создании автомобиля превышено ограничение загрузки!'
    
    def is_overloaded(self):
        return self.__load > self.__max_load
    
    @property # Декоратор функции, оформляющий функцию как функцию доступа
    def load(self):
        return self.__load
    
    @load.setter # Декоратор функции, оформляющий функцию как функцию-сеттер
    def load(self, val): # проверка при изменении значения
        assert val < self.__max_load, "Превышен предел загрузки!"
        self.__load = val
        
    # при необходимости, есть декоратор вида: @load.deletter
        
    @property 
    def max_load(self): # для max_load есть только возможность получения значения
        return self.__max_load