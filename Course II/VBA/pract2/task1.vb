'Заданы целые числа. a, b, c. Вычислить значение выражения
Option Explicit
Sub MAIN()
    Dim x, y, z As Integer
    Dim result1, result2, first_part, second_part As Double
    
    x = Val(InputBox("Введите X"))
    y = Val(InputBox("Введите Y"))
    z = Val(InputBox("Введите Z"))
    
    first_part = z * Sqr(x) - y ^ 2 * x ^ (1 / 3)
    second_part = (x + 0.5) ^ (1 / 5)
    result1 = first_part / second_part
    
    result2 =cos(
    
    
    MsgBox "Результат выражения №1: " & CStr(result1)
    MsgBox "Результат выражения №2: " & CStr(result2)
    
End Sub
