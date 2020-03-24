from .publication_class import PublicationClass
class BookClass(PublicationClass):
    """Класс КНИГА (название, фамилия автора, год издания, издательство)"""
    def __init__(self, name, author_name, publish_year, publishing_house):
        super().__init__(name, author_name)
        self.publish_year = str(publish_year)
        self.publishing_house = str(publishing_house)
    def info(self):
        print(
            "Информация о книге\nНазвание:" + self.name + "\nАвтор:" + self.author_name + "\n" + "Год издания:" + self.publish_year + "\nИздательство:" + self.publishing_house)