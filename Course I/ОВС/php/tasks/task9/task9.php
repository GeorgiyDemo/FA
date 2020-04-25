<?php

require_once('../../pages/header.php');
require_once('../connector.php');
print('Пример работы с базами данных на PHP. Менеджмент товаров на складе<br>');
$sql = "SELECT * FROM task9_users ORDER BY name";
$result = mysqli_query($link, $sql);

print('Выберите логин:<br><form action="start.php" method="post">
  <select name="id" class="form-control" id="exampleFormControlSelect1">
  ');

while ($row = $result->fetch_assoc())
    print("<option value='" . $row["id"] . "'>" . $row['name']);


print("</select>Введите пароль:<br><input type='password' name='password'><br><br>
    <input name='enterStart'
       type='submit' class='btn btn-outline-primary' value='Перейти к работе с базой'>
    </form>
    ");

print("</body></html>")
?>
