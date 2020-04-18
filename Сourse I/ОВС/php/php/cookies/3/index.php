<?php
print(
 "<form action='index.php' method='post'>
 <legend>Ввод данных пользователя:</legend>
 <table>
   <tr> 
     <td><label>Город:</label></td><td><input type='text' name='city' /></td>
   </tr>
   <tr>
   <td><label>Возраст:</label></td><td><input type='text' name='years' /></td>
   </tr>
 </table>
 <input type='submit' name='send' value='Отправить'>
</form>".
"<form action='output.php'>
<input type='submit' value='Выполнить задание'>
</form>"
);
if (($_POST["city"] != Null) && ($_POST["years"] != Null))
    SetCookie("city",$_POST["city"],time()+3600);
    SetCookie("years",$_POST["years"],time()+3600);
?>