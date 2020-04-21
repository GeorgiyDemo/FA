"""
1. Дано натуральное число n. Выведите все числа от 1 до n.
Ввод: 5
Вывод 1 2 3 4 5
"""


def r_printer(n_max, current_n=1):
    # Останов
    if current_n > n_max:
        print(" ")
        return
    print(current_n, end=" ")
    # Вызов на уровень ниже
    r_printer(n_max, current_n + 1)


if __name__ == "__main__":
    n = int(input("Введите натуральное число n -> "))
    r_printer(n)
