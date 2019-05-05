Attribute VB_Name = "Module1"
Sub Stock()
    Dim Total_Volume As Double
    Dim Ticker As String
    Dim Stock_Table As Integer
    Dim i As Long
    Dim Sht As Worksheet

Sht_Count = ActiveWorkbook.Worksheets.Count
    For Each Sht In Worksheets
        Sht.Activate
        Stock_Table = 2
        Ticker = Cells(2, 1).Value
        Total_Volume = 0
        LastRows = Range("A1", Range("A1").End(xlDown)).Rows.Count
        For i = 2 To LastRows
            If Cells(i, 1).Value <> Cells(i + 1, 1).Value Then
                Ticker = Cells(i, 1).Value
                Total_Volume = Total_Volume + Cells(i, 7).Value
                Range("J" & Stock_Table).Value = Total_Volume
                Range("I" & Stock_Table).Value = Ticker
                Stock_Table = Stock_Table + 1
                Total_Volume = 0
            Else
                Total_Volume = Total_Volume + Cells(i, 7).Value
            
            End If
        Next i
    Next Sht
End Sub


