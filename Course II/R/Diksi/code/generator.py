"""Генератор случайных данных для контрольной по R"""

import os
from random import randint


def data_generator():
    """Генератор данных для магазина"""

    day_list = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
    ]
    infile_str = '"День.недели" "Поставки"\n'
    outfile_str = infile_str

    for day in day_list:
        infile_value = randint(100, 1000)
        infile_str += '"{}" {}\n'.format(day, infile_value)
        outfile_value = randint(int(infile_value / 4), infile_value)
        outfile_str += '"{}" {}\n'.format(day, outfile_value)
    return infile_str, outfile_str


def main():

    dir_list = list(range(1, 11))

    for shop in dir_list:
        print("Перегенерация данных для магазина №{}".format(shop))
        in_file, out_file = data_generator()
        with open("../shop{}/in.txt".format(shop), "w") as f:
            f.write(in_file)
        with open("../shop{}/out.txt".format(shop), "w") as f:
            f.write(out_file)


if __name__ == "__main__":
    main()
