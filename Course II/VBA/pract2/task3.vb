'Подсчитать количество положительных чисел среди чисел a, b, c
Option Explicit
Sub MAIN()

    Dim a, b, c As Double
    Dim counter As Byte
    
    a = Val(InputBox("Введите a"))
    b = Val(InputBox("Введите b"))
    c = Val(InputBox("Введите c"))
    
    If a > 0 Then
        counter = counter + 1
    End If
    
    If b > 0 Then
        counter = counter + 1
    End If
    
    If c > 0 Then
        counter = counter + 1
    End If
    
    MsgBox "Кол-во положительных чисел: " + CStr(counter)
    
End Sub

