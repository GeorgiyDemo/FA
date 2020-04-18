<?php 

	if (isset($_COOKIE['Time'])) 
	{ 
	 $timee= $_COOKIE['Time']; 
	 $resultstr9= $resultstr9."Прошло секунд ".(time()-$timee); 
	}

	else
	{ 
	 setcookie('Time',time()); 
	 $resultstr9="Прошло секунд ds".time(); 
	}

	print($resultstr9);
	
?>