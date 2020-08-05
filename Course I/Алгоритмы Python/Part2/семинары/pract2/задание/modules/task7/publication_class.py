class PublicationClass:
    """
    Класс ИЗДАНИЕ с методом, позволяющим вывести на экран информацию об издании,
    а также определить, является ли данное издание искомым.
    """

    def __init__(self, name, author_name):
        self.name = str(name)
        self.author_name = str(author_name)

    def info(self):
        print(
            "Информация об издании\nНазвание:"
            + self.name
            + "\nАвтор:"
            + self.author_name
        )
