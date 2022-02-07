'Вариант 4
'Дана матрица А (3x4).
'Программа находит максимальный элемент 1-ой строки и выводит его на экран.

Option Explicit

'Перевод матрицы в string
Public Function Matrix2Str(arr As Variant) As String
    Dim i, j, n, m As Integer
    Dim buff As String
    
    buff = ""
    
    'Определение размерности
    n = UBound(arr, 1) - LBound(arr, 1)
    m = UBound(arr, 2) - LBound(arr, 2)
    
    For i = 1 To n
        For j = 1 To m
            buff = buff + CStr(arr(i, j)) + " "
        Next j
        buff = buff + vbCrLf
        
    Next i
    Matrix2Str = buff
    
End Function

Sub MAIN()
    Dim A(3, 4) As Variant
    Dim i, j, n, m, maxElement As Integer
    
    n = UBound(A, 1) - LBound(A, 1)
    m = UBound(A, 2) - LBound(A, 2)
    
    'Заполняем матрицу рандомными значениями от 1 до 100
    For i = 1 To n ' цикл по строкам
        For j = 1 To m ' цикл по столбцам
            A(i, j) = Int((100 * Rnd) + 1)
        Next j
    Next i
    
    'Ищем максимальный элемент в 1 строке
    maxElement = A(1, 1)
    For j = 1 To m
        If (maxElement < A(1, j)) Then
            maxElement = A(1, j)
        End If
    Next j
    
    'Вывод на экран матрицы и максимального элемента по 1 строке
    MsgBox ("Исходная матрица:" + vbCrLf + Matrix2Str(A) + vbCrLf + "Максимальный элемент в 1 строке: " + CStr(maxElement))

End Sub

