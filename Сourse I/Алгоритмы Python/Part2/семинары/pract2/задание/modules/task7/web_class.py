from .publication_class import PublicationClass
class WebClass(PublicationClass):
    """Класс ЭЛЕКТРОННЫЙ РЕСУРС (название, фамилия автора, ссылка, аннотация)"""
    def __init__(self, name, author_name, link, annotation):
        super().__init__(name, author_name)
        self.link = str(link)
        self.annotation = str(annotation)
    def info(self):
        print("Информация об электронном ресурсе\nНазвание: " + self.name + "\nАвтор: " + self.author_name + "\n" + "Ссылка: " + self.link + "\nАннотация" + self.annotation)