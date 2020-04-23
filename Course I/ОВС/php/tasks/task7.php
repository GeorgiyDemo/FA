<?php

//Пример формы обратной связи на PHP

if (isset($_POST['okb']))
{ if ($_POST['person']=='' or $_POST['email']=='' or $_POST['q']=='')
   {  
      print("<font color='red'>Вы ввели не все данные</font><br><a href=obrabotka.php>назад</a>");
     exit;
    }
    
   $komu="cashaev@rambler.ru";
   $tema="Вопрос от".$_POST['person']."  ".$_POST['email'];
   $text_pisma=$_POST['q'];
   
   print('Отправлено. Получатель - '.$_POST['person']."<br>");
   print($komu."<br");
   print($tema."<br>");
   print($text_pisma."<br>");

   }
else
    print('
    <form  method="post">
    Имя <br>
    <input type="text" name="person">
    <br> E-mail<input type="text" name="email">
    <br> Вопрос:<br>
    <br><textarea name="q" cols=10 rows=5>
    </textarea>
    <br>
    <input type="submit" name="okb" value="OK">
    </form>
    ');

?>
