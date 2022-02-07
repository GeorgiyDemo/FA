Option Explicit
Sub MAIN()

    Dim x, y, p As Double
    p = Val(InputBox("Введите p"))
    
    For x = 0 To 2 Step 0.4
        y = -Sqr(p ^ 2 - (x - p) ^ 2)
        MsgBox ("x = " + CStr(x) + ", y = " + CStr(y))
    Next x
    
End Sub
