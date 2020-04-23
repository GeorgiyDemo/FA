<!DOCtype html>

<html>
<head>
    <meta charset=“utf-8”>
    <title>Работы по ОВС</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/css/bootstrap.css" rel="stylesheet">

</head>
<body>

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

<ul class="nav nav-pills">

    <li class="nav-item">
        <?php
		if ((isset($_COOKIE['registrated'])) || ($_POST["setlogin"] == "booleantrue"))
            print("<a class='nav-link active' href='#'>Вход</a>");
        else
            print("<a class='nav-link active' href='#'>Регистрация</a>");
        ?>
    </li>

    <li class="nav-item">
        <a class="nav-link" href="/index.php">Основное</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#">Работа с БД</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#">Работа с формами</a>
    </li>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true"
           aria-expanded="false">Базовые задания</a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="#">№1</a>
            <a class="dropdown-item" href="#">№2</a>
            <a class="dropdown-item" href="#">№3</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">Separated link</a>
        </div>
    </li>
</ul>
<br>

<?php
if ((isset($_COOKIE['registrated'])) || ($_POST["setlogin"] == "booleantrue")) {
    print("

		<div class='container'>
		<form class='form-signin' action='./loginlogic/authorisation.php' method='POST'>
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
}
else {
    print("
	<div class='container'>
	<form class='form-signin' action='./loginlogic/registration.php' method='POST'>
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
?>

</body>

</html>