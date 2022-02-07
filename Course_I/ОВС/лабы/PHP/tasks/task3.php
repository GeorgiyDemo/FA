<?php
require_once('../pages/header.php');
print('Пример использования массивов в ЯП PHP<br>');
//Пример использования массивов
$mas = array("Room1" => "Офис", "Room2" => "Склад", 55 => 100);
echo $mas["Room1"] . "<br>";
echo $mas ["Room2"] . "<br>";
echo $mas [55] . "<br>";
print('</body></html>')
?>
