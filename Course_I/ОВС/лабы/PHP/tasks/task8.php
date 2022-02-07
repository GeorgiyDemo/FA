<?php
require_once('../pages/header.php');
print('Пример гостевой книги на PHP');
//Пример гостевой книги
$filename = "task8_data.txt";
if (isset($_POST['okbutton'])) {
    if ($_POST['name_of_quest'] == '')
        exit("Введите имя <a href=’#>Назад!</a>");
    if ($_POST['message_of_quest'] == '')
        exit("Введите сообщение <a href='questbook.php'>Назад!</a>");
    $f = fopen($filename, "at") or die("Не могу открыть файл");
    flock($f, 2);
    fputs($f, $_POST['name_of_quest'] . "\n");
    fputs($f, $_POST['message_of_quest'] . "\n");
    flock($f, 3);
    fclose($f);
}

print('

<form method="post">

<div class=form-group row">
    Имя <input type="text" class="form-control" name="name_of_quest">
</div>

<div class=form-group row">
    <label for="exampleFormControlTextarea1">Сообщение:</label>
    <textarea class="form-control"  name="message_of_quest" id="exampleFormControlTextarea1" rows="3"></textarea>
</div>

<div class=form-group row">
    <input type="submit" class="btn btn-outline-primary" name="okbutton" value="Отправить">
</div>

</form>

');
$f = fopen($filename, "rt") or die("Не могу открыть файл");
while (!feof($f)) {
    $data = fgets($f); // Получаем фамилию
    echo "<small>Имя:</small>" . $data . "<br>";
    $data = fgets($f); // Получаем сообщение
    echo "<small>Сообщение:</small>" . $data . "<br>";
    echo "<hr>";
}
fclose($f);

print('</body></html>');
?> 
