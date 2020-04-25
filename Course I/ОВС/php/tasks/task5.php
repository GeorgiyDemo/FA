<?php
require_once('../pages/header.php');
require_once('connector.php');
//Пример работ с формами c полем text, password и radio. Запись результатов в файл
print("Пример работы с формами c полем text, password и radio. Запись результатов в файл");
$username = $_POST['username'];
$password = $_POST['password'];
$filename = "task5_data.txt";
$tablename = "task5";
if (isset($username) && ($username != "")) {
    //1234
    if ((isset($password)) && (md5($password) == "81dc9bdb52d04dc20036dbd8313ed055")) {
        $radiodata = $_POST["ways"];


        if (mysqli_connect_errno()) {
            printf("Не удалось подключиться: %s\n", mysqli_connect_error());
            exit();
        }
        mysqli_query($link, "INSERT INTO task5 (name, radiobutton) VALUES ('" . $username . "','" . $radiodata . "')");
        //Работа с файлом
        $f = fopen($filename, 'at');
        $text = "\n" . $username . " : " . $radiodata;
        fwrite($f, $text);
        fclose($f);

        print('
                    <h3>Привет ' . $username . '!</h3>Ты успешно авторизовался с правильным паролем<br>Тобой был выбран вариант radiobutton №' . $radiodata . '
                    <br><br>Запишем это в БД в таблицу ' . $tablename . " и файл" . $filename . ' 
                    <FORM name="my_form" METHOD="POST">
                    <input
                    type="submit" value="Выйти из системы"
                    name="exit_system"
                    title="">
                    </form>'
        );

    } else
        print("<h3>Привет " . $username . '!</h3>Не удалось авторизоваться в системе, поробуй еще раз.<FORM name="my_form" METHOD="POST">
            <input
                type="submit" value="Попробовать еще раз"
                name="exit_system"
                title="">
                </form>'
        );
} else
    print(
    '<FORM name="my_form" METHOD="POST">
            Представьтесь: 
        <INPUT TYPE = "TEXT" NAME = "username"
            value=""
            title="Поле для ввода имени">
        <br>Введите пароль: 
        <INPUT TYPE = "password" NAME = "password"
            value=""     title="Поле для ввода пароля">
        
        <br>
        <input  type="radio"  Name="ways"  Value="1"
            >Установка первого варианта
        <br><input  type="radio"  Name="ways"  Value="2"
          checked>Установка второго варианта
          <br>
          
        <input
            type="submit" value="Войти в систему"
            name="enter_system"
            title="Нажмите, если Вы ввели имя, чтобы увидеть 
            результат">
            </form>'
    );
mysqli_close($link);

print('</body></html>')
?>
