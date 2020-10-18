'Контрольная 1. Задание B. Деменчук Георгий ПИ19-4
Option Explicit
Sub MAIN()
    
    Dim x, y, z As Double
    Dim way As Byte
    'Ввод данных
    x = Val(InputBox("Введите значение x", "Ввод"))
    
    'Вычисляем z
    'Условие 1
    If x > 0 Then
        z = 1
        way = 1
    End If
    'Условие 2
    If x <= 0 Then
        z = x ^ 2
        way = 2
    End If
    
    'Вычисляем y
    y = Exp(z) + 3.5 - Cos(x * z) ^ 3
    'Вывод данных
    MsgBox ("Результат: y = " + CStr(y) + vbCrLf + "Выполнилось условие №" + CStr(way))

End Sub
