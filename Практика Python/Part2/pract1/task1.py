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
#TODO ТУТ ВСЕ НЕПРАВИЛЬНО

class MainClass:
    def __init__(self):
        self.x_processing_flag = False
        self.result_sum = 0
        # Ввод данных
        while not self.x_processing_flag:
            self.x_values_input()

        for i in range(5, 11):
            self.current_calculating(self.x, i)

        print("Общая сумма: " + str(self.result_sum))

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

    def current_calculating(self, n, x):
        """
        Метод для вычисления N элемента по рекурентным формулам
        - n - текущий n
        - x - входящий x
        - n_stop - фильнальый n, где необходима остановка
        
        Общая формала по 6 варианту:
        L*(C/P)
        """

        #Обозначение знака L
        L = -1

        if x != 0:
            C = pow(x,n+1)
        else:
            C = 1 


        for i in range(0, n):
            #Чтоб в числителе не стало 0
            if x != 0:
                C = pow(x,n+1)
            else:
                C = 1 
            
            #Меняем знак на противоположный
            L = -L

        result = pow(-1, n + 1) * (pow(x, n) / n)
        self.result_sum += result
        print("n = " + str(n) + ", результат: " + str(result))
        # Остановка
        if n == n_stop:
            return
        self.calculating(n + 1, x, n_stop)


if __name__ == "__main__":
    MainClass()
