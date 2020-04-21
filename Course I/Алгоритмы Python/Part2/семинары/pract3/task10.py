"""
10. Даны числа a и b. Определите, сколько существует последовательностей из a нулей и b
единиц, в которых никакие два нуля не стоят рядом
"""


def ranges_detector(a, b):
    if a > b + 1: return 0
    if a == 0 or b == 0: return 1
    result_plus = ranges_detector(a, b - 1) + ranges_detector(a - 1, b - 1)
    return result_plus


if __name__ == "__main__":
    a = int(input("Введите число а -> "))
    b = int(input("Введите число b -> "))
    r = ranges_detector(a, b)
    print(r)
