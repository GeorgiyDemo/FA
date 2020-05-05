"""
Задача 14*:
Создайте двусвязный список (или массив) групп факультета. Каждая группа представляет
собой односвязный список (или массив) студентов.
"""

import yaml


class GetDataClass(object):
    def __init__(self):
        self.processing()

    def processing(self):
        with open("./task14.yml", 'rb') as stream:
            self.d = yaml.safe_load(stream)


class Students(object):
    """
    Класс для создания коллекции студентов в виде односвязанного списка
    Поля:
    - value - значение объекта
    - next - ссылка на след объект в коллекции
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Groups(object):
    """
    Класс для создания коллекции групп в виде двусвязного списка
    Поля:
    - value - имя объекта(название группы)
    - students - значение объекта(список студентов)
    - next - ссылка на след объект в коллекции
    - previous - ссылка на предыдущий объект коллекции
    """

    def __init__(self, value=None, students=None, next=None, previous=None):
        self.value = value
        self.students = students
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.value)


class ProcessingClass(object):

    def __init__(self):
        self.get_data()
        self.processing()

    def get_data(self):
        settings = GetDataClass()
        self.data = settings.d

    def processing(self):
        group_list = []
        for group in self.data:
            student_list = []
            for student in self.data[group]:
                student_list.append(Students(student))
                print("Занесли  '" + student + "' ")

                # Связываем между собой студентов группы
                for i in range(len(student_list) - 1):
                    student_list[i].next = student_list[i + 1]

            group_list.append((group, Groups(group, student_list)))
            print("Занесли студентов группы", group)

            for i in range(len(group_list) - 1):
                group_list[i][1].next = group_list[i + 1][1]
                group_list[i + 1][1].previous = group_list[i][1]

        for group in group_list:

            print("*" * 60)
            print(group[1].previous, "->", group[0], "->", group[1].next)
            print("Элементы группы:")
            for student in group[1].students:
                print(student.value, "->", student.next)


if __name__ == "__main__":
    ProcessingClass()
