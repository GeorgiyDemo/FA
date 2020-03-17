from .task4 import Task4Class
def main():
    print("\nЗадание 4:")
    try:
        x = float(input("Введите x -> "))
    except ValueError:
        print("Проблема ввода данных!")
        return

    obj = Task4Class(x)
    print("Результат: " + str(obj.result))