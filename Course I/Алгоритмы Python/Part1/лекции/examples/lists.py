import copy  # подключаем модуль copy

lst_to2_deep = copy.deepcopy(
    [{1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4]}]
)  # делаем полную копию списка
print(lst_to2_deep)

lst_4 = [6, 7] * 11  # все 11 копий ссылаются на одни теже элементы
print(lst_4)

ld = [8]
ld2 = [ld]
lst_t1 = ld2 * 10
print(lst_t1)

lst_8 = lst_9 = [1, 2, 3]
lst_8[0] = 228
print(lst_8)
print(lst_9)
lst_10 = list(lst_8)
print(lst_10)

# Добавляем поэлементно
l = [1, 2, 3]
l.extend([1, 2, 3])
print(l)
l[1:1] = ["A", "B"]
print(l)
l[2:4] = []  # удаление значений
print(l)
