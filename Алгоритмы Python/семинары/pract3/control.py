def main():

    max = 7
    matrix = []
    for i in range(max):
        s = input("->").split(" ")
        s.sort(reverse=True)
        matrix.append(s)

    buf = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            buf +=" "+ str(matrix[i][j])
        buf += "\n"
    print(buf)

main()