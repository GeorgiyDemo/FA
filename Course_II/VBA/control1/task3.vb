'Контрольная 1. Задание C. Деменчук Георгий ПИ19-4
'Функция вычисления y
Function Calculate(t As Double, d As Double, b As Double) As Double

    Dim y As Double
    If t > -0.5 Then
        y = 3 * Sin(t) + Atn(t)
    End If
    If t = -0.5 Then
        y = (2 * t - Exp(t)) / d
    End If
    If t < -0.5 Then
        y = b * Sqr(Abs(Cos(t) + a))
    End If
    Calculate = y
    
End Function

Sub MAIN()
    
    Dim x, u, z As Double
    Dim xCoord As Integer
    
    'Начальные значения для Excel
    Sheets("Лист1").Select
    Set d = Range("A1").CurrentRegion
    xCoord = d.Rows.Count + 1
    
    'Основной цикл итерации
    For t = -3.2 To 4.5 Step 0.9
    
        'Вычисляем значения
        d = 13 * Exp(t)
        a = 0.5 * t ^ 3 - Sin(t)
        b = 1.5 * t - Abs(t) ^ 1 / 3
        
        'Получаем значение z
        y = Calculate((t), (d), (b))
        
        'Выводим в Excel
         Cells(xCoord, 1) = t
         Cells(xCoord, 2) = b
         Cells(xCoord, 3) = a
         Cells(xCoord, 4) = d
         Cells(xCoord, 5) = y
         
         'Меняем координаты в Excel
         xCoord = xCoord + 1
    Next t
End Sub

