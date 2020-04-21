from texttable import Texttable
from task_module import UtilClass

class ChangeClass:
    """Класс для изменения данных студентов"""
    def __init__(self, main_obj):
        self.main_obj = main_obj
        self.new_obj = None
        
        methods_dict = {
            1 : self.sname_changer,
            2 : self.sgroup_changer,
            3 : self.scourse_changer,
            4 : self.cert_menu,
            5 : self.work_menu,
        }

        while True:
            print("\033[93m\nПожалуйста, учтите, что баллы студента и даты аттестаций автоматически перегенерируются за счет работ, которые они содержат\033[0m\nЧто вы хотите изменить?\n1. Имя студента\n2. Группу студента\n3. Курс студента\n4. Название аттестаций\n5. Работы студента\n0. Выход и запись изменений")
            try:
                method_number = int(input("-> "))
                if method_number in methods_dict:
                    methods_dict[method_number]()
                elif method_number == 0:
                    self.new_obj = self.main_obj
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Некорректный ввод данных")

    #TODO
    def sgroup_changer(self):
        """Изменение группы студента"""
        pass

    #TODO
    def scourse_changer(self):
        """Изменение курса студента"""
        pass

    #TODO
    def work_menu(self):
        """Меню выбора работы для ее последующего изменения"""
        pass

    def sname_changer(self):
        """Изменение ФИО студента"""
        
        obj = self.main_obj
        new_name = input('Введите новые ФИО для студента {} ->'.format(obj.name))
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
            allowed_keys.append(str(i+1))
            table_list.append([str(i+1)]+[cert.name, cert.points, c(cert.date_begin), c(cert.date_end)])

        table.add_rows(table_list)
        print("\n"+table.draw())

        selected_cert = input("-> ")
        if selected_cert in allowed_keys:
            new_name = input("Введите обновленное название для аттестации №{} ->".format(selected_cert))
            self.main_obj.cert_obj_list[selected_cert].name = new_name
            print("Успешное обновление названия аттестации")
        else:
            print("Некорректный ввод данных, выход в подменю")
