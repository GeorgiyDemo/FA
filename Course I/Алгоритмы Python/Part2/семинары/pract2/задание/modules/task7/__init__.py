from faker import Faker

from .publication_class import PublicationClass


def main():
    try:
        n = int(input("Введите количество изданий -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    fake, search_flag = Faker(["ru_RU"]), False
    all_publications_list = []
    for _ in range(n):
        all_publications_list.append(PublicationClass(fake.word(), fake.name()))
    for pub in all_publications_list:
        pub.info()
        print()
    search_name = input("Введите фамилию автора для поиска издания -> ")
    for pub in all_publications_list:
        if search_name in pub.author_name:
            print("[Издание найдено]")
            pub.info()
            search_flag = True
    if not search_flag:
        print("Изданий не найдено")
