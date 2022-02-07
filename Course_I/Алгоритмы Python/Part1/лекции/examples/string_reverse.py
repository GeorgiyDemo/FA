# TODO Разобраться что происходит с итератором __next__


class Series(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


n_list = Series(1, 10)
print(list(n_list))

s = "MEOW"
print(s)
s = s[::-1]
print(s)

elements = ["element1", "element2", "element3"]
s = "->".join(elements)
print(s)
s = "->".join(reversed(elements))
print(s)

s = s * 5
print(s)
s = "meow"
# boolval = s.count("m",6) s[:6]

product = 1
i = iter([1, 2, 4])
# расчет произведения всех элементов кортежа (аналог цикла for реализованный в цикле while):
while True:
    try:
        product *= next(i)
    except StopIteration:
        break
print(product)

st = "Hello world"
for e in enumerate(st):
    print(str(e) + " index: " + str(e[0]) + " char: " + e[1])

for ind, symb in enumerate(st):
    print("Symbol '{}' has index {}".format(symb, ind))

filelist = ["meow.png", "check.pdf", "cat.png"]
for f in filelist:
    if f.endswith(".png"):
        print(f, "является изображением")
