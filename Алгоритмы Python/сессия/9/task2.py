"""
(15 баллов) Напишите функцию, которая для строки вида 
«Иванов: 100, 45, 89 вычисляет сумму баллов.
Строка является параметром функции.
Функция возвращает вычисленное целое число.
(15 баллов) Текстовый файл Оценки.txt содержит строки указанного вида.
Используя данные этого файла и созданную функцию,
создайте новый файл, в котором строки упорядочены в порядке убывания суммы баллов.
"""

def counter(input_str):
    
    #Разделение строки на список и определение переменных
    name, values = input_str.split(": ")

    #Список кол-вом баллов
    values_list = values.split(", ")

    #Конвертация каждого элемента списка в целочисленный тип
    values_list = [int(x) for x in values_list]

    #Возврат суммы баллов
    return sum(values_list)


if __name__ == "__main__":

    #Открываем файл оценки.txt на чтение
    with open("./Оценки.txt", "r") as file:
        result = file.read()
    
    #Делаем список строк по разделителю \n
    results_list = result.split("\n")

    #Цикл по каждому элементу 
    for i in range(len(results_list)):

        #Получаем сумму с помощью функции
        element_sum = counter(results_list[i])

        #Переопределяем элемент в виде словаря
        results_list[i] = {"sum": element_sum, "value" : results_list[i]}

    #Сортировка в порядке убывания суммы
    results_list.sort(key=lambda x: x["sum"], reverse = True)
    print(results_list)

    #Определение списка для последующей записи в файл
    final_list = [x["value"] for x in results_list]
    
    #Перевод списка в строку
    final_str = "\n".join(final_list)
    
    #Открываем файл результат.txt на напись
    with open("./результат.txt", "w") as file:
        
        #Записываем строку final_str
        file.write(final_str)