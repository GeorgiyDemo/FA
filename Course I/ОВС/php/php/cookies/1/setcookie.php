<?php

	foreach($_POST as $key=>$value)
		SetCookie($key, $value, time() + 3600);
	print("
	COOKIE успешно установлены
	<br>
	<form action='./getcookie.php'>
	<input type='submit' value='Чтение Cookie' class='DEMKAsendbutton'>
	</form>
	");
?>