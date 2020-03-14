import math
class Task4Class:
    def __init__(self, x):
        self.x = x
        self.getter()
    def getter(self):
        x = self.x
        upper = x ** 3 * math.e ** (x - 1)
        lower = x ** 3 - math.fabs(x)
        if lower == 0:
            print("Знаменатель равен нулю, деление на 0!")
            self.result = 0
            return
        first = upper / lower
        log_sqrt = math.sqrt(x) - x
        if log_sqrt >= 0:
            buf_log = math.log(log_sqrt, 2)
        else:
            print("Выражение в log[sqrt(x)-x,2] меньше 0!")
            self.result = 0
            return
        self.result = first - buf_log