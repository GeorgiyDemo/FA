import math
             

def get_result_n (x, n):
    result = 0
    step = 1
    factor = 1
    for i in range(1, n*2+1, 2):
        result += step/factor
        step *= x**2
        factor *= i*(i+1)
    return result
    
def get_result_epsilon (x, e):
    result = 0
    step = 1
    factor = 1
    i = 1
    while(abs(step/factor)>=e):
        result += step/factor
        step *= x**2
        factor *= i*(i+1)
        i+=2
    return result
    
    
if __name__ == '__main__':
    x = float(input())
    n = int(input())
    e = float(input())
    print(f'Сумма {n} членов ряда: {get_result_n(x, n)}')
    print(f'Сумма c точностью epsilon = {e}: {get_result_epsilon(x, e)}')
    print(f'ch({x}) = {math.cosh(x)}  (Ответ получен с помощью функции math.cosh(x))')