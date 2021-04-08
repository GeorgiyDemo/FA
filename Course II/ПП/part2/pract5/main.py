import multiprocessing as mp
import yaml
import random
from typing import List

MATRIX1_FILE = "./data/matrix1.yml"
MATRIX2_FILE = "./data/matrix2.yml"
RESULT_FILE = "./data/result.yml"


def print_matrix(matrix: List[List[int]]) -> None:
    """Вывод матрицы на экран"""
    r = "\n" + "\n".join(["\t".join([str(cell) for cell in row]) for row in matrix])
    print(r)


def matrix_reader(file_name: str) -> List[List[int]]:
    """Читает матрицу из уазанного файла"""
    with open(file_name, "r") as file:
        return yaml.safe_load(file)


def matrix_writer(matrix: List[List[int]], file_name: str) -> None:
    """Записывает матрицу в указанный файл"""
    with open(file_name, "w") as file:
        yaml.safe_dump(matrix, file)


def matrix_gen(n: int, m: int) -> List[List[int]]:
    """Генерация матрицы"""
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(1, 100))
    return matrix


def worker(i: int, j: int, A: list, B: list, que: mp.Queue) -> None:
    """
    Обработчик перемножения элементов матрицы
    Запускается в отдельном процессе
    """

    buffer_list = []
    for k in range(len(A[0]) or len(B)):
        buffer_list.append(A[i][k] * B[k][j])

    result_dict = {}
    result_dict["result"] = sum(buffer_list)
    result_dict["i"] = i
    result_dict["j"] = j

    que.put(result_dict)


def new_matrix_input():
    """Логика генерации новой матрицы"""
    n = int(input("Введите кол-во строк в матрице -> "))
    m = int(input("Введите кол-во столбцов в матрице -> "))

    # Генерируем
    matrix1 = matrix_gen(n, m)
    matrix2 = matrix_gen(m, n)

    # Пишем в файлы
    matrix_writer(matrix1, MATRIX1_FILE)
    matrix_writer(matrix2, MATRIX2_FILE)
    return matrix1, matrix2


def old_matrix_input():
    """Логика чтения уже существующих матриц из файлов"""
    return matrix_reader(MATRIX1_FILE), matrix_reader(MATRIX2_FILE)


def main():

    manager = mp.Manager()
    commands_dict = {
        "1": old_matrix_input,
        "2": new_matrix_input,
    }

    matrix1 = None
    matrix2 = None

    while True:
        command_input = input(
            "Как вы хотите получить данные матриц?\n1. Загрузить из файла\n2. Сгенерировать новые значения\n-> "
        )
        if command_input in commands_dict:
            matrix1, matrix2 = commands_dict[command_input]()
            break
        else:
            print("Команда не найдена")

    matrix_result = [
        [0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix2[0]))
    ]

    print_matrix(matrix1)
    print_matrix(matrix2)

    # Список процессов
    processes_list = []
    # Очередь ответов
    que = manager.Queue()

    for i in range(len(matrix_result)):
        for j in range(len(matrix_result[i])):
            p = mp.Process(
                target=worker,
                args=(
                    i,
                    j,
                    matrix1,
                    matrix2,
                    que,
                ),
            )
            processes_list.append(p)

    for p in processes_list:
        p.start()
    for p in processes_list:
        p.join()

    for i in range(len(matrix_result)):
        for j in range(len(matrix_result[i])):
            r = que.get()
            matrix_result[r["i"]][r["j"]] = r["result"]

    print_matrix(matrix_result)
    matrix_writer(matrix_result, RESULT_FILE)


if __name__ == "__main__":
    main()
