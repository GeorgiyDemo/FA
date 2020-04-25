<?php
require_once('../pages/header.php');
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


    print("Внесена оценка студента с фамилией - " . $_POST['name_of_user'] . '<FORM name="my_form" METHOD="POST">
    <input
        type="submit" value="Внести ещё"
        name="exit_system"
        title="">
        </form></body></html>');
} else {
    print('
    <FORM     name="my_form" METHOD="POST">
   Фамилия:   <INPUT TYPE = "text" NAME = "name_of_user"
       value=""    title="Поле для ввода фамилии">
   <br>	
   <SELECT size="1" Name="spisok1">
     <option value= "Оценка 5 ">Отлично</option>
     <option value= "Оценка 4 ">Хорошо</option>
     <option value= "Оценка 3 ">Удовлетворительно</option>
     <option value= "Оценка 2 ">Неудовлетворительно</option>
   </SELECT>
   <br>
      <input     type="submit" value="OK"   name="enter_system"
      title="Нажмите, если Вы ввели имя, чтобы увидеть результат">
      </form>
    </body></html>');
}
?>
