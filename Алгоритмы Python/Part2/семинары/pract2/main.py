
def main():
    print("Задание 1:", Task1Class.sum(3, 4))
    obj = Task2Class(2, 4)
    print("Задание 2:", obj.sum())

    print("Задание 3:")
    Task3Class()

    print("\nЗадание 4:")
    try:
        x = float(input("Введите x -> "))
    except ValueError:
        print("Проблема ввода данных!")
        return

    obj = Task4Class(x)
    print("Результат: " + str(obj.result))


if __name__ == "__main__":
    main()