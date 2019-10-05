d = {"MEOW": 222, "KOT": 3240}
# ПРАВИЛЬНЫЙ обход пар ключ-значение:
for k, v in d.items():
    print('key: {}, value: {}'.format(k, v))
# Получаем значение с помощью get
print(d.get("MEOW"))

d["KEY"] = 1
d.update([('a', 6), ('b', 4)])
check = list(zip(('a', 6), ('b', 4)))

example = (6, 6, 1, 1, 2, 4, 5, 5, 7, 6, 6, 6,)
print(example)
d = {}
d[tuple(list(set(example)))] = "CAT"
d[None] = "CAR"

print(d)

# SET
s3 = {1, 2, 3, 4}
s4 = {2, 4, 5, 6}
# Объединение множеств:
out = s3 | s4
print(out)
# Пересечение множеств
out = s4 & s3
print(out)

# Все элементы обоих множеств, исключая одинаковые элементы.
out = {3, 4, 5, 6} ^ {5, 6, 7, 8}

j = [1 for c in range(10)]
i = [[1 for c in range(10)] for r in range(10)]
print(j)

meow = ((1), (2))
if 2 not in meow:
    print("ЕСТЬ 2")


# возвращаемое значение функции может быть кортежем:
def my_func(a):
    return (a, a + 1)


print(my_func(2))

# распаковка элементов
x = 10
y = 1
print(x, y)
y, x = x, y
print(x, y)
a, *b, c = range(10, 16)
print(a, b, c)

print("------")
print([(1, 2, 3), (4, 5, 6, 7), (9,)])
for a, *b in [(1, 2, 3), (4, 5, 6, 7), (9,)]:
    print('a = {}, b = {}'.format(a, b))

keys = ['a', 'b']  # Список с ключами
values = [1, 2]  # Список со  значениями 
d18 = {k: v for (k, v) in zip(keys, values)}
