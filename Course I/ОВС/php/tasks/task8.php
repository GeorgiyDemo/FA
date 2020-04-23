<?php
//Пример гостевой книги
$filename = "task8_data.txt";
if (isset($_POST['okbutton']))
{
 if ($_POST['name_of_quest']=='')
      exit("Введите имя <a href=’#>Назад!</a>");
 if ($_POST['message_of_quest']=='')
   exit("Введите сообщение <a href='questbook.php'>Назад!</a>");
 $f=fopen($filename,"at") or die("Не могу открыть файл");
 flock($f,2);
 fputs($f,$_POST['name_of_quest']."\n");
 fputs($f,$_POST['message_of_quest']."\n");
 flock($f,3);
 fclose($f);
}

print('
<html><head>
<title> Гостевая книга </title></head>
<body>
<form method="post">
Имя <br>
<input type="text" name="name_of_quest">
<br>Сообщение:<br>
<br>
<textarea name="message_of_quest" cols=10 rows=5>
</textarea>
<br><input type="submit" name="okbutton" value="OK">
</form>
');
$f=fopen($filename,"rt") or die("Не могу открыть файл");
while (!feof($f))
{
    $data=fgets($f); // Получаем фамилию
    echo "<small>Имя:</small>".$data."<br>";
    $data=fgets($f); // Получаем сообщение
    echo "<small>Сообщение:</small>".$data."<br>";
    echo "<hr>";
}
fclose($f);
?> 
