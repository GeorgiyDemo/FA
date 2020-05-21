#Деменччук Георгий ПИ19-4 Вариант 6

import math

def math_calculating(x):
    """Математический результат"""

    return_result = math.pi / 2.0 - math.atan(x)
    return return_result
    
def calculating(x_input, e_input=10**-5):
    """Ручные вычисления"""
    
    #Начальные значения
    e = e_input
    a = x_input
    b = 1.0
    c = -1.0
    result = c * a / b
    buffer = 0
    i = 1

    #Вычисляем, пока не достигнем погрешности
    while abs(result - buffer) > e:
        buffer = result
        a = a * pow(x,2)
        b += 2
        #Чередование знака
        c = -c
        #Добавляем результат
        result += c * a / b
        i += 1
    
    #Формируем окончательный результат 
    return_result = math.pi / 2 + result
    return return_result


def main():
    """Основная логика с вызовом"""

    while True:
        try:
            x = float(input('Введите x (x<=1) -> '))
            e = float(input('Введите точность eps (например 0.0001) -> '))
            break
        except ValueError:
            print('Неверный ввод!')

    print("[Результат ручной] {} при e = {}".format(calculating(x,e), e))
    print("[Результат с math] {}".format(math_calculating(x)))

if __name__ == '__main__':
    main()