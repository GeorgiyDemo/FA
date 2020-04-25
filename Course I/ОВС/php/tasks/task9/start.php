<?php
require_once('../../pages/header.php');
if (isset($_POST['enterStart'])) // Проверка - является ли скрипт результатом ввода формы
{
    require_once('../connector.php');

    $pass = md5($_POST['password']);
    $sql = "SELECT name, password FROM task9_users WHERE id=" . $_POST['id'] . " and password='" . $pass . "'";
    $result = mysqli_query($link, $sql);
    if ($result->num_rows == 0)

        die('Неверный пароль <br><a href="index.php"><br>
         Вернуться на главную страницу </a>');
    else
        print("Авторизация прошла успешно!!!
    <form action='pr.php' method='post'>
    <input name='add1' type='submit'
    value='Перейти к работе'></form>");


} else

    print('<a  href="index.php">Вернуться на главную страницу </a>');

?>
