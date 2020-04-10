def check(b):
    print(b)


fl = lambda: 10 + 20  # функция без nараметров 
f2 = lambda х, y: х + y  # функция с двумя nараметрами
f3 = lambda х, y, z: х + y + z  # функция с тремя nараметрами

print(fl())
print(f2(5, 10))
print(f3(5, 10, 30))


def c_summa(*t, **d):
    for v in t:
        print(v, end=" ")
    for k, v in d.items():
        print("{} => {}".format(k, v), end=" ")


t4 = [10, 20, 30, 40, 50, 60, 70]
d3 = {'f': 3, 'g': 4, 'e': 5}
##Передача слоаря
c_summa(*t4, **d3)


###Глобальные переменные
def func_glob(glob2):
    print("Значение  глобальной  nеременной  g1оb = ", glob)
    glob2 += 10
    print("Значение  локальной  переменной  g1ob2 = ", glob2)


glob, glob2 = 10, 5
func_glob(77)  # Вызываем функцию
print("Значение  глобальной  переменной  g1ob2 = ", glob2)


def func():
    loc = 77  # Локальная  переменная
    glob = 25  # Локальная  переменная
    print('Значение glob внутри функции: ', glob)


glob = 10  # Глобальная  переменная
func()  # Вызываем функцию
print("Значение glob вне  функции: ", glob)
try:
    print(loc)  # Вызовет  исключение  NameError
except NameError:  # Обрабатьrnаем исключение
    print("Переменная 1ос не видна вне функции")


###Необязательные параметры
def summa(x=1, y=2):
    return x + y


print(summa())
print(summa(2))
print((summa(3, 3)))
# Передача топ
print(summa(y=8))


# лирическое отступление
def foo():
    def local_f(a, b):
        return a + b

    return local_f


test = foo()
test(4, 5)

print("*********")


# распаковывание последовательности в списке параметров функции:
def summa(a, b):
    return a + b

    # res = 0
    # for i in t:
    #    res += i 
    # return  res


d = {"a": 1, "b": 2}
print(summa(**d))


# распаковывание последовательности в списке параметров функции:
def all_summa(*t):
    """Функция принимает произвольное количество параметров"""
    res = 0
    for i in t:
        res += i
    return res


# Принимает все
def KOT(*t, **d):
    for v in t:
        print(v, end=" ")
    for k, v in d.items():
        print("{} => {}".format(k, v), end=" ")


print(KOT({"KOT": 2, "MEOW": 2}))
print(KOT([2, 2, 3]))

print(globals())


##Если передали неизменяемый объект - функция его не изменит
def func():
    loc = 54
    glob2 = 25
    print("Локальные идентификаторы внутри  функции", sorted(vars().keys()))


func()

print(vars())
