<!DOCtype html>

<html>
<head>
    <meta charset=“utf-8”>
    <title>Приют "Котикус"</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <style> [class*="col-"] {
            background-color: #eee;
            text-align: center;
            padding-top: 10px;
            padding-bottom: 10px;
            margin-bottom: 10px;
            font-size: 2rem;
        }
    </style>

</head>
<body>
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<style>
    p {
        font-size: 120%;
    }

    .col-lg-6:first-child {
        background-color: white;
    }

    .table-responsive {
        font-size: 120%;
        background-color: #eee;
    }

    .label-default {
        background-color: #337ab7;
    }
</style>

<?php
if ((isset($_COOKIE['registrated'])) || ($_POST["setlogin"] == "booleantrue")) {
    print("
					<ul class='nav nav-pills'>
					<li role='presentation' class='active'><a href='#'>Вход</a></li>
					<li role='presentation'><a href='./index.php'>Основное</a></li>
					<li role='presentation'><a href='./history.php'>История породы</a></li>
					<li role='presentation'><a href='./veterinary.php'>Уход</a></li>
					<li role='presentation'><a href='./other.php'>Спонсоры</a></li>
					<li role='presentation'><a href=''./about.php'>О нас</a></li>
					<li role='presentation'><a href='./canvas.php'>Canvas</a></li>
					<li role='presentation'><a href='#'>Javascript</a></li>
					<li role='presentation'><a href='./php.php'>PHP</a></li>
					<li role='presentation'><a href='./computergraph.php'>Графика</a></li>
					<li class='dropdown'>
					<a href='#' data-toggle='dropdown' class='dropdown-toggle'>
						Игры 
						<b class='caret'></b>
					</a>
						<ul class='dropdown-menu'>
							<li><a href='./citygame.php'>Игра \"Города\" на PHP</a></li>
							<li><a href='./snakegame.php'>Игра \"Змейка\" на JS</a></li>
						</ul>
					</li>
					</ul>

					<div class='container'>
					<form class='form-signin' action='./php/loginlogic/authorisation.php' method='POST'>
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
} //ФИЛЬТРАЦИЯ
else {
    print("
					<ul class='nav nav-pills'>
					<li role='presentation' class='active'><a href='#'>Регистрация</a></li>
					<li role='presentation'><a href='./index.php'>Основное</a></li>
					<li role='presentation'><a href='./history.php'>История породы</a></li>
					<li role='presentation'><a href='./veterinary.php'>Уход</a></li>
					<li role='presentation'><a href='./other.php'>Спонсоры</a></li>
					<li role='presentation'><a href=''./about.php'>О нас</a></li>
					<li role='presentation'><a href='./canvas.php'>Canvas</a></li>
					<li role='presentation'><a href='#'>Javascript</a></li>
					<li role='presentation'><a href='./php.php'>PHP</a></li>
					<li role='presentation'><a href='./computergraph.php'>Графика</a></li>
					<li class='dropdown'>
					<a href='#' data-toggle='dropdown' class='dropdown-toggle'>
						Игры 
						<b class='caret'></b>
					</a>
						<ul class='dropdown-menu'>
							<li><a href='./citygame.php'>Игра \"Города\" на PHP</a></li>
							<li><a href='./snakegame.php'>Игра \"Змейка\" на JS</a></li>
						</ul>
					</li>
					</ul>
					<div class='container'>
					<form class='form-signin' action='./php/loginlogic/registration.php' method='POST'>
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