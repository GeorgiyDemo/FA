<?php
require_once('../connector.php');


// Запись нового товара
if (isset($_POST['new_goods'])) {

  $new_warehouse_id = $_POST['new_warehouse'];
  $new_goods = $_POST['new_goods'];
  $amount = $_POST['amount'];

  $query = "INSERT INTO task9_nomenclature (warehouse_id, name, amount) VALUES (".$new_warehouse_id.",'".$new_goods."',".$amount.")";
  mysqli_query($link, $query);
}


//Вывод инфы по-умолчанию
$nomenclature_result = mysqli_query($link, "SELECT task9_nomenclature.name, task9_warehouse.name AS warehouse, task9_nomenclature.amount FROM task9_nomenclature
INNER JOIN task9_warehouse ON task9_nomenclature.warehouse_id=task9_warehouse.id ORDER BY task9_nomenclature.name");

print('
<font style="font-size:16pt">
Имеющиеся позиции товаров:</font>
<table border=1>
');

while ($goods = $nomenclature_result->fetch_assoc()) {
  //Вывод названия товара
  print('<tr><td>' . $goods["name"] . '</td><td>');
  //Получаем название склада
  print($goods["warehouse"] . "</td><td>");
  //Кол-во товара
  print($goods["amount"] . "</td></tr>");
}

//Генерация формы новых товаров
print("
</table>
<div style='position:absolute;top:5;left:1000'>
<font size='+2'> Форма ввода новых товаров</font>
<form method='post' action=''>
<font style='font-size:16pt'>
Название нового товара  :<input type='text'
        name='new_goods' value=''>
<br>
");

$result3 = mysqli_query($link, "SELECT id, name FROM task9_warehouse");
print('Склад  :<select  name="new_warehouse">');

while ($line = $result3->fetch_assoc())
  print("<option value='" . $line["id"] . "'>" . $line["name"]);

print("
</select><br>
Количество  :<input type='text' name='amount' value=''>
<br><input name='enterNew'
 type='submit' value='Ввести товар'>
</form>
<br>
<a  href='index.php'>Вернуться на главную страницу </a>
</div>");
