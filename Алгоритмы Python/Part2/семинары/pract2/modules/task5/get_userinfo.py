def processing():
    n = int(input("Ведите количество персон -> "))
    person_range = list(map(int, input("Введите диапазон для поиска персон по возрасту\nПример: 36-40\n-> ").split("-")))
    min_age, max_age = sorted(person_range)
    return n, min_age, max_age