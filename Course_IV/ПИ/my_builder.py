class Document:

    def __init__(self):
        print("Начало создания документа\n")
        self.data = ""

    def build_abstract(self) -> str:
        self.data +=  "\nВведение"

    def build_part1(self):
        self.data += "\nГлава 1"

    def build_part2(self):
        self.data += "\nГлава 2"

    def build_part3(self):
        self.data += "\nГлава 3"

    def header(self):
        self.data += "\nЗаголовок"
    
    def content(self):
        self.data += "\n**контент**"

    def summarize(self):
        self.data += "\nВывод"

    def __str__(self) -> str:
        return self.data

class DiplomaBuilder:

    def __init__(self):
        self.build()

    def build(self):
        doc = Document()
        doc.build_abstract()

        doc.build_part1()
        doc.header()
        doc.content()
        doc.header()
        doc.content()
        doc.header()
        doc.content()

        doc.build_part2()
        doc.header()
        doc.content()
        doc.header()
        doc.content()
        doc.header()
        doc.content()

        doc.build_part3()
        doc.header()
        doc.content()
        doc.header()
        doc.content()
        doc.header()
        doc.content()

        doc.summarize()

        print(doc)


class CourseWorkBuilder:

    def __init__(self):
        self.build()

    def build(self):
        doc = Document()
        doc.build_abstract()

        doc.build_part1()
        doc.header()
        doc.content()
        doc.header()
        doc.content()

        doc.build_part2()
        doc.header()
        doc.content()
        doc.header()
        doc.content()

        doc.summarize()

        print(doc)

class ReferatBuilder:

    def __init__(self):
        self.build()

    def build(self):
        doc = Document()
        doc.build_abstract()

        doc.header()
        doc.content()
        doc.header()
        doc.content()
        doc.header()
        doc.content()
        doc.summarize()

        print(doc)

if __name__ == "__main__":

    router_dict = {
        "1": CourseWorkBuilder,
        "2": DiplomaBuilder,
        "3": ReferatBuilder,
    }

    data_input = input("Что вы хотите написать?\n1. Курсовая работа\n2. Диплом\n3. Реферат\n ->")

    if data_input in router_dict:
        router_dict[data_input]()
    
    else:
        print("Некорректный ввод данных")

