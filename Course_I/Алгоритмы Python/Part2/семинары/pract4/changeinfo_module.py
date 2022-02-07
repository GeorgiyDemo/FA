from texttable import Texttable
from task_module import UtilClass


class ChangeClass:
    """Класс для изменения данных студентов"""

    def __init__(self, main_obj):
        self.main_obj = main_obj
        self.new_obj = None

        methods_dict = {
            1: self.sname_changer,
            2: self.sgroup_changer,
            3: self.scourse_changer,
            4: self.work_menu,
        }

        while True:
            print(
                "\033[93m\nПожалуйста, учтите, что баллы студента и даты аттестаций автоматически перегенерируются за счет работ, которые они содержат\033[0m\nЧто вы хотите изменить?\n1. ФИО студента\n2. Группу студента\n3. Курс студента\n4. Работы студента\n0. Выход и запись изменений"
            )

            method_number = input("-> ")
            if UtilClass.is_digital(method_number):

                method_number = int(method_number)
                if method_number in methods_dict:
                    methods_dict[method_number]()
                elif method_number == 0:
                    self.new_obj = self.main_obj
                    break
                else:
                    print("Введенный номер отсутствует в списке")
            else:
                print("Некорректный ввод данных")

    def sgroup_changer(self):
        """Изменение группы студента"""
        new_group = input("Введите новую группу студента ->")
        self.main_obj.group = new_group
        print("Данные группы студента успешно обновлены")

    def scourse_changer(self):
        """Изменение курса студента"""
        new_course = input("Введите новый курс студента ->")
        self.main_obj.course = new_course
        print("Данные курса студента успешно обновлены")

    def work_menu(self):
        """Меню выбора работы для ее последующего изменения"""

        print("Введите номер работы для ее редактирования:")
        table = Texttable()
        table_list = [
            [
                "№",
                "Название аттестации",
                "Название",
                "Тип",
                "Дата дедлайна",
                "Дата сдачи",
                "Дата защиты",
                "Баллы",
            ]
        ]

        # Вводим единый список работ для 2 аттестаций для удобного выбора

        patched_workobj_list = []

        for i in range(len(self.main_obj.cert_obj_list)):
            cert = self.main_obj.cert_obj_list[i]
            for j in range(len(cert.work_obj_list)):
                work = cert.work_obj_list[j]
                patched_workobj_list.append([cert, work, i, j])

        main_list, allowed_keys = [], []
        for i in range(len(patched_workobj_list)):
            cert, work, _, _ = patched_workobj_list[i]
            allowed_keys.append(str(i + 1))
            main_list.append([str(i + 1), cert.name] + work.get_list())

        table_list.extend(main_list)
        table.add_rows(table_list)
        print("\n" + table.draw())
        selected_work = input("-> ")

        if selected_work in allowed_keys:

            # В этой группе тусуются все наши пацаны, вот они слева направо: объект аттестации, объект работы, индекс аттестациии, индекс работы
            _, work, i, j = patched_workobj_list[int(selected_work) - 1]
            # Вызов класса с передачей объекта работы
            workchanger_obj = WorkChangerClass(work)
            # Получили новый объект и выставляем его через объект студента по индексам
            self.main_obj.cert_obj_list[i].work_obj_list[j] = workchanger_obj.new_obj
            print("Данные работы успешно обновлены")

        else:
            print("Некорректный ввод данных, выход в подменю")

    def sname_changer(self):
        """Изменение ФИО студента"""

        obj = self.main_obj
        new_name = input("Введите новые ФИО для студента {} ->".format(obj.name))
        self.main_obj.name = new_name
        print("Успешное обновление ФИО студента")

    def cert_menu(self):
        """Меню выбора аттестации для изменения названия"""

        print("Пожалуйста, выберите аттестацию для изменения ее названия:")
        cert_list = self.main_obj.cert_obj_list
        table = Texttable()
        table_list = [["№", "Название", "Баллы", "Дата начала", "Дата окончания"]]
        allowed_keys = []
        c = UtilClass.converter
        for i in range(len(cert_list)):
            cert = cert_list[i]
            allowed_keys.append(str(i + 1))
            table_list.append(
                [str(i + 1)]
                + [cert.name, cert.points, c(cert.date_begin), c(cert.date_end)]
            )

        table.add_rows(table_list)
        print("\n" + table.draw())

        selected_cert = input("-> ")
        if selected_cert in allowed_keys:
            new_name = input(
                "Введите обновленное название для аттестации №{} ->".format(
                    selected_cert
                )
            )
            self.main_obj.cert_obj_list[int(selected_cert) - 1].name = new_name
            print("Успешное обновление названия аттестации")
        else:
            print("Некорректный ввод данных, выход в подменю")


class WorkChangerClass:
    """Класс для изменения данных переданного объекта работы"""

    def __init__(self, main_obj):
        self.main_obj = main_obj
        self.new_obj = None

        methods_dict = {
            1: self.wname_changer,
            2: self.wtype_changer,
            3: self.set_complete,
            4: self.set_protection,
            5: self.wpoints_changer,
        }

        while True:
            print(
                "\nЧто вы хотите изменить в работе?\n1. Название работы\n2. Тип работы\n3. Сдать работу/изменить дату сдачи\n4. Защитить работу/изменить дату защиты\n5. Изменить кол-во баллов за работу\n0. Выход и запись изменений"
            )

            method_number = input("-> ")
            if UtilClass.is_digital(method_number):

                method_number = int(method_number)
                if method_number in methods_dict:
                    methods_dict[method_number]()
                elif method_number == 0:
                    self.new_obj = self.main_obj
                    break
                else:
                    print("Введенный номер отсутствует в списке")
            else:
                print("Некорректный ввод данных")

    def wname_changer(self):
        """Изменение названия работы"""
        new_name = input("Введите новое название работы -> ")
        self.main_obj.name = new_name
        print("Успешное изменение названия работы")

    def wtype_changer(self):
        """Изменение типа работы"""
        alowed_list = ["практика", "контрольная", "тестирование"]
        new_type = input(
            "Введите новый тип работы (практика/контрольная/тестирование) -> "
        )
        if new_type not in alowed_list:
            print("Некорректный ввод данных")
            return

        self.main_obj.work_type = new_type
        print("Успешное обновление типа работы")

    # Спасибо мне большое, что я для объекта работы написал эти методы
    def set_complete(self):
        """Осуществление сдачи работы"""
        date_input = input("Введите дату сдачи работы ->")
        self.main_obj.set_complete(date_input, True)

    def set_protection(self):
        """Осуществление защиты работы"""
        date_input = input("Введите дату защиты работы ->")
        self.main_obj.set_protection(date_input, True)

    def wpoints_changer(self):
        """Изменение кол-во баллов работы"""
        print(
            "Для изменения баллов работы необходимо полностью удалить студента в главном меню и пересоздать его.\nТакое происходит из-за того, что кол-во баллов на работу рассчитывается исходя из 20 баллов/общее кол-во практических работ."
        )
