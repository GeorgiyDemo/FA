"""
Задача 2. Создайте класс ИЗДАНИЕ с методом, позволяющим вывести на экран информацию об издании,
а также определить, является ли данное издание искомым.

Создайте дочерние классы КНИГА (название, фамилия автора, год издания, издательство),
СТАТЬЯ (название, фамилия автора, название журнала, его номер и год издания),
ЭЛЕКТРОННЫЙ РЕСУРС (название, фамилия автора, ссылка, аннотация) со своими методами вывода информации 
на экран.

Создайте список из п изданий, выведите полную информацию из списка,
а также организуйте поиск изданий по фамилии автора. 
"""
from faker import Faker


class PublicationClass:
    """
    Класс ИЗДАНИЕ с методом, позволяющим вывести на экран информацию об издании,
    а также определить, является ли данное издание искомым.
    """

    def __init__(self, name, author_name):
        self.name = str(name)
        self.author_name = str(author_name)

    def info(self):
        print("Информация об издании\nНазвание:" + self.name + "\nАвтор:" + self.author_name)


class BookClass(PublicationClass):
    """
    Класс КНИГА (название, фамилия автора, год издания, издательство)
    """

    def __init__(self, name, author_name, publish_year, publishing_house):
        super().__init__(name, author_name)
        self.publish_year = str(publish_year)
        self.publishing_house = str(publishing_house)

    def info(self):
        print(
            "Информация о книге\nНазвание:" + self.name + "\nАвтор:" + self.author_name + "\n" + "Год издания:" + self.publish_year + "\nИздательство:" + self.publishing_house)


class ArticleClass(PublicationClass):
    """
    Класс СТАТЬЯ (название, фамилия автора, название журнала, его номер и год издания),
    """

    def __init__(self, name, author_name, publish_year, journal_name, journal_number):
        super().__init__(name, author_name)
        self.publish_year = str(publish_year)
        self.journal_name = str(journal_name)
        self.journal_number = str(journal_number)

    def info(self):
        print(
            "Информация о статье\nНазвание:" + self.name + "\nАвтор:" + self.author_name + "\n" + "Год издания:" + self.publish_year + "\nНазвание журнала:" + self.journal_name + "\nНомер журнала" + self.journal_number)


class WebClass(PublicationClass):
    """
    Класс ЭЛЕКТРОННЫЙ РЕСУРС (название, фамилия автора, ссылка, аннотация)
    """

    def __init__(self, name, author_name, link, annotation):
        super().__init__(name, author_name)
        self.link = str(link)
        self.annotation = str(annotation)

    def info(self):
        print(
            "Информация об электронном ресурсе\nНазвание: " + self.name + "\nАвтор: " + self.author_name + "\n" + "Ссылка: " + self.link + "\nАннотация" + self.annotation)


def main():
    try:
        n = int(input("Введите количество изданий -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    fake = Faker(['ru_RU'])
    all_publications_list = []

    for _ in range(n):
        all_publications_list.append(PublicationClass(fake.word(), fake.name()))

    for pub in all_publications_list:
        pub.info()
        print()

    search_name = input("Введите фамилию автора для поиска издания -> ")
    search_flag = False

    for pub in all_publications_list:
        if search_name in pub.author_name:
            print("[Издание найдено]")
            pub.info()
            search_flag = True

    if search_flag == False:
        print("Изданий не найдено")


if __name__ == "__main__":
    main()
