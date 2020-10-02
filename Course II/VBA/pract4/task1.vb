'Программа должна для каждого контракта, где цена выходит за установленные пределы,
'заменять ее на соответствующую предельную цену.
'Кроме того, на рабочем листе Лист3 должен быть получен перечень номеров контрактов,
'для которых цена была исправлена.

'TODO Валидация данных

'Функция получения минимального и максимального значения по товару
Function MaxMinPriceGetter(good_name As String) As Variant()
    Dim good_maxprice, good_minprice As Double
    Dim returnArray(0 To 1) As Variant
    
    Sheets("Лист2").Select
    Set d2 = Range("A1").CurrentRegion
    x_max = d2.Rows.Count
    For x2 = 2 To x_max
        
        If (Cells(x2, 1).Value = good_name) Then
            good_minprice = Cells(x2, 2).Value
            good_maxprice = Cells(x2, 3).Value
            Exit For
        End If
        
    Next x2
    
    Sheets("Лист1").Select
    returnArray(0) = good_maxprice
    returnArray(1) = good_minprice
    MaxMinPriceGetter = returnArray
    
End Function

'Функция записи исправленных данных на 3 лист
Sub AddCorrectionToList3(good_number As String)

    Sheets("Лист3").Select
    Set d3 = Range("A1").CurrentRegion
    'Определяем ячейку для записи
    x_max = d3.Rows.Count
    
    Cells(x_max + 1, 1) = good_number
    Sheets("Лист1").Select
    
End Sub

Sub MAIN()
    
    Dim readerflag As Boolean
    Dim x, y As Integer
    Dim good_name, good_number As String
    Dim MaxMinResult As Variant
    Dim good_price, good_maxprice, good_minprice As Double
    
    'Начальные значения
    Sheets("Лист1").Select
    Set d1 = Range("A1").CurrentRegion
    
    'Границы данных
    x_max = d1.Rows.Count
    y_max = d1.Columns.Count
    
    'Цикл по каждому товару
    For x = 2 To x_max
    
        'Данные о текущем просматриваемом товаре
        good_number = Cells(x, 1).Value
        good_name = Cells(x, 2).Value
        good_price = Cells(x, 3).Value
                
        MaxMinResult = MaxMinPriceGetter((good_name))

        good_maxprice = MaxMinResult(0)
        good_minprice = MaxMinResult(1)
        
        'Если цена товара меньше минимального
        If good_price < good_minprice Then
            'Запись данных на 3 лист
            AddCorrectionToList3 (good_number)
            'Исправление значения
            Cells(x, 3) = good_minprice
        End If
        
        'Если цена больше максимального
        If good_price > good_maxprice Then
            'Запись данных на 3 лист
            AddCorrectionToList3 (good_number)
            'Исправление значения
            Cells(x, 3) = good_maxprice
        End If
        
    Next x
    
End Sub