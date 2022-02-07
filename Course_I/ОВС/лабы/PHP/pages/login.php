<?php
require_once('../pages/header.php');

print("<br>");

if ((isset($_COOKIE['registrated'])) || ($_POST["setlogin"] == "booleantrue")) {
    print("

		<div class='container'>
		<form class='form-signin' action='../loginlogic/authorisation.php' method='POST'>
			<h2 class='form-signin-heading'>Авторизация</h2>
			<label for='inputEmail' class='sr-only'>Адрес e-mail</label>
			<input type='email' id='inputEmail' class='form-control' name='login' placeholder='Адрес e-mail' required autofocus>
			<label for='inputPassword' class='sr-only'>Пароль</label>
			<input type='password' id='inputPassword' class='form-control' name='pass' placeholder='Пароль' required>
			<div class='checkbox'>
			</div>
			<button class='btn btn-lg btn-primary btn-block' type='submit'>Войти</button>
		</form>
		<form class='formreg' action='login.php' method='POST'>
		<button class='btn' name='setregistration' value='booleantrue' type='submit'>Необходимо зарегистрироваться?</button>
		</form>
		</div>
");
} else {
    print("
	<div class='container'>
	<form class='form-signin' action='../loginlogic/registration.php' method='POST'>
		<h2 class='form-signin-heading'>Регистрация</h2>
		<label for='inputName' class='sr-only'>Имя пользователя</label>
		<input type='text' id='inputName' class='form-control' name='name' placeholder='Имя пользователя' required autofocus>
		<label for='inputEmail' class='sr-only'>Адрес e-mail</label>
		<input type='email' id='inputEmail' class='form-control' name='login' placeholder='Адрес e-mail' required autofocus>
		<label for='inputPassword' class='sr-only'>Пароль</label>
		<input type='password' id='inputPassword' class='form-control' name='pass' placeholder='Пароль' required>
		<div class='checkbox'>
		</div>
		<button class='btn btn-lg btn-primary btn-block' type='submit'>Зарегистрироваться</button>
		</form>
		<form class='formlog' action='login.php' method='POST'>
		<button class='btn' name='setlogin' value='booleantrue' type='submit'>Уже зарегистрированы?</button>
		</form>
	</div>
	");
}

print('</body></html>')

?>