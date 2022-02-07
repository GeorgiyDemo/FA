'Заданы целые числа. a, b, c. Вычислить значение выражения
Option Explicit
Sub MAIN()

    Dim a, b, x As Integer
    Dim s, k As Double
    
    a = Val(InputBox("Введите a"))
    b = Val(InputBox("Введите b"))
    x = Val(InputBox("Введите x"))
    
    s = 1 + Tan(x / (1 + Sqr(x)))
    k = 3 * Cos(a) + b / 7
    
    MsgBox "Результат выражения №1" + vbCrLf + "s=" + CStr(s)
    MsgBox "Результат выражения №2" + vbCrLf + "k=" + CStr(k)
    
End Sub
