"""
Реализовать текстовый калькулятор для решения тригонометрических уравнения.
Добавить возможность сохранения хода решения в файл. 
Встроенными функциями и библиотечными для решения уравнений и систем пользоваться ЗАПРЕЩЕНО.
"""


class TaskClass:
    def __init__(self, input_exp):
        d_function = dict(
            sin=self.sin_solver,
            cos=self.cos_solver,
            tan=self.tan_solver,
            ctg=self.ctg_solver,
        )
        # Поле результата
        self.r = None
        self.input_exp = input_exp
        self.processing()

        if self.function in d_function:
            d_function[self.function]()
            self.file_writer()
            self.get_result()
        else:
            print("Нет метода такой функции!")

    def file_writer(self):
        """
        Метод для записи исходного выражения в файл
        """
        result_str = (
            "Входные данные\n"
            + self.input_exp
            + "\nЗначение:"
            + str(self.number)
            + "\nФункция:"
            + self.function
            + "\nКоэффициент:"
            + str(self.koff)
            + "\n\nОтвет:\n"
            + str(self.r)
            + "\n"
        )
        with open("result.txt", "w") as f:
            f.write(result_str)

    def processing(self):
        """
        Метод-парсер исходного выражения

        - Определяет коэффициент
        - Определяет значение
        - Определяет функцию
        """

        exp = self.input_exp
        self.number = float(exp[exp.find("=") + 1 : len(exp)])

        function = exp[0:3]
        self.function = function
        if exp.find("x") - exp.find("(") == 1:
            self.koff = 1
        else:
            self.koff = float(exp[exp.find("(") + 1 : exp.find("x")])

    def get_result(self):
        """
        Метод для вывода результатов выполнения на экран
        """
        print("Входные данные:", self.input_exp)
        print("Значение:", self.number)
        print("Функция:", self.function)
        print("Коэффициент:", self.koff)
        print("\nОтвет:\n" + self.r)

    def sin_solver(self):
        """
        Метод для решения триг. уравнений с функцией sin
        """
        number = self.number
        k = self.koff
        d_number = {
            0.5: "π/"
            + str(6 * k)
            + "+2πk"
            + "/"
            + str(k)
            + "\n"
            + "(5π/"
            + str(6 * k)
            + "+2πk)"
            + "/"
            + str(k),
            0.7: "π/"
            + str(4 * k)
            + "+2πk"
            + "/"
            + str(k)
            + "\n"
            + "(3π/"
            + str(4 * k)
            + "+2πk)"
            + "/"
            + str(k),
            0.866: "π/"
            + str(3 * k)
            + "+2πk"
            + "/"
            + str(k)
            + "\n"
            + "(2π/"
            + str(3 * k)
            + "+2πk)"
            + "/"
            + str(k),
            -0.5: "-π/"
            + str(6 * k)
            + "+2πk"
            + "/"
            + str(k)
            + "\n"
            + "(-5π/"
            + str(6 * k)
            + "+2πk)"
            + "/"
            + str(k),
            -0.7: "-π/"
            + str(4 * k)
            + "+2πk"
            + "/"
            + str(k)
            + "\n"
            + "(-3π/"
            + str(4 * k)
            + "+2πk)"
            + "/"
            + str(k),
            -0.866: "-π/"
            + str(3 * k)
            + "+2πk"
            + "/"
            + str(k)
            + "\n"
            + "(-2π/"
            + str(3 * k)
            + "+2πk)"
            + "/"
            + str(k),
        }
        self.r = (
            d_number[number]
            if number in d_number
            else "(arcsin("
            + str(number)
            + ")+2πk)"
            + "/"
            + str(k)
            + "\n"
            + "(π-arcsin("
            + str(number)
            + ")+2πk)"
            + "/"
            + str(k)
        )

    def cos_solver(self):
        """
        Метод для решения триг. уравнений с функцией cos
        """
        number = self.number
        k = self.koff
        d_number = {
            0.866: "+-π/" + str(6 * k) + "+2πk" + "/" + str(k),
            0.7: "+-π/" + str(4 * k) + "+2πk" + "/" + str(k),
            0.5: "+-π/" + str(3 * k) + "+2πk" + "/" + str(k),
            -0.5: "+-2π/" + str(3 * k) + "+2πk" + "/" + str(k),
            -0.866: "+-5π/" + str(6 * k) + "+2πk" + "/" + str(k),
            -0.7: "+-3π/" + str(4 * k) + "+2πk" + "/" + str(k),
        }
        self.r = (
            d_number[number]
            if number in d_number
            else "(+-arccos(" + str(number) + ")+2πk)" + "/" + str(k)
        )

    def tan_solver(self):
        """
        Метод для решения триг. уравнений с функцией tg
        """
        number = self.number
        k = self.koff
        d_number = {
            0.577: "π/" + str(6 * k) + "+πk" + "/" + str(k),
            1: "π/" + str(4 * k) + "+πk" + "/" + str(k),
            1.732: "π/" + str(3 * k) + "+πk" + "/" + str(k),
            -0.577: "-π/" + str(6 * k) + "+πk" + "/" + str(k),
            -1: "-π/" + str(4 * k) + "+πk" + "/" + str(k),
            -1.732: "-π/" + str(3 * k) + "+πk" + "/" + str(k),
        }
        self.r = (
            d_number[number]
            if number in d_number
            else "(arctan(" + str(number) + ")+πk)" + "/" + str(k)
        )

    def ctg_solver(self):
        """
        Метод для решения триг. уравнений с функцией ctg
        """
        number = self.number
        k = self.koff
        d_number = {
            0.577: "π/" + str(3 * k) + "+πk" + "/" + str(k),
            1: "π/" + str(4 * k) + "+πk" + "/" + str(k),
            1.732: "π/" + str(6 * k) + "+πk" + "/" + str(k),
            -0.577: "2π/" + str(3 * k) + "+πk" + "/" + str(k),
            -1: "3π/" + str(4 * k) + "+πk" + "/" + str(k),
            -1.732: "5π/" + str(6 * k) + "+πk" + "/" + str(k),
        }
        self.r = (
            d_number[number]
            if number in d_number
            else "(arctan(" + str(number) + ")+πk)" + "/" + str(k)
        )


if __name__ == "__main__":
    exp = input("-> ")
    # exp = "cos(x)=0.5"
    TaskClass(exp)
