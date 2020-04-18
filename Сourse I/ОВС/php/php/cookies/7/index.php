<?php 

    if ($_POST['send'] != "")
    {
        setcookie('firstname', $_POST['firstname']);
        setcookie('lastname', $_POST['lastname']);
        setcookie('datebirth', $_POST['datebirth']);
        header("Location: http://127.0.0.1:8888/SITE/php/cookies/7/test.php");
        exit;
    }

    else{

        if (isset($_COOKIE['firstname'])) {
            unset($_COOKIE['firstname']);
            setcookie('firstname', null, -1, '/');
        }
        if (isset($_COOKIE['lastname'])) {
            unset($_COOKIE['lastname']);
            setcookie('lastname', null, -1, '/');
        }
        if (isset($_COOKIE['datebirth'])) {
            unset($_COOKIE['datebirth']);
            setcookie('datebirth', null, -1, '/');
        }

        print("
            <h1>Форма информации</h1>
            <form method='post' action='index.php'>
                <table>
                    <tr>
                        <td><label for='firstname'>Фамилия</label></td>
                        <td><input type='text' name='firstname'></td>
                    </tr>

                    <tr>
                        <td><label for='lastname'>Имя</label></td>
                        <td><input type='text' name='lastname'></td>
                    </tr>

                    <tr>
                        <td><label for='datebirth'>Дата рождения</label></td>
                        <td><input type='date' name='datebirth'></td>
                    </tr>
                </table>
                <input type='submit' value='Отправить' name='send'>
            </form>
        ");
    }
?>