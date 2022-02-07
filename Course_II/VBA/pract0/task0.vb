'Написать программу на VBA, которая позволяет в одномерном массиве вычеслить сумму
'положительных элементов и произведение отрицательных

Private Sub CommandButton1_Click()
    Dim a(100), i, sum, proz As Integer

    'Ввод исходных данных
    Label1.Caption = "Исходный массив: " + Chr(13)
    n = InputBox("Введите размерность массива: ")

    'Вывод искодного массива на Label1
    sum = 0
    proz = 1

    For i = 1 To n
        a(i) = CInt(Rnd() * 20 - 10)
        Label1.Caption = Label1.Caption + CStr(a(i)) + " "
        If (a(i) > 0) Then
            sum = sum + a(i)
        End If
        If (a(i) < 0) Then
            proz = proz * a(i)
        End If
    Next i

    Label1.Caption = Label1.Caption + Chr(13) + "Сумма полож. элементов:" + CStr(sum) + Chr(13) + "Произведение отриц. элементов: " + CStr(proz)

End Sub
