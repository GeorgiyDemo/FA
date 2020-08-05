# TODO тут нет фильтрации ввода и у меня нет времени ее сделать

import time
from random import randint, choice

import data_module
from airclass_module import PlaneClass, HelicopterClass
from faker import Faker
from objectkilled_module import ObjectKilledClass
from pvo_module import MissileClass, AntiAircraft


def main():
    """
    Программа должна: 
    1.	предоставлять пользователю возможность создания списка летательных объектов, средств ПВО и Объектов поражения;
    2.	предоставлять возможность вывода информации о летательном объекте, средстве ПВО и Объекте поражения;
    3.	выполнить расчет времени полета на имеющемся запасе топлива; (для самолетов)
    4.	выполнить расчет возможности полета на введенное расстояние без дозаправки; (для самолетов)
    5.	для выбранного летательного объектов выполнять расчет возможности поражения заданного объекта (объект может быть летательным или наземным); (для самолетов)
    6.	предоставлять расчет количества вертолетов для перевозки груза за заданное количество полетов; (для вертолетов)
    7.	предоставлять расчета возможности поражения летательного объекта с учетом его скорости и высоты полета.
    В программе должно использоваться минимально 2 рекурсии на усмотрение учащегося. Допускается обоснованное изменение структуры классов при программной реализации. Итоговое задание требуется разбить на модули.
    """

    fake = Faker("ru_RU")

    aircraftclass_dict = {
        1: PlaneClass,
        2: HelicopterClass,
    }
    helicopter_obj_list, plane_obj_list = [], []
    aircraft_count = int(input("Введите количество объектов летательных аппаратов -> "))
    for _ in range(aircraft_count):

        r_num = randint(1, 2)
        # Генерируем рандомные аргументы
        aircraftclass_dictargs = {
            1: [
                fake.word(),
                randint(1000, 200000),
                data_module.plane_type(),
                randint(1, 10000),
                data_module.get_country(),
                data_module.get_country(),
                randint(300, 2500),
                "ракеты",
                randint(500, 10000),
                randint(1000, 100000),
                100000,
                10,
            ],
            2: [
                fake.word(),
                randint(1000, 200000),
                data_module.helicopter_type(),
                randint(1, 10000),
                data_module.get_country(),
                data_module.get_country(),
                randint(2, 8),
                randint(20, 40),
                data_module.get_country(),
            ],
        }
        if r_num == 1:
            plane_obj_list.append(
                aircraftclass_dict[r_num](*aircraftclass_dictargs[r_num])
            )
        else:
            helicopter_obj_list.append(
                aircraftclass_dict[r_num](*aircraftclass_dictargs[r_num])
            )

    print(
        "Хорошо, я сгенерировал {} самолетов и {} вертолетов, давайте взгляним на них?".format(
            len(plane_obj_list), len(helicopter_obj_list)
        )
    )
    input()
    for e in [helicopter_obj_list, plane_obj_list]:
        for obj in e:
            print()
            obj.info()

    # Средства ПВО

    pvo_dict = {
        1: MissileClass,
        2: AntiAircraft,
    }

    missile_list_obj, antiaircraft_list_obj = [], []
    pvo_count = int(input("Введите количество объектов средств ПВО -> "))
    for _ in range(pvo_count):
        r_num = randint(1, 2)

        pvo_dictargs = {
            1: [
                fake.word(),
                randint(1000, 200000),
                randint(2, 8),
                randint(16, 128),
                randint(1000, 200000),
                randint(1000, 200000),
                choice(["стационарное", "перемещаемое"]),
                randint(5, 80),
            ],
            2: [
                fake.word(),
                randint(1000, 200000),
                randint(2, 8),
                randint(16, 128),
                randint(9, 72),
                randint(1, 256),
            ],
        }
        if r_num == 1:
            missile_list_obj.append(pvo_dict[r_num](*pvo_dictargs[r_num]))
        else:
            antiaircraft_list_obj.append(pvo_dict[r_num](*pvo_dictargs[r_num]))

    print(
        "Хорошо, я сгенерировал {} ракетных и {} зенитных вида ПВО, заценим?".format(
            len(missile_list_obj), len(antiaircraft_list_obj)
        )
    )
    input()
    for e in [missile_list_obj, antiaircraft_list_obj]:
        for obj in e:
            print()
            obj.info()

    killedobj_count = int(input("Введите количество объектов поражения -> "))
    killedobj_list = []
    for _ in range(killedobj_count):
        obj = ObjectKilledClass(fake.word(), choice(["наземный", "летательный"]))
        obj.info()
        killedobj_list.append(obj)

    # 3.	выполнить расчет времени полета на имеющемся запасе топлива; (для самолетов)
    print(
        "\nХорошо, начнем с самолетов. Давайте рассчитаем для каждого время олета на имеющемся запасе топлива"
    )
    for plane in plane_obj_list:
        print(
            "Название самолета: {}, время полета на запасе: {}".format(
                plane.name, plane.fuel_calculation()
            )
        )

    # 4.	выполнить расчет возможности полета на введенное расстояние без дозаправки; (для самолетов)
    plane_range = float(input("Введите расстояние для рассчета без дозаправки -> "))
    for plane in plane_obj_list:
        plane_result, max_distance = plane.flight_opportunity_max(plane_range)
        if plane_result == True:
            result = "долетит то точки "
        else:
            result = "не долетит"
        print("Самолет {}, пролетит {} и {}".format(plane.name, max_distance, result))

    print(
        "Теперь необходимо выбрать летательный объект для самолета и задать объект поражения. Сейчас выведу краткую информацию по каждому:"
    )
    print("Выбор самолета")
    for i in range(len(plane_obj_list)):
        print(
            "[{}] Название: {}, вид: {}".format(
                i, plane_obj_list[i].name, plane_obj_list[i].object_type
            )
        )

    plane_number = int(input("Введите номер самолета -> "))
    print("Хорошо, самолет под номером {} выбран".format(plane_number))

    print("Теперь выбираем объект для поражения:")
    for i in range(len(killedobj_list)):
        print(
            "[{}] Название: {}, тип: {}".format(
                i, killedobj_list[i].name, killedobj_list[i].type
            )
        )

    obj_number = int(input("Введите номер объекта -> "))
    print("Хорошо, объект под номером {} выбран".format(obj_number))

    print("Стреляем..")

    time.sleep(3)
    # Получаем результат
    result = plane_obj_list[plane_number].murder_opportunity(killedobj_list[obj_number])
    if result == True:
        print(
            "Мы уничтожили объект с названием '{}' и типом {}".format(
                killedobj_list[obj_number].name, killedobj_list[obj_number].type
            )
        )
        del killedobj_list[obj_number]
    else:
        print("Мы не смогли уничтожить объект")

    print("ПОКА ВСО")
    # TODO ТУТ ВСЕ МЕТОДЫ ЕСТЬ, ТОЛЬКО ВЫЗОВ НАДО, надо больше времени
    # plane_mumber = input("Введите номер самолета -> ")
    # 5.	для выбранного летательного объектов выполнять расчет возможности поражения заданного объекта (объект может быть летательным или наземным); (для самолетов)
    # 6.	предоставлять расчет количества вертолетов для перевозки груза за заданное количество полетов; (для вертолетов)
    # 7.	предоставлять расчета возможности поражения летательного объекта с учетом его скорости и высоты полета.


if __name__ == "__main__":
    main()
