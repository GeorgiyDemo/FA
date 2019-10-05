class ExampleClass(object):

    def __init__(self, number):
        self.X = int
        self.number = number

    def get_number(self):
        return self.X(self.number)


def main():
    dict_example = {}

    obj = ExampleClass(20.123)
    print(type(ExampleClass))
    dict_example[ExampleClass] = str(obj.get_number())
    print(dict_example)


if __name__ == "__main__":
    main()
