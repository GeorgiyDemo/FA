from math import fabs

while True:
    try:
        x = float(input('x = '))
        L = 1
        C = 2*x**2
        P = 2
        T = L*(C/P)
        S = T
        i = 1
        E = float(input('e = '))
        while fabs(T) > E:
            i += 1
            L = -L
            P = P*(2*i-1)*(2*i)
            C = 4*(x**2)*C
            T = L*(C/P)
            S += T
        print('Значение ряда при E = ' + str(E) + ': ' + str(S))
        break
    except ValueError:
        print('x и e должны быть числом, попробуйте снова!')
        continue

