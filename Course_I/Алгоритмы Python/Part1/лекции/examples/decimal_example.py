import decimal


class DecimalClass(object):
    def __init__(self):
        self.m()

    def m(self):
        a = decimal.Decimal(39595)
        b = decimal.Decimal(354363.430643693496933364636)
        self.result = a + b


if __name__ == "__main__":
    o = DecimalClass()
    print(o.result)
