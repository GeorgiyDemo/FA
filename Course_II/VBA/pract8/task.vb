Sub Main()
    UserForm1.Show
End Sub

'Перевод из цифр в пропись
Function Translater(number)

    Dim rub, units, dozens, hundrunits, nadc, sizes, i, m
    
    If (number >= 1E+15) Or (number < 0) Then
        Exit Function
    End If
    
    hundrunits = Array("", "сто ", "двести ", "триста ", "четыреста ", "пятьсот ", "шестьсот ", "семьсот ", "восемьсот ", "девятьсот ")
    dozens = Array("", "", "двадцать ", "тридцать ", "сорок ", "пятьдесят ", "шестьдесят ", "семьдесят ", "восемьдесят ", "девяносто ")
    nadc = Array("десять ", "одиннадцать ", "двенадцать ", "тринадцать ", "четырнадцать ", "пятнадцать ", "шестнадцать ", "семнадцать ", "восемнадцать ", "девятнадцать ")
    units = Array("", "один ", "два ", "три ", "четыре ", "пять ", "шесть ", "семь ", "восемь ", "девять ", "", "одна ", "две ")
    sizes = Array("триллион ", "триллиона ", "триллионов ", "миллиард ", "миллиарда ", "миллиардов ", "миллион ", "миллиона ", "миллионов ", "тысяча ", "тысячи ", "тысяч ", "рубль ", "рубля ", "рублей ")

    rub = Left(Format(number, "000000000000000"), 15)

    If (CDbl(rub) = 0) Then
        m = "ноль "
    End If
    
    For i = 1 To Len(rub) Step 3
        If Mid(rub, i, 3) <> "000" Or i = Len(rub) - 2 Then
                m = m & hundrunits(CInt(Mid(rub, i, 1))) & IIf(Mid(rub, i + 1, 1) = "1", nadc(CInt(Mid(rub, i + 2, 1))), _
                dozens(CInt(Mid(rub, i + 1, 1))) & units(CInt(Mid(rub, i + 2, 1)) + IIf(i = Len(rub) - 5 And CInt(Mid(rub, i + 2, 1)) < 3, 10, 0))) & _
                IIf(Mid(rub, i + 1, 1) = "1" Or (Mid(rub, i + 2, 1) + 9) Mod 10 >= 4, sizes(i + 1), IIf(Mid(rub, i + 2, 1) = "1", sizes(i - 1), sizes(i)))
        End If
    Next i
    Translater = UCase(Left(m, 1)) & Mid(m, 2)
    
End Function

'Нажатие на заполнение
Private Sub CommandButton1_Click()

    ActiveDocument.Bookmarks("ЦЕНА").Range.Text = TextBox1.Text
    ActiveDocument.Bookmarks("ЦЕНА_ПРОПИСЬ").Range.Text = Translater(TextBox1.Text)
    ActiveDocument.Bookmarks("ИНДЕКС").Range.Text = TextBox3.Text
    ActiveDocument.Bookmarks("АДРЕС").Range.Text = TextBox4.Text + " " + TextBox5.Text + " " + TextBox6.Text + " " + TextBox7.Text
    ActiveDocument.Bookmarks("КОМУ").Range.Text = TextBox13.Text
    ActiveDocument.Bookmarks("ОТ_КОГО").Range.Text = TextBox14.Text

    If (Frame4.Enabled = False) Then
        ActiveDocument.Bookmarks("ОБРАТНЫЙ_ИНДЕКС").Range.Text = " - "
        ActiveDocument.Bookmarks("ОБРАТНЫЙ_АДРЕС").Range.Text = " - "
    End If

    If (Frame4.Enabled = True) Then
        ActiveDocument.Bookmarks("ОБРАТНЫЙ_ИНДЕКС").Range.Text = TextBox8.Text
        ActiveDocument.Bookmarks("ОБРАТНЫЙ_АДРЕС").Range.Text = TextBox9.Text + " " + TextBox10.Text + " " + TextBox11.Text + " " + TextBox12.Text
    End If

    UserForm1.Hide

End Sub

'Выход
Private Sub CommandButton2_Click()
    Unload UserForm1
End Sub

Private Sub OptionButton1_Click()
    Frame4.Enabled = True
End Sub

Private Sub OptionButton2_Click()
    Frame4.Enabled = False
End Sub

Private Sub TextBox1_Change()
TextBox2.Text = Translater(TextBox1.Text)
End Sub


