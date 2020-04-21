<?php
print("  <style type='text/css'>
.layout {
 width: 100%;
}
TD {
 vertical-align: top;
 padding: 5px;
}
TD.leftcol {
 width: 200px;
 background: #ccc;
}
TD.rightcol {
 background: #fc3;
}
</style>");

$catsnamesarr = array("cat1"=>"Котик №1", "cat2"=>"Котик №2", "cat3"=>"Котик №3", "cat4"=>"Котик №4", "cat5"=>"Котик №5","cat6"=>"Котик №6");
$catspricearr = array("cat1"=>12000, "cat2"=>1000, "cat3"=>3000, "cat4"=>2000, "cat5"=>1900, "cat6"=>2500);
print("
 <form>
 <legend>Ваша корзина:</legend>
 <table cellspacing='0' class='layout'>
 <tr> 
  <td class='leftcol'><b>Название товара</b></td>
  <td class='rightcol'><b>Цена<b>
  </td>
 </tr>
 
");
  $finalprice = 0;
  foreach($_COOKIE as $key=>$value)
  {
    print(" <tr> 
    <td class='leftcol'>".$catsnamesarr[$key]."</td>
    <td class='rightcol'>".$catspricearr[$key]." руб."."</td>
   </tr>");
   $finalprice +=(double) $catspricearr[$key];
  }

print(
  "<tr> 
  <td class='leftcol'><b>Итог:</b></td>
  <td class='rightcol'><b>".$finalprice." руб.<b></td>
 </tr>
 </table>
 </form>
 <form action='index.php' method='post'>
 <input type='submit' name='send' value='К списку товаров'>
</form>");

?>