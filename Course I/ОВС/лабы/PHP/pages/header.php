<?php

$BASEURL = "http://127.0.0.1:8888";

/*
В зависимости от вызываемой страницы присваевается active
*/
function PageDetector($PageNumber)
{
    $basename = basename($_SERVER["SCRIPT_FILENAME"]);
    $NavigatorArr = array(
        "login.php" => 1,
        "index.php" => 2,
        "task9.php" => 3,
        "pr.php" => 3,
        "start.php" => 3,
    );

    if (array_key_exists($basename, $NavigatorArr) && $NavigatorArr[$basename] == $PageNumber)
        return "'nav-link active'";
    return "'nav-link'";

}

print('
<!DOCtype html>
<html>
<head>
    <meta charset=“utf-8”>
    <title>Работы по ОВС</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="' . $BASEURL . '/css/bootstrap.css" rel="stylesheet">

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

    <li class="nav-item">');

if (isset($_COOKIE['logined']))
    print("<a class=" . PageDetector(1) . " href='#'><b>Добро пожаловать," . base64_decode($_COOKIE["logined"]) . "</b></a>");

else if (isset($_COOKIE['registrated']))
    print("<a class=" . PageDetector(1) . " href='" . $BASEURL . "/pages/login.php'>Вход</a>");

else
    print("<a class=" . PageDetector(1) . " href='" . $BASEURL . "/pages/login.php'>Регистрация</a>");

print('
    </li>

    <li class="nav-item">
        <a class=' . PageDetector(2) . ' href="' . $BASEURL . '/index.php">Основное</a>
    </li>
    <li class="nav-item">
        <a class=' . PageDetector(3) . ' href="' . $BASEURL . '/tasks/task9/task9.php">Работа с БД</a>
    </li>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true"
           aria-expanded="false">Работа с формами</a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task5.php">Задание №5</a>
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task6.php">Задание №6</a>
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task7.php">Задание №7</a>
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task8.php">Задание №8</a>
        </div>
    </li>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true"
           aria-expanded="false">Базовые задания</a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task1.php">Задание №1</a>
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task2.php">Задание №2</a>
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task3.php">Задание №3</a>
            <a class="dropdown-item" href="' . $BASEURL . '/tasks/task4.php">Задание №4</a>
        </div>
    </li>
</ul>');
?>