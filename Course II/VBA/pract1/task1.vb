'Вариант 1 Напишите команды для организации ввода в программу двух чисел.
'Окна ввода должны иметь разные параметры (строку заголовка, сообщение в окне, значения по умолчанию).
Sub MAIN()
    Dim number1, number2 As Double
    Dim sum As Double
    
    number1 = InputBox("Введите число №1", "Ввод числа №1", 2)
    number2 = InputBox("Введите число №2", "Ввод числа №2", 4)
    
    sum = number1 + number2
    
    MsgBox "Сумма чисел " + CStr(number1) + " и " + CStr(number2) + " = " + CStr(sum), , "Вывод данных"
End Sub
