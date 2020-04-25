<?php
require_once('../../pages/header.php');
require_once('../connector.php');

// Запись нового товара
if (isset($_POST['new_goods'])) {

    $new_warehouse_id = $_POST['new_warehouse'];
    $new_goods = $_POST['new_goods'];
    $amount = $_POST['amount'];

    $query = "INSERT INTO task9_nomenclature (warehouse_id, name, amount) VALUES (" . $new_warehouse_id . ",'" . $new_goods . "'," . $amount . ")";
    mysqli_query($link, $query);
}


//Вывод инфы по-умолчанию
$nomenclature_result = mysqli_query($link, "SELECT task9_nomenclature.name, task9_warehouse.name AS warehouse, task9_nomenclature.amount FROM task9_nomenclature
INNER JOIN task9_warehouse ON task9_nomenclature.warehouse_id=task9_warehouse.id ORDER BY task9_nomenclature.name");


print('
<div class="container">
  <div class="row">
    <div class="col">
Имеющиеся позиции товаров:
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
</div>
<div class='col'>
    
<form method='post' action=''>
Название нового товара  :<input type='text' name='new_goods' value=''>
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
<a  href='task9.php'>Вернуться на главную страницу </a>
</div>");

print("</div>
</div>")
?>