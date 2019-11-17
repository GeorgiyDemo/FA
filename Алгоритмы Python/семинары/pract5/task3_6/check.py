import texttable
table = texttable.Texttable()
#table.set_cols_align(["l", "r", "c"])
#table.set_cols_valign(["t", "m", "b"])
buf_list = []

table_list = [["№", "Поезд", "№ вагона","№ места","Цена","Тип места","Статус","Время отправления","Время прибытия"]]
for i in range(9): 
    buf_list = []
    for j in range(9):
        buf_list.append(j)
    table_list.append(buf_list)

#table = [["№", "Поезд", "№ вагона","№ места","Цена","Тип места","Статус","Время отправления","Время прибытия"]]
table.add_rows(table_list)
print(table.draw() + "\n")