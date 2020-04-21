<?php 
    if ($_POST['send'] != "")    
    {
        setcookie('numbers', $_POST['numbers']);
        header("Location: http://127.0.0.1:8888/SITE/php/cookies/8/test.php");
        exit;
    }
    else
    {
        print
        (
            "<form method='POST' acton='index.php'>
            <label>Введите числа (через запятую)</label>
            <input type='text' name='numbers'>
            <input type='submit' value='Отправить' name='send'>
            </form>"
        );
    }  
?>