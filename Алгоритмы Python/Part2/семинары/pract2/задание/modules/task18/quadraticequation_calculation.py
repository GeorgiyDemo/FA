import math
def calculation(a, b, c):
    try:
        equation_results_list = [] 
        D = b ** 2 - 4 * a * c
        if D == 0:
            A1 = -b / (2 * a)
            A2 = A1
            equation_results_list.append(A1)
            equation_results_list.append(A2)
        elif D > 0:
            A1 = (-b + math.sqrt(D)) / (2 * a)
            A2 = (-b - math.sqrt(D)) / (2 * a)
            equation_results_list.append(A1)
            equation_results_list.append(A2)
        else: equation_results_list.append("Нет решения, D < 0")
        return equation_results_list
    except ZeroDivisionError:
        return ["Даление на 0!"]