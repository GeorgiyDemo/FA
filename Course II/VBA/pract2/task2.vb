'Вычислить квадратный корень из данного числа, если оно неотрицательное, и уменьшить его на 2 в противном случае.
Option Explicit
Sub MAIN()
    Dim number, result As Double
    Dim tree As Byte
    
    number = Val(InputBox("Введите число"))
    If number < 0 Then
        result = number - 2
        tree = 1
    Else
        result = Sqr(number)
        tree = 2
    End If

    MsgBox "Результат: " + CStr(result) + vbCrLf + "Выполнилось условие " + CStr(tree)
    
End Sub
