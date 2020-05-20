import math 

def math_calculating(x):
    """
    Метод для вычисления с помощью математического модуля
    """
    return math.log(x)

def calculating(x, e):
    """
    Метод для вычисления по рекурентной формуле
    """
    #Весь знаменатель, включая N
    locale_c = 1
    #Часть знаменателя без N
    locale_c_part = 1 
    #N в знаменателе
    locale_n = -1
    #Числитель 
    locale_p = 1
    #Сумма
    final_sum = 0
    #Переменная счетчика
    i = 0
    
    while True:
        
        #На 0 итерации все 1 т.к. предыдущего элемента нет
        if i == 0:
            locale_pow = 1
        
        #Иначе, если все остальные итерации
        else:
            locale_pow = 2
        
        #Прибавляем от предыдущего элемента +2 для N
        locale_n = locale_n+2
        #Вычисляем числитель
        locale_p = pow(x-1, locale_pow) * locale_p
        #Вычисляем знаменатель без N
        locale_c_part = locale_c_part * pow(x+1, locale_pow)
        #Вычисляем знаменатель с N
        locale_c = locale_c_part * locale_n
        
        locale_result = locale_p / locale_c
        print("Итерация №{} ({}/{}) = {}".format(i, locale_p, locale_c, locale_result))
        final_sum += locale_result
        
        if abs(locale_result) < 10**-e:
            break
        else:
            i = i + 1
    
    #*2 т.к. по заданию
    return i, 2*final_sum

def main():

    # Проверка на ввод x
    x_flag = False
    while x_flag == False:
        x = float(input("Введите x: "))

        if x <= 0:
            print("Введённое значение не удовлетворяет заданному ограничению")
        else:
            x_flag = True
    
    e_flag = False
    while e_flag == False:
        try:
            e = int(input("Введите степень погрешности e: "))
            e_flag = True
        except ValueError:
            continue

    # Вызов функций
    i, result = calculating(x,e)
    print("\nx={}, n={}, результат: {}".format(x, i, result))
    
    result = math_calculating(x)
    print("Результат с помощью math.log: {}".format(result))

if __name__ == "__main__":
    main()
