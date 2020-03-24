"""
(10 баллов) Текстовый файл Оценки.txt содержит строки вида «Иванов: 100, 45, 89, 789».
Используя данные этого файла создайте словарь, у которого ключом является фамилия, значением – кортеж из трех чисел (оценки).

(15 баллов) Напишите функцию, которая для словаря указанного вида находит максимальную и минимальную оценку
по заданной дисциплине.
Параметрами функции являются словарь и номер дисциплины (от 1 до 3).
По умолчанию номер дисциплины равен 1.
Функция возвращает кортеж из двух чисел.
"""
from sys import maxsize


def counter(input_dict, subj_number=1):
    """
    Входные данные:
    - input_dict - исходный словарь
    - subj_number - номер предмета
    """

    # Изначальные данные для max и min
    max_result, min_result = 0, maxsize

    # Для каждого значения в словаре цикл
    for value in input_dict.values():

        # Фикс индекса т.к. индексирование в python с 0
        locale_index = subj_number - 1

        # Если значение больше текущего максимального
        if value[locale_index] > max_result:
            # То это значение и становится максимальным
            max_result = value[locale_index]

        # Если значение меньше текущего минимального
        if value[locale_index] < min_result:
            # То это значение и становится минимальным
            min_result = value[locale_index]

    # Возврат значений
    return max_result, min_result


if __name__ == "__main__":

    # Финальный словарь
    this_dict = {}

    # Открываем файл оценки.txt на чтение
    with open("./Оценки.txt", "r") as file:
        file_result = file.read()

    # Создание списка строк исходного файла
    result_list = file_result.split("\n")

    # Цикл по каждой строке в списке
    for result in result_list:
        # Разделение по : и назначение переменных
        name, values = result.split(": ")

        # Список значений по разделителю ,
        values_list = values.split(", ")

        # Конвертация значений списка в целочисленный тип
        values_list = [int(x) for x in values_list]

        # Определение нового ключа словаря и значения
        this_dict[name] = values_list

    # Вывод полученного словаря на экран
    print(this_dict)
    # Вызов функции и вывод ее результата
    print(counter(this_dict, 2))
