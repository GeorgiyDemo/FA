'Вариант 4
'1. Найти сумму элементов массива, принадлежащих промежутку от А до В.
'2. Найти количество нечетных элементов массива.
Option Explicit

'Определение длины массива
Public Function ArrayLen(arr As Variant) As Integer
    ArrayLen = UBound(arr) - LBound(arr) + 1
End Function

'Перевод массива в string
Public Function Array2Str(arr As Variant) As String
    Dim i As Integer
    Dim buff As String
    
    buff = ""
    For i = 1 To ArrayLen(arr)
        buff = buff + CStr(arr(i)) + " "
    Next i
    Array2Str = buff
    
End Function

Sub MAIN()

    Dim arr(1 To 5) As Variant
    Dim A, B, i, elementsSumm, oddCounter As Integer
    
    A = Val(InputBox("Введите начало промежутка A для поиска чисел"))
    B = Val(InputBox("Введите начало промежутка B для поиска чисел"))
    
    'Генерация элементов массива
    For i = 1 To ArrayLen(arr)
      arr(i) = Int((35 * Rnd) + 1)
    Next i
    
    'Поиск суммы элементов массива, принадлежащих промежутку от А до В.
    elementsSumm = 0
    For i = 1 To ArrayLen(arr)
        'Если входит в промежуток, то вычисляем сумму
        If (arr(i) > A) And (arr(i) < B) Then
            elementsSumm = elementsSumm + arr(i)
        End If
    Next i
    
    
    'Находим количество нечетных элементов массива.
    oddCounter = 0
    For i = 1 To ArrayLen(arr)
        If arr(i) Mod 2 = 1 Then
            oddCounter = oddCounter + 1
        End If
    Next i
    
    MsgBox ("Исходный массив: " + vbCrLf + Array2Str(arr) + vbCrLf + "Сумма элементов от " + CStr(A) + " до " + CStr(B) + " = " + CStr(elementsSumm) + vbCrLf + "Кол-во нечетных чисел = " + CStr(oddCounter))
    
End Sub
