<!DOCtype html>

<html>
<head>
    <meta charset=“utf-8”>
    <title>Работы по ОВС</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.css" rel="stylesheet">

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
        if (isset($_COOKIE['logined']))
            print("<a class='nav-link' href='#'><b>Добро пожаловать,".base64_decode($_COOKIE["logined"])."</b></a>");
        
        else if (isset($_COOKIE['registrated']))
            print("<a class='nav-link' href='./login.php'>Вход</a>");
        
        else
            print("<a class='nav-link' href='./login.php'>Регистрация</a>");
        ?>
    </li>

    <li class="nav-item">
        <a class="nav-link active" href="#">Основное</a>
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

<div class="jumbotron">
    <h1 class="display-4">Лаба ОВС</h1>
    <p class="lead">Да пацаны, ето жестко © Джейсон Стетхем</p>
    <hr class="my-4">
    <p>Здесь собраны все задания, связанные с защитой 3 практической по ОВС.</p>
    <a class="btn btn-primary btn-lg" href="https://github.com/GeorgiyDemo/FA" role="button">Мой Github</a>
</div>

<div class="h2">
    Описание каждого задания
</div>
<div class="row">
    <div class="col-4">
        <div class="list-group" id="list-tab" role="tablist">
            <a class="list-group-item list-group-item-action active" id="list-home-list" data-toggle="list" href="#list-home" role="tab" aria-controls="home">Home</a>
            <a class="list-group-item list-group-item-action" id="list-profile-list" data-toggle="list" href="#list-profile" role="tab" aria-controls="profile">Profile</a>
            <a class="list-group-item list-group-item-action" id="list-messages-list" data-toggle="list" href="#list-messages" role="tab" aria-controls="messages">Messages</a>
            <a class="list-group-item list-group-item-action" id="list-settings-list" data-toggle="list" href="#list-settings" role="tab" aria-controls="settings">Settings</a>
        </div>
    </div>
    <div class="col-8">
        <div class="tab-content" id="nav-tabContent">
            <div class="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list">цукцукцуцу</div>
            <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">ееееееее</div>
            <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">аааааааа</div>
            <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">ччччч</div>
        </div>
    </div>
</div>

<?php
if (isset($_COOKIE['logined'])) {
    print("
				<form action='./php/loginlogic/exitbutton.php' method='POST'>
				<button type='submit' class='btn btn-primary btn-lg'>Выход</button><br>
				</form>");
}
?>

</body>

</html>