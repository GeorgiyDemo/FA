"""
4) Объедините программный код в одну программу с меню выбора действия для пользователя.
"""
import task1
import task2
import task3


def main():
    selector_dict = {
        "1": task1,
        "2": task2,
        "3": task3,
    }
    input_str = ""
    while input_str != "0":
        input_str = input("\033[93mВведите номер задания (1-3) или 0 для завершения работы -> \033[0m")
        if input_str in selector_dict:
            selector_dict[input_str].MainClass()
        else:
            print("Такого номера не существует!")


if __name__ == "__main__":
    main()
