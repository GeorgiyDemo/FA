class MatrixClass():
    def __init__(self):
        self.except_flag = True
        self.generator()
        if self.except_flag:
            self.get_4on4()
            self.sum_E1()
            self.sum_E2()
        else:
            print("Необходима квадратная матрица!")

    def sum_E1(self):
        s = 0
        for i in range(len(self.matrix)):
            s += self.matrix[i][len(self.matrix) - 1 - i]
        print("Сумма элементов на побочной диагонали:\n"+str(s))
        
    def sum_E2(self):
        s = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j < i and (i+j > len(self.matrix)-1):
                    s += self.matrix[i][j]

        print("Сумма элементов нижнего треугольника:\n"+str(s))

    def get_4on4(self):
        buf_matrix = []
        for i in range(4):
            buf = []
            for j in range(4):
                buf.append(self.matrix[i][j])
            buf.sort(reverse=True)
            buf_matrix.append(buf)

        for i in range(len(buf_matrix)):
            for j in range(len(buf_matrix[i])):
                self.matrix[i][j] = buf_matrix[j][i]
        
        self.show_matrix("Исходная матрица после сортировки квадрата 4x4:")

    def show_matrix(self, out_text=""):
        matrix = self.matrix
        print(out_text)
        buf = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                buf +=" "+ str(matrix[i][j])
            buf += "\n"
        print(buf)

    def check_digit(self, e):
        try:
            return int(e)
        except:
            return e

    def generator(self):

        max = 8
        matrix = []
        for _ in range(max):

            s = [self.check_digit(x) for x in input("->").split(" ")]
            if len(s) != max:
                self.except_flag = False
            s.sort(reverse=True)
            matrix.append(s)

        self.matrix = matrix
        self.show_matrix("Исходная матрица:")


if __name__ == "__main__":
    MatrixClass()