<?php
	if(isset($_REQUEST['not_show']))
		setcookie('not_show', 'false', time()+3600*24*30);

	if (isset($_COOKIE['not_show']) || isset($_REQUEST['not_show']))
		print("Убрали котика на 5 мин");
	else 
		print("<a href='?not_show'><img src='../../../img/cat5.jpg'></a>");
?>