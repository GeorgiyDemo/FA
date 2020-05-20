import math


def m_counter(x):
    # Обратный гиперболический котангенс
    # Его нет в math, пришлось вручную
    result = 1/2*math.log((x+1)/(x-1))
    return result


def counter(x, e):

    # Весь знаменатель, включая N
    C_all = 1
    # Часть знаменателя без N
    C_part = 1
    # N в знаменателе
    N = -1
    # Сумма
    SUM = 0
    # Для цикла
    i = 0

    while True:

        # На 0 итерации степень 1
        if i == 0:
            power = 1
        else:
            power = 2

        # Прибавляем от предыдущего элемента +2 для N
        N += 2

        # Вычисляем знаменатель без N
        C_part *= pow(x, power)

        # Вычисляем знаменатель с N
        C_all = C_part * N

        # Т.к. чилситель 1
        RESULT = 1 / C_all

        print("n="+str(i)+", (1/"+str(C_all)+") = "+str(RESULT))
        SUM += RESULT

        if abs(RESULT) < 10**-e:
            break
        else:
            i += 1

    return SUM, i


# Проверка на ввод x
flag = True

while flag:
    x = float(input("Введите x: "))

    if abs(x) > 1:
        flag = False
    else:
        print("Введённое значение не удовлетворяет условию задачи")

e = int(input("Введите степень погрешности e: "))

result, i = counter(x, e)
print("\nx="+str(x)+" при n="+str(i)+" и e=" +
      str(10**-e)+", результат: "+str(result))
result = m_counter(x)
print("Результат с помощью math.log: "+str(result))
