from modules import task5, task4, task3, task2, task1

def main():
    d_selector = {"1" : task1, "2" : task2, "3" : task3, "4" : task4, "5" : task5}
    input_str = input("Введите номер задания (1-20) ->")
    if input_str in d_selector: d_selector[input_str].main()
    '''
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
'''

if __name__ == "__main__":
    main()