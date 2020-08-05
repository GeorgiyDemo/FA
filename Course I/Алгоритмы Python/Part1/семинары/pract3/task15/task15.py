"""
Дан список студентов. Элемент списка содержит фамилию, имя, отчество, год рождения, курс, номер группы, 
оценки по пяти предметам. 
Упорядочите студентов по курсу, причем студенты одного курса располагались в алфавитном порядке.

Определите самого старшего студента и самого младшего студентов.
Найдите средний балл каждой группы по каждому предмету. 
Для каждой группы найдите лучшего с точки зрения успеваемости студента.
"""


class MainProcessingClass(object):
    def __init__(self):

        self.student_list = [
            ["Деменчук", "Георгий", "Максимович", "1999", 3, "ПИ19-4", [2, 5, 3, 4, 5]],
            [
                "Анатолий",
                "Анатолий",
                "Анатольевич",
                "1995",
                3,
                "ПИ19-2",
                [2, 5, 3, 4, 5],
            ],
            ["Прищепа", "Екатерина", "Кот", "2001", 1, "ПИ19-2", [5, 4, 5, 3, 5]],
            ["Ваня", "Ваня", "Иванович", "2000", 1, "ПИ18-2", [2, 3, 3, 4, 5]],
        ]
        self.datadict = {"oldest": 9999, "youngest": 0, "data": {}}

        self.processing()
        self.out_data()

    def processing(self):

        datadict = self.datadict
        student_list = self.student_list
        student_list.sort(key=lambda x: (x[4], x[0]))

        for collection in student_list:

            # Проверка на лучшего студента
            best_student = {
                "fio": collection[0] + " " + collection[1] + " " + collection[2],
                "date": collection[3],
                "course": collection[4],
                "sum": sum(collection[6]),
            }

            if collection[5] in datadict["data"]:

                if datadict["data"][collection[5]]["best"]["sum"] < sum(collection[6]):
                    datadict["data"][collection[5]] = {"best": best_student}

                datadict["data"][collection[5]]["subjects"]["sum"] = [
                    sum(x)
                    for x in zip(
                        collection[6],
                        datadict["data"][collection[5]]["subjects"]["sum"],
                    )
                ]

                datadict["data"][collection[5]]["subjects"]["count"] += 1

            else:
                datadict["data"][collection[5]] = {
                    "best": best_student,
                    "subjects": {"count": 1, "sum": collection[6]},
                }

            if int(datadict["youngest"]) < int(collection[3]):
                datadict["youngest"] = collection[3]
            if int(datadict["oldest"]) > int(collection[3]):
                datadict["oldest"] = collection[3]

        for stat in datadict["data"]:
            datadict["data"][stat]["subjects"] = [
                x / datadict["data"][stat]["subjects"]["count"]
                for x in datadict["data"][stat]["subjects"]["sum"]
            ]

        self.student_list = student_list
        self.datadict = datadict

    def out_data(self):
        d = self.datadict
        print("Отсортированный словарь:\n", self.student_list, "\n")
        print(
            "Самый старший студент "
            + d["oldest"]
            + "-го года\nСамый младший студент "
            + d["youngest"]
            + "-го года"
        )
        for group, data in d["data"].items():
            print("\n*Группа " + group + "*")
            b = data["best"]
            print(
                "Луший студент группы:\n" + b["fio"] + " " + b["date"] + ",",
                b["course"],
                "курс,",
                "cумма баллов",
                b["sum"],
            )
            print("Средние баллы группы по предметам:", data["subjects"])


if __name__ == "__main__":
    MainProcessingClass()
