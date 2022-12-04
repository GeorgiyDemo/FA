"""
    Реализация через метакласс
"""


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyLogger(metaclass=MetaSingleton):
    pass


logger1 = MyLogger()
logger2 = MyLogger()
print(logger1, logger2)
