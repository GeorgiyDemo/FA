<?php
$f = fopen("z.txt", "a+t") or die("Файл не открывается");
flock($f, 2);
$s = fgets($f);
$s = $s + 1;
ftruncate($f, 0);
fputs($f, $s);
flock($f, 3);
fclose($f);
echo $s;
?>
