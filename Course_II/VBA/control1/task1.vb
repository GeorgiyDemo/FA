'Контрольная 1. Задание A. Деменчук Георгий ПИ19-4
Sub MAIN()
    
    Dim a, b, c, p, s As Double
    
    'Устанавливаем начальные значения
    a = 0.13
    b = 0.8
    c = 5.2
    
    'Вычисялем значения
    p = (a + b + c) / 2
    s = Sqr(Abs(p ^ 2 - c + Sin(Log(p)) ^ 3))
    
    'Вывод данных
    MsgBox ("p = " + CStr(p) + vbCrLf + "s = " + CStr(s))

End Sub

