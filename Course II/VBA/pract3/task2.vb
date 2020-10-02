Option Explicit
Sub MAIN()
    Dim max_number, summ, i As Integer
    max_number = Val(InputBox("Введите ограничение"))
    
    summ = 0
    i = 1
    While i <= max_number
        summ = summ + i
        i = i + 1
    Wend
    MsgBox ("Сумма натуральных чисел в промежутке от 1 до " + CStr(max_number) + " = " + CStr(summ))
    
End Sub
