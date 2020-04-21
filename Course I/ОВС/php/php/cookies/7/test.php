<?php 

    if ((!isset($_COOKIE['firstname'])) || (!isset($_COOKIE['firstname'])) || (!isset($_COOKIE['firstname'])))
    {
        header("Location: http://127.0.0.1:8888/SITE/php/cookies/7/index.php");
        exit;
    }

    else
    {
        var_dump($_COOKIE);
        $firstname = $_COOKIE['firstname'];
        $lastname  = $_COOKIE['lastname'];
        $datebirth = explode('-', $_COOKIE['datebirth']);

            print("
                <h1>Результаты теста</h1>
                <table>
                    <tr>
                        <td>Фамилия</td>
                        <td>".$lastname."</td>
                    </tr>
                    <tr>
                        <td> Имя </td>
                        <td>".$firstname."</td>
                    </tr>
                    <tr>
                        <td> День рождения </td>
                        <td> ".$datebirth[2].".".$datebirth[1].".".$datebirth[0]." </td>
                    </tr>
                </table>
                <a href='index.php'>Изменить результаты теста</a>
            ");
    }

?>