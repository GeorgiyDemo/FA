"""
Пример замыканий в Python
"""
import functools


# Функция высшего порядка
def generate_power_func(n):
    def nth_power(x):
        return x ** n

    return nth_power


def apply_operation(a, b):
    e = generate_power_func(a)
    return e(b)


if __name__ == "__main__":

    n3 = generate_power_func(2)
    print(n3(2), n3(3), n3(4))

    value = apply_operation(2, 3)
    print(value)

    str_e = "ABCDEFGH"

    enum1 = functools.partial(enumerate, start=5)
    for i, v in enum1(str_e):
        print(i, v)
