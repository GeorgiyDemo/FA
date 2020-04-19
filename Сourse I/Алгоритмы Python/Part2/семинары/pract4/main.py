"""
Разработать программное средство с использованием ООП для представления успеваемости студентов по дисциплине:
1)	Промежуточная аттестация максимум 20 баллов, разбитые по количеству работ (практики, контрольная и тестирование в 1 половине семестра);
2)	Работа в семестре 20 баллов (практики, контрольная и тестирование во 2 половине семестра);
3)	Экзамен 60 баллов;
4)	Выставление итоговой оценки.
Объект класса должен содержать поля для сохранения имени студента и
истории получения баллов (по практикам, контрольным и тестированиям) с учетом даты получения оценки по схеме: выполнено, защищено.
"""
import sqlite_module
import webbrowser
from task_module import WorkClass, ExamClass, StudentClass, CertificationClass

def main():
    """
    Общий алгоритм
    - Генерим студента
    - Генерим промежуточную аттестацию/аттестацию
    - Генерим работу

    - Добавляем объект аттестации к студенту
    - В объект аттестации добавляем работы
    - Добавляем объект работы к промежуточной аттестации

    Повторяем сколько надо
    """

    #Найс ассоциация, но мне нравки
    boolean_dict = {
        "Да" : True,
        "ДА" : True,
        "Нет" : False,
        "Не" : False,
        "нет" : False,
        "не" : False,
    }

    work_count = int(input("Введите количество работ за половину семестра (кол-во работ в 1 и 2 половине семестра равно) -> "))
    
    #if work_count < 3:
    #    print("Слишком мало работ, ты что, в Синергии?")
    #    webbrowser.open('https://synergy.ru/', new=2)
    #    return


    WorkClass.WORK_COUNT = work_count
    students_count = int(input("Введите количество студентов для добавления -> "))

    stud_obj_list = []
    for i in range(students_count):
        print("*Добавляем студента №{}*".format(i+1))
        
        s_name = input("Введите ФИО студента -> ")
        s_group = input("Введите группу студента -> ")
        s_course = input("Введите курс студента -> ")

        student_obj = StudentClass(s_name, s_group, s_course)
        cert_obj_list = []

        for j in range(2):
            print("\nДобавляем промежуточную аттестацию №{}".format(j+1))
            cert_obj = CertificationClass("Промежуточная аттестация №{}".format(j+1))

            work_obj_list = []
            for k in range(work_count):

                bool_flag = True
                while bool_flag:
                    try:

                        print("\n*Добавляем работу №{}*".format(k+1))
                        w_name = input("Введите название работы -> ")
                        w_type = input("Введите тип работы (практика/контрольная/тестирование) -> ")
                        w_deadline = input("Введите дату дедлайна работы в формате ДД.ММ.ГГГГ (пример: 01.01.2020) -> ")
                        w_completed = boolean_dict[input("Работа завершена? (Да/Нет) -> ")]
                        w_date_completed, w_date_protected = None, None
                        if w_completed:
                            w_date_completed = input("Введите дату завершения работы в формате ДД.ММ.ГГГГ (пример: 01.01.2020) -> ")
                        w_protected = boolean_dict[input("Работа защищена? (Да/Нет) -> ")]
                        if w_protected:
                            w_date_protected = input("Введите дату защиты работы в формате ДД.ММ.ГГГГ (пример: 01.01.2020) -> ")

                        work_obj = WorkClass(w_name, w_type, w_deadline, w_completed, w_date_completed, w_protected, w_date_protected)
                        work_obj_list.append(work_obj)
                        
                        bool_flag = False

                    except Exception as e:
                        print("Произошла ошибка:",e,"\nПовторите весь ввод данных по текущей работе!")
            
            #Добавляем работы к промежуточной аттестации
            [cert_obj.add(w) for w in work_obj_list]
            
            #Добавляем промежуточную аттестацию к промежуточным аттестациям
            cert_obj_list.append(cert_obj)
        
        #Добавляем аттестации студенту
        [student_obj.add_certification(cert) for cert in cert_obj_list]

        #Экзамен?
        bool_flag = True
        while bool_flag:
            try:
                s_exam = boolean_dict[(input("{} сдавал экзамен? (Да/Нет) -> ".format(s_name)))]
                if s_exam:
                    s_name = input("Введите полное название экзамена ->")
                    s_points = int(input("Введите кол-во баллов на экзамене (макс. 60) -> "))
                    exam_obj = ExamClass(s_name, s_points)
                    student_obj.add_exam(exam_obj)
                    
                bool_flag = False
            except Exception as e:
                print("Произошла ошибка:",e,"\nПовторите ввод данных!")

        #Вывод всей инфы по данной структуре
        student_obj.all_info()

        #Добавляем студента в БД
        sqlite_obj = sqlite_module.SQLiteClass()
        sqlite_obj.set_students(student_obj)

        #Добавляем студента в список студентов
        stud_obj_list.append(student_obj)

    #TODO Надо статистику в Excel по каждому студенту

# Что вы хотите сделать?
# 1) Получение данных студентов с БД
# 2) Добавление данных студентов в БД
# 3) Удаление данных студентов в БД
# 4)Формирование отчета по студентам из данных БД
# 0) Завершение работы программы
if __name__ == "__main__":
    main()