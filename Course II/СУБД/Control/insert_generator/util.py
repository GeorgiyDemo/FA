"""Отдельный модуль с фуекциями-утилитами для генерации"""
import random
import faker


def get_number_range(n) -> str:
    """Отдает n рандомных цифр"""

    result = ""
    for _ in range(n):
        result += str(random.choice(range(10)))
    return result


def get_random_name(fake_ru: faker.Faker, fake_en: faker.Faker) -> tuple:
    """Возвращает рандомное русское/английское имя"""

    names_list = [
        fake_ru.name().replace("'", "").split(" "),
        fake_en.name().replace("'", "").split(" "),
    ]
    current_name_list = random.choice(names_list)
    if len(current_name_list) == 4:
        _, first_name, last_name, _ = current_name_list
    elif len(current_name_list) == 3:
        first_name, _, last_name = current_name_list
    else:
        first_name, last_name = current_name_list
    return (first_name, last_name)


# TODO
def data_range_generator() -> tuple:
    """Генератор дат для бронирования"""

    pass
