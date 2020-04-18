<?php
print(
 "<form>
 <legend>Результат выполнения задания:</legend>
 <table>
  <tr> 
  <td><label>Имя:</label></td><td><input type='text' name='name'/></td>
  </tr>
   <tr> 
     <td><label>Город:</label></td><td><input type='text' name='city' value='".$_COOKIE["city"]."' /></td>
   </tr>
   <tr>
   <td><label>Возраст:</label></td><td><input type='text' name='years' value='".$_COOKIE["years"]."' /></td>
   </tr>
 </table>
 <input type='submit' name='send' value='Отправить'>
</form>"
);
?>