<?php
require_once('../pages/header.php');
//Работа с файлами в PHP, счетчик на сайте
print("Работа с файлами в PHP. Счетчик количества посещений сайта<br>");
$f_str = "task4_counter.txt";

$f = fopen($f_str, 'a+t');
$counter = fgets($f);
file_put_contents($f_str, "");
if ($counter == FALSE)
    $counter = 0;

$counter++;
print($counter);
fwrite($f, $counter);
fclose($f);
print('</body></html>')
?>
