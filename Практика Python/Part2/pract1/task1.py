#TODO ИЗ DEV ВЗЯТЬ ЧАСТЬ И ЧАСТЬ ОТСЮДА 
#СОЕДИНИТЬ + РЕФОРМАТ
def recurrent(x, n):
    
    m = -1
    c = 1
    p = 1
    
    final_sum = 0

    for i in range(0, n):
        # Рекурентные формулы
        if i == 0:
            c = 1
        else:
            c = c + 1    # знаменатель
        m = -m            # знак
        p = x * p   # числитель
        print("{}/{}".format(p,c))
        locale_result = m * p / c
        final_sum += locale_result
        
    return final_sum

# Task_1
x = float(input('x = '))
for i in range(5, 11):
    res = recurrent(x, i)
    print(f'Результат при x = {x} и n = {i}): {res}')
    print()
    break
