<?php
require_once('../pages/header.php');
print('Пример формы с раскрывающимся списком и записью в файл');
//Пример формы с раскрывающимся списком и записью в файл
if ($_POST['enter_system'] == "OK") {
    $f = fopen("task6_data.txt", "a+t") or die("Файл не открывается");
    flock($f, 2);
    fputs($f, $_POST['name_of_user']);
    fputs($f, " ");
    fputs($f, $_POST['spisok1']);
    fputs($f, "\n");
    flock($f, 3);
    fclose($f);


    print("<br>Внесена оценка студента с фамилией - " . $_POST['name_of_user'] . '<form name="my_form" method="post">
    <input
        type="submit" class="btn btn-outline-primary" value="Внести ещё"
        name="exit_system"
        title="">
        </form></body></html>');
} else {
    print('
    <form name="my_form" method="post">
    <div class=form-group row">
      Фамилия:
      <input type = "text" class="form-control" name = "name_of_user"
      value="" title="Поле для ввода фамилии">
   </div>	

   <div class=form-group row">

    <select class="form-control" name="spisok1">
      <option value= "Оценка 5 ">Отлично</option>
      <option value= "Оценка 4 ">Хорошо</option>
      <option value= "Оценка 3 ">Удовлетворительно</option>
      <option value= "Оценка 2 ">Неудовлетворительно</option>
    </select>
    </div>	

    <div class=form-group row">
      <input type="submit" class="btn btn-outline-primary" value="OK" name="enter_system"
      title="Нажмите, если Вы ввели имя, чтобы увидеть результат">
      </div>

      </form>
    </body></html>');
}
?>
