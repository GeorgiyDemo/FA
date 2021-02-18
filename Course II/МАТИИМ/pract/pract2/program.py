"""
Диагональная матрица 
Рассчет установившейс вероятности для непрерывных марковских процессов
"""
import numpy as np
import copy

#L = int(input("Введите интенсивность поступления требований -> ")) #Лямбда
#u = int(input("Введите интенсивность обслуживания требований одним каналом -> "))
#m = int(input("Количество каналов -> "))
#n = int(input("Количество мест в очереди -> "))

L = 29
m = 7
u = 6
n = 6

"""Матрица переходов"""
p_matrix = np.zeros((m + n + 1, m + n + 1))
for i in range(m + n):
    p_matrix[i, i + 1] = L
    if i < m:
        p_matrix[i + 1, i] = (u * (i + 1))
    else:
        p_matrix[i + 1, i] = u*m

print("Матрица переходов")
print(p_matrix)

"""Установившиеся вероятности"""

#Диагональная матрица
print("Диагональна матрица из сумм строк матрицы интенсивности переходов")
result = []
for i in range(p_matrix.shape[0]):
    result.append(p_matrix[i, :].sum())
D = np.diag(result)
print(D)


M = p_matrix.T - D
print("Перед заменой единицы")
print(M)
M_ = copy.deepcopy(M)
M_[-1, :] = 1
print("После замены единицы")
print(M_)

b_matrix = np.zeros(M_.shape[0])
b_matrix[-1] = 1

X_RESULT = np.linalg.inv(M_).dot(b_matrix)
print("Установившиеся вероятности")
print(X_RESULT)
print("Сумма: ", X_RESULT.sum())

print("Вероятность отказа в обслуживании", X_RESULT[-1])
print("Относительная пропускная способность = ", 1 - X_RESULT[-1])
print("Абсолютная пропускная способность = ", (1 - X_RESULT[-1]) * L)
print("Средняя длина")
#TODO ДОДЕЛАТЬ СРЕДНЯЯ ДЛИНА ОЧЕРЕДИ
#TODO СРЕДНЕЕ ВРЕМЯ В ОЧЕРЕДИ
#СРЕДНЕЕЕ КОЛ-ВО ЗАНЯТЫХ КАНАЛОВ
#СУММА УСТАНОВИВШИХСЯ ВЕРОЯТНОСТЕЙ ОТ з ДО M-1