"""
Вычислить сумму N членов ряда, заданного в Приложении 1, согласно номеру варианта.
1. Вывести рекуррентную формулу для расчета очередного слагаемого, а также определить начальные значения для слагаемого и суммы.
2. Разработать блок-схему алгоритма.
3. На языке Python реализовать разработанный алгоритм.
Значения x задаются по вводу с клавиатуры.
Если введённое значение не удовлетворяет заданному ограничению,
вывести в командное окно соответствующее сообщение и повторить ввод.
4. Произвести расчёты для нескольких значений N 
(5≤N≤10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
"""


class MainClass:
    def __init__(self):

        self.x_processing_flag = False
        self.result_sum = 0

        # Ввод данных
        while not self.x_processing_flag:
            self.x_values_input()

        for i in range(5, 11):
            self.calculating(i)
            print("x={}, n={}, sum={}\n".format(self.x, i, self.final_sum))

    def calculating(self, n):
        """
        Метод для вычисления по рекурентной формуле
        """
        x = self.x
        locale_m = -1
        locale_c = 1
        locale_p = 1

        final_sum = 0

        for i in range(0, n):
            # Рекурентные формулы
            if i == 0:
                locale_c = 1
            else:
                locale_c += 1  # знаменатель
            locale_m = -locale_m  # знак
            locale_p = x * locale_p  # числитель
            locale_result = locale_m * locale_p / locale_c
            print("{}*({}/{}) = {}".format(locale_m,
                                           locale_p, locale_c, locale_result))
            final_sum += locale_result

        self.final_sum = final_sum

    def x_values_input(self):
        """
        Метод для ввода данных по x
        """
        try:
            x = float(input("Введите x -> "))
            if x > 1 or x < -1:
                print("Введённое значение не удовлетворяет заданному ограничению")
            else:
                self.x_processing_flag = True
                self.x = x
        except ValueError:
            print("Некорректный ввод данных")


if __name__ == "__main__":
    MainClass()
