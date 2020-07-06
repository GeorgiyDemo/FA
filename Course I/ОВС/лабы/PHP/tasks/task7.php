<?php
require_once('../pages/header.php');
//Пример формы обратной связи на PHP
print('Пример формы обратной связи на PHP');
if (isset($_POST['okb'])) {
    if ($_POST['person'] == '' or $_POST['email'] == '' or $_POST['q'] == '') {
        print("<font color='red'>Вы ввели не все данные</font><br><a href=obrabotka.php>назад</a>");
        exit;
    }

    $komu = "cashaev@rambler.ru";
    $tema = "Вопрос от" . $_POST['person'] . "  " . $_POST['email'];
    $text_pisma = $_POST['q'];

    print('<br>Отправлено. Получатель - ' . $_POST['person'] . "<br>");
    print($komu . ":<br><br");
    print($tema . "<br>");
    print($text_pisma . "<br>");

} else
    print('
    <form  method="post">
    <div class=form-group row">
        Имя <input type="text" class="form-control" name="person">
    </div>

    <div class=form-group row">
    E-mail<input type="text" class="form-control" name="email">
    </div>


    <div class=form-group row">
    <label for="exampleFormControlTextarea1">Вопрос:</label>
    <textarea class="form-control"  name="q" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>
    


    <div class=form-group row">
        <input type="submit" class="btn btn-outline-primary" name="okb" value="Отправить">
    </div>
    </form>
    ');

print('</body></html>');
?>
