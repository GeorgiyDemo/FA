class ExampleClass():
    def __init__(self):
        self.types()
        self.operations()
        self.change_operations()
    
    def types(self):
        """
        Повторение типов в python
        """
        #Получаем тип значения
        type(3253523)
        print(0b11) # целое число, заданное в двоичном формате
        print(0o11) # целое число, заданное в восьмеричном формате
        print(0x11) # целое число, заданное в шестнадцатеричном формате

        # задание вещественного числа в экспоненциальной форме:
        print(4.21e-1)

        # комплексное число:
        print(2+2.1j)

    def operations(self):
        """
        Нетипичные операции в python
        """
        #// - деление с округлением вниз. Вне зависимости от типа чисел остаток отбрасывается.
        print(10 // 5) #Деление целых чисел без остатка 
        print(10 % 5) # Остаток от деление целых чисел
        print(10 ** 2) #Возведение в степень
    
    def change_operations(self):

        check = float(42)
        print(type(check))



if __name__ == "__main__":
    ExampleClass()

