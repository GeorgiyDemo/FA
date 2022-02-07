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
<br>
<div class="container">
  <div class="row">
    <div class="col">
Имеющиеся позиции товаров:
<table class="table">
  <thead>
    <tr>
      <th scope="col">Название</th>
      <th scope="col">Склад</th>
      <th scope="col">Количество</th>
    </tr>
  </thead>
  <tbody>
  
');

while ($goods = $nomenclature_result->fetch_assoc()) {
    //Вывод названия товара
    print('<tr><td>' . $goods["name"] . '</td>');
    //Получаем название склада
    print('<td>' . $goods["warehouse"] . '</td>');
    //Кол-во товара
    print('<td>' . $goods["amount"] . ' шт. </td></tr>');
}

//Генерация формы новых товаров
print("
  </tbody>
</table>
</div>
<div class='col'>
    
<form method='post' >
<div class='form-group row'>
    Название нового товара  :<input type='text' name='new_goods' value=''>

</div>
");

$result3 = mysqli_query($link, "SELECT id, name FROM task9_warehouse");
print('
  <div class="form-group row">  Склад  :<select  class="form-control" name="new_warehouse">');

while ($line = $result3->fetch_assoc())
    print("<option value='" . $line["id"] . "'>" . $line["name"]);

print("
    </select>
    </div>
    
    <div class='form-group row'>
    Количество  :<input type='text'   class='form-control' name='amount' value=''>
    </div>
    
    <div class='form-group row'>
    <input name='enterNew'
     type='submit' class='btn btn-outline-primary' value='Внести новый товар в БД'>
    </div>
    
    <div class='form-group row'>
      <a class='btn btn-outline-primary' href='task9.php'>Вернуться на форму логина</a>
    </div>
    </form>
</div>");

print("</div>
</div>")
?>


