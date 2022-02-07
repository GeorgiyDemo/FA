<?php
require_once('../pages/header.php');
//Пример использования констант
print('Пример использования констант в ЯП PHP<br>');
define("koeff", 60);
$h = 3.5;
echo " Число минут в указанном значении в часах =" . $h * koeff . "<br>";
echo PHP_VERSION;
print('</body></html>')
?>
