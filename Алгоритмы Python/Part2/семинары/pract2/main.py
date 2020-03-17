from modules import task5, task4, task3, task2, task1
def main():
    d_selector = {"1" : task1, "2" : task2, "3" : task3, "4" : task4, "5" : task5}
    input_str = ""
    while input_str != "0":
        input_str = input("\033[93mВведите номер задания (1-20) или 0 для завершения работы -> \033[0m")
        if input_str in d_selector: d_selector[input_str].main()
if __name__ == "__main__":
    main()