from .publication_class import PublicationClass


class ArticleClass(PublicationClass):
    """Класс СТАТЬЯ (название, фамилия автора, название журнала, его номер и год издания),"""

    def __init__(self, name, author_name, publish_year, journal_name, journal_number):
        super().__init__(name, author_name)
        self.publish_year = str(publish_year)
        self.journal_name = str(journal_name)
        self.journal_number = str(journal_number)

    def info(self):
        print(
            "Информация о статье\nНазвание:" + self.name + "\nАвтор:" + self.author_name + "\n" + "Год издания:" + self.publish_year + "\nНазвание журнала:" + self.journal_name + "\nНомер журнала" + self.journal_number)
