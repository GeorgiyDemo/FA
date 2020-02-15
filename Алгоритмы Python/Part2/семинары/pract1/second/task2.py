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

class PublicationClass:
    """
    Класс ИЗДАНИЕ с методом, позволяющим вывести на экран информацию об издании,
    а также определить, является ли данное издание искомым.
    """
    def __init__(self, name, author_name):
        self.name = str(name)
        self.author_name = str(author_name)
    
    def info(self):
        print("Информация об издании\nНазвание:"+self.name+"\nАвтор:"+self.author_name)

class BookClass(PublicationClass):
    """
    Класс КНИГА (название, фамилия автора, год издания, издательство)
    """
    def __init__(self, name, author_name, publish_year, publishing_house):
        super().__init__(name, author_name)
        self.publish_year = str(publish_year)
        self.publishing_house = str(publishing_house)

    def info(self):
        print("Информация о книге\nНазвание:"+self.name+"\nАвтор:"+self.author_name+"\n"+"Год издания:"+self.publish_year+"\nИздательство:"+self.publishing_house)

    
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
        print("Информация о статье\nНазвание:"+self.name+"\nАвтор:"+self.author_name+"\n"+"Год издания:"+self.publish_year+"\nНазвание журнала:"+self.journal_name+"\nНомер журнала"+self.journal_number)

    
class WebClass(PublicationClass):
    """
    Класс ЭЛЕКТРОННЫЙ РЕСУРС (название, фамилия автора, ссылка, аннотация)
    """
    def __init__(self, name, author_name, link, annotation):
        super().__init__(name, author_name)
        self.link = str(link)
        self.annotation = str(annotation)

    def info(self):
        print("Информация об электронном ресурсе\nНазвание:"+self.name+"\nАвтор:"+self.author_name+"\n"+"Ссылка:"+self.link+"\nАннотация"+self.annotation)


def main():
    try:
        n = int(input("Введите количество изданий -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    
    all_publications_list = []
    
if __name__ == "__main__":
    main()

    pass
