class MatrixClass():
    def __init__(self):
        self.generator()
        self.get_4on4()

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

    def generator(self):

        max = 7
        matrix = []
        for i in range(max):
            s = input("->").split(" ")
            s.sort(reverse=True)
            matrix.append(s)
        self.matrix = matrix
        self.show_matrix("Исходная матрица:")


if __name__ == "__main__":
    MatrixClass()