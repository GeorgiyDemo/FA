<?php
$catsmoney = array(1=>12000, 2=>1000, 3=>3000, 4=>2000, 5=>1900, 6=>2500);

print(
 "<form action='index.php' method='post'>
 <legend>Выберите котика:</legend>
 <table>");

  for ($i=1;$i<7;$i++)
  {
    print("<tr> 
    <td><label>Котик №".$i.":</label></td><td><img src='../../../img/cat".$i.".jpg'><br>Цена: ".$catsmoney[$i]." руб. <br><input type='submit' name='cat".$i."' value='В корзину'></td>
  </tr>");
  }

  print(
 "</table>
</form>
<form action='output.php'>
</form>"
);



foreach($_POST as $key=>$value)
  if (substr($key, 0, 3)=='cat')
    SetCookie($key, $value, time() + 3600);

print(
 "<form action='bucket.php' method='post'>".
 "<input type='hidden' name='catsprice' value=".htmlentities(serialize($catsmoney)).">".
 "<input type='submit' name='send' value='Переход к корзине'>
</form>"
);

?>