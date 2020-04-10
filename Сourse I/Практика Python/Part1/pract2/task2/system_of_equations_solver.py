import copy
import pickle
from os import system

oper = '+-'
poweroper = '-'
oper0 = '^'
digit = '1234567890.'


def minus(list1, list2):
    for i in range(len(list1)):
        list1[i] -= list2[i]
    return list1


def devide(list1, n):
    for i in range(len(list1)):
        list1[i] = list1[i] / n
    return list1


def switch(list1, list2, j):
    for i in range(len(list2)):
        list1[i][j], list2[i] = list2[i], list1[i][j]
    return list1


def fill(m, n=1, number=0.1):
    d = []
    if n > 1:
        for i in range(n):
            d.append([])
            for j in range(m):
                d[i].append(number)
    elif n == 1:
        for j in range(m):
            d.append(number)
    return d


def compilator(listt):
    for primer in range(len(listt)):
        left = True
        res = ''
        for i in range(len(listt[primer])):
            if listt[primer][i] == '=':
                left = False
                middle = i
            if not left:
                if listt[primer][i] in digit and listt[primer][middle + 1:i].replace(' ', '') == '':
                    res += '-' + listt[primer][i]
                elif listt[primer][i] == '+':
                    res += '-'
                elif listt[primer][i] == '-':
                    res += '+'
                elif listt[primer][i] == '=':
                    pass
                else:
                    res += listt[primer][i]
            else:
                res += listt[primer][i]
        listt[primer] = res
    for primer in range(len(listt)):
        listt[primer] = listt[primer].replace(' 0 ', '')
        listt[primer] = listt[primer].replace(' ', '')
    return listt


def xfinder(listt):
    dictt1 = {}
    dictt2 = {}
    count = 0
    for primer in listt:
        for s in primer:
            if s not in oper and s not in oper0 and s not in digit and s not in dictt1:
                dictt1[s] = count
                dictt2[count] = s
                count += 1
    return dictt1, dictt2


def solver(dictt, uravnenie, x0):
    summ = 0

    for s in range(len(uravnenie)):
        if uravnenie[s] in digit and (uravnenie[s - 1] not in digit or s == 0):
            start = s
            stop = start
            konst = True

            while konst:
                stop += 1
                try:
                    if uravnenie[stop] not in digit:
                        konst = False
                except IndexError:
                    konst = False

            try:
                if uravnenie[stop] in oper and (uravnenie[start - 1] in oper or start == 0):
                    if uravnenie[start - 1] == '-':
                        start -= 1
                    summ += float(uravnenie[start:stop])
            except IndexError:
                if stop == len(uravnenie) and uravnenie[start - 1] in oper or start == 0 and uravnenie[stop] in oper:
                    if uravnenie[start - 1] == '-':
                        start -= 1
                    summ += float(uravnenie[start:stop])
        elif uravnenie[s] not in oper and uravnenie[s] not in oper0 and uravnenie[s] not in digit:
            k = 1
            power = 1
            if uravnenie[s - 1] in digit and s != 0:
                start = s - 1
                stop = start
                dig = True
                while dig:
                    stop -= 1
                    if uravnenie[stop] not in digit:
                        dig = False
                try:
                    k = float(uravnenie[stop:start + 1])
                except ValueError:
                    k = float(uravnenie[0:start + 1])
            elif uravnenie[s - 1] == '-':
                k = -1
            try:
                if uravnenie[s + 1] in oper0:
                    start = s + 2
                    stop = start
                    poww = True
                    while poww:
                        stop += 1
                        try:
                            if uravnenie[stop] not in digit and uravnenie[stop] not in poweroper or uravnenie[
                                stop - 1] in digit and uravnenie[stop] in poweroper:
                                poww = False
                        except IndexError:
                            poww = False
                    power = float(uravnenie[start:stop])
            except IndexError:
                pass
            try:
                summ += k * (x0[dictt[uravnenie[s]]] ** power)
            except ZeroDivisionError:
                summ = None
                break
    return summ


def f(dictt, listt, x0):
    f = []
    for uravnenie in listt:
        f.append(solver(dictt, uravnenie, x0))
    return f


def dot(list1, list2):
    scalar = 0
    if len(list1) == len(list2):
        for i in range(len(list1)):
            scalar += list1[i] * list2[i]
    return scalar


def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


def Gauss(A, B):
    column = 0
    while (column < len(B)):

        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            return None

        if current_row != column:
            SwapRows(A, B, current_row, column)

        DivideRow(A, B, column, A[column][column])

        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])

        column += 1

    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))

    return X


def jacobian(f, x0, dictt, sistem):
    h = 1.0e-4
    n = len(x0)
    Jac = fill(n, n, 0)
    f0 = copy.copy(f(dictt, sistem, x0))
    for i in range(0, n, 1):
        tt = x0[i]
        x0[i] = tt + h
        f1 = copy.copy(f(dictt, sistem, x0))
        x0[i] = tt
        Jac = switch(Jac, devide(minus(f1, f0), h), i)
    return Jac, f0


def newton(f, x0, dictt, sistem, tol=1.0e-11):
    iterMax = 1000
    for i in range(iterMax):
        Jac, fO = jacobian(f, x0, dictt, sistem)
        if (dot(fO, fO) / len(x0)) ** 0.5 < tol:
            return x0, i
        dx = Gauss(Jac, fO)
        x0 = minus(x0, dx)


def rounded(number, epsilon=10):
    if abs((number // 1) + 1 - number) <= 10 ** (-epsilon + 5):
        return round((number // 1) + 1)
    elif abs(number - (number // 1)) <= 10 ** (-epsilon + 5):
        return round(number // 1)
    else:
        return round(number, epsilon)


with open("sistema.pickle", "rb") as input_file:
    sistem = pickle.load(input_file)

sistem = compilator(sistem)
dictt, reverce = xfinder(sistem)
x0 = fill(len(sistem))

try:
    x, iter = newton(f, x0, dictt, sistem)
    for i in range(len(x)):
        print(f'{"".join(sistem[i])}=0        {reverce[i]} = {rounded(x[i])}')
    print('\n')
except ValueError:
    print("Data isn't correct\n")
except TypeError:
    for i in range(len(sistem)):
        print(f'{"".join(sistem[i])}=0')
    print("No Solution or too many iteration for the Newton method\n")

system("pause")
