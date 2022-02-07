# TODO Рандомная генерация файла заполнения мест
# TODO Скидки - реализация для студентов
# TODO Указание дат бронирования
"""
Для задания  6 из предыдущей практики реализовать:
[OK]    3.1 применение функций (не менее 5 штук)
    3.2 расписание полетов или поездов задается файлом, свободные места в вашон
       е или салоне указываются в файле (при продаже билета изменяете файл)
    
    3.3 реализовать заполнение шаблонов билетов (шаблон билетов разрабатывается
       самостоятельно) данными о рейсе, ФИО пассажира, вагоне, месте, времени и дат
       е отправления на весь путь(с учетом пересадок)

+ Редактирование и сдачу билетов. Но они есть, не забывайте что в файлах храним информацию 
о пассажирах и при этих операциях требуется изменять данные в соответствующих файлах.
Меню в консоли на выбор действия. При сдаче указаваем процент, который удерживается с пассажира 
(делаем вывод, что стоимость билета нам тоже желательно хранить)

Создать словарь железнодорожных сообщений с учетом более одной но менее 4 пересадок, с рекомендацией оптимального маршрута по времени
Между переходами разница в 30 мин
"""

import datetime
from os import path

import file_generator_module
import menu_module
import universal_module


def tt_regenerator(file_name, d, reg_flag):
    """
    Проверяет reg_flag, если требуется регенерация с новой датой (т.е. reg_flag == True)
    В условии перегенерирует d с текущей датой и пишет его в файл
    """

    # Формирование нового с новой датой
    if reg_flag == True:
        print("Регенерируем файл с расписанием поездов..")

        date = datetime.datetime.now().date().strftime("%d.%m.%Y ")

        d = {
            "Одинцово": [
                {
                    "begin_time": date + "21:30",
                    "time_range": 30,
                    "name": "Белорусский Вокзал",
                },
                {"begin_time": date + "14:40", "time_range": 3, "name": "Баковка"},
                {"begin_time": date + "10:30", "time_range": 15, "name": "Отрадное"},
            ],
            "Баковка": [
                {"begin_time": date + "07:45", "time_range": 3, "name": "Одинцово"},
                {
                    "begin_time": date + "14:20",
                    "time_range": 10,
                    "name": "Курский Вокзал",
                },
                {
                    "begin_time": date + "08:10",
                    "time_range": 25,
                    "name": "Савёловский Вокзал",
                },
            ],
            "Отрадное": [
                {"begin_time": date + "08:10", "time_range": 15, "name": "Одинцово"},
                {
                    "begin_time": date + "09:40",
                    "time_range": 60,
                    "name": "Курский Вокзал",
                },
                {
                    "begin_time": date + "18:21",
                    "time_range": 38,
                    "name": "Савёловский Вокзал",
                },
            ],
            "Белорусский Вокзал": [
                {"begin_time": date + "11:15", "time_range": 30, "name": "Одинцово"},
                {
                    "begin_time": date + "13:50",
                    "time_range": 10,
                    "name": "Курский Вокзал",
                },
                {
                    "begin_time": date + "20:52",
                    "time_range": 5,
                    "name": "Савёловский Вокзал",
                },
            ],
            "Курский Вокзал": [
                {
                    "begin_time": date + "17:02",
                    "time_range": 10,
                    "name": "Белорусский Вокзал",
                },
                {"begin_time": date + "17:10", "time_range": 10, "name": "Баковка"},
                {"begin_time": date + "15:58", "time_range": 60, "name": "Отрадное"},
            ],
            "Савёловский Вокзал": [
                {
                    "begin_time": date + "11:18",
                    "time_range": 5,
                    "name": "Белорусский Вокзал",
                },
                {"begin_time": date + "15:26", "time_range": 25, "name": "Баковка"},
                {"begin_time": date + "19:10", "time_range": 38, "name": "Отрадное"},
            ],
        }
        tt_obj = universal_module.FileClass(file_name)
        tt_obj.set_file(d)

        return d

    return d


class MainClass(object):
    def __init__(self):
        """
        Конструктор класса
        Формирует словарь железнодорожных сообщений + вызов всех методов
        """
        self.file_name = "./yaml/tickets.yml"
        self.tt_file_name = "./yaml/tt.yml"
        # Чтение из YAML
        tt_obj = universal_module.FileClass(self.tt_file_name, 2)
        self.d = tt_obj.get_text()

        tt_gereneration_flag = False
        # Проверка на текущую дату
        for first in self.d:
            for second in self.d[first]:
                buf_date = datetime.datetime.strptime(
                    second["begin_time"], "%d.%m.%Y %H:%M"
                ).strftime("%d.%m.%Y")
                date_now = datetime.datetime.now().strftime("%d.%m.%Y")
                if buf_date != date_now:
                    tt_gereneration_flag = True

        self.d = tt_regenerator(self.tt_file_name, self.d, tt_gereneration_flag)

        fileflag = path.exists(self.file_name)
        if fileflag == False:
            file_generator_module.FileGeneratorClass(self.d, self.file_name)
        else:
            reg_str = input(
                "Хотите обнулить все забронированные места и перегенерировать исходный файл? (Да/Нет)\n-> "
            )
            if reg_str == "Y" or reg_str == "y" or reg_str == "Да":
                file_generator_module.FileGeneratorClass(self.d, self.file_name)

        menu_module.MenuShower(self.d, self.file_name)


if __name__ == "__main__":
    MainClass()
