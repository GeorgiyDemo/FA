class TaskClass():
    def __init__(self, input_exp):

        self.r = None

        d_function = {
            "sin": self.sin_solver,
            "cos": self.cos_solver,
            "tan": self.tan_solver,
            "ctg": self.ctg_solver,
        }
        exp = input_exp
        self.number = float(exp[exp.find("=") + 1:len(exp)])

        function = exp[0:3]

        if exp.find("x") - exp.find("(") == 1:
            self.koff = 1
        else:
            self.koff = float(exp[exp.find("(") + 1:exp.find("x")])

        print("Значение:", self.number)
        print("Функция:", function)
        print("Коэффициент:", self.koff)

        if function in d_function:
            d_function[function]()
            self.get_result()
        else:
            print("Нет метода такой функции!")

    def get_result(self):
        print("\nОтвет:\n" + self.r)

    def sin_solver(self):
        number = self.number
        k = self.koff
        d_number = {
            0.5: "π/" + str(6 * k) + "+2πk" + "/" + str(k) + "\n" + "(5π/" + str(6 * k) + "+2πk)" + "/" + str(k),
            0.7: "π/" + str(4 * k) + "+2πk" + "/" + str(k) + "\n" + "(3π/" + str(4 * k) + "+2πk)" + "/" + str(k),
            0.866: "π/" + str(3 * k) + "+2πk" + "/" + str(k) + "\n" + "(2π/" + str(3 * k) + "+2πk)" + "/" + str(k),
            -0.5: "-π/" + str(6 * k) + "+2πk" + "/" + str(k) + "\n" + "(-5π/" + str(6 * k) + "+2πk)" + "/" + str(k),
            -0.7: "-π/" + str(4 * k) + "+2πk" + "/" + str(k) + "\n" + "(-3π/" + str(4 * k) + "+2πk)" + "/" + str(k),
            -0.866: "-π/" + str(3 * k) + "+2πk" + "/" + str(k) + "\n" + "(-2π/" + str(3 * k) + "+2πk)" + "/" + str(k),
        }

        if number in d_number:
            self.r = d_number[number]
        else:
            self.r = "(arcsin(" + str(number) + ")+2πk)" + "/" + str(
                k) + "\n" + "(π-arcsin(" + number + ")+2πk)" + "/" + str(k)

    def cos_solver(self):
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

        if number in d_number:
            self.r = d_number[number]
        else:
            self.r = "(+-arccos(" + str(number) + ")+2πk)" + "/" + str(k)

    def tan_solver(self):
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

        if number in d_number:
            self.r = d_number[number]
        else:
            self.r = "(arctan(" + str(number) + ")+πk)" + "/" + str(k)

    def ctg_solver(self):

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

        if number in d_number:
            self.r = d_number[number]
        else:
            self.r = "(arctan(" + str(number) + ")+πk)" + "/" + str(k)


if __name__ == "__main__":
    exp = input("-> ")
    # exp = "cos(x)=0.5"
    TaskClass(exp)