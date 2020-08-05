x = 0
try:  # Обрабатьшаем исключения
    х = 1 / 0  # Ошибка: деление на 0
except (NameError, IndexError, ZeroDivisionError) as err:
    print(err.__class__.__name__)  # Название  класса  исключения
    print(err)  # Текст сообщения об ошибке

x = 0
try:  # Обрабатьшаем исключения
    try:  # Вложенньм обработчик
        х = 1 / 0  # Ошибка: деление на 0
    except NameError:
        print("Неоnределенный идентификатор")
    except IndexError:
        print("Несуществующий индекс")
    print("Bыpaжeниe после вложенного обработчика")
except ZeroDivisionError:
    print("Обработка деления на 0")
    х = 0
print(x)  # Выведет:

"""
Для получения  информации об исключении можно воспользоваться функцией ехс_info() из модуля sys, которая возвращает кортеж из трех элементов: типа исключения, значения и объекта с трассировочной информацией. Преобразовать эти значения в удобочитаемый вид позволяет модуль traceback. 
"""
import sys

x = 0
try:  # Обрабатьшаем исключения
    х = 1 / 0  # Ошибка: деление на 0
except ZeroDivisionError as err:
    etype, value, trace = sys.exc_info()
    print(etype, value, trace)

try:
    raise ValueError("Onиcaниe исключения")
except ValueError as msg:
    print(msg)  # Выведет: Описание исключения

##########################################################
CHECK_FLAG = True
try:
    assert CHECK_FLAG, "CHECK_FLAG ИСКЛЮЧЕНИЕ БРАТ"
except AssertionError as err:
    print(err)  # Выдает: Сообщение об ошибке


# Пример использования assert
def factorial(n):
    """Возвращает Факториал числа n.
    Аргумент n - не отрицательное целое число."""
    assert n >= 0, "Аргумент n должен быть больше 0!"
    assert n % 1 == 0, "Аргумент n должен быть целым!"
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


factorial(5.5)
