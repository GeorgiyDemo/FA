<?php
  print("<html><head><title> Авторизация  </title>");
  require_once('../connector.php'); 
  $sql="SELECT * FROM task9_users ORDER BY name";
  $result=mysqli_query($link, $sql);

   print('<form action="start.php" method="post">
  <select  name="id">
  ');

  while($row = $result->fetch_assoc())
   print("<option value='".$row["id"]."'>".$row['name']);
   

  
   //echo "id: " . $row["id"]. " - Name: " <br>";

//
 //    while ($line=mysql_fetch_row($result))
 //    { echo "<option value='".$row["id"]."'>$row["name"]";
 //    }
  
     print("</select><br><br>
     Пароль:<input type='password' name='password'>
    <input name='enterStart' STYLE='font-size: 14pt; font-family: Tahoma, sans-serif'
       type='submit' value='Перейти к работе с базой'>
    </form>
    ");
?>
