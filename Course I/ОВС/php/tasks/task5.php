<html>
    <body>
<?php
    //Пример работ с формами c полем text,password и radio. Заись результатов в файл
    $username = $_POST['username'];
    if((isset($username)) && ($username != ""))
        
        print("Привет   ". $username.'<FORM name="my_form" METHOD="POST">
        <input
            type="submit" value="Выйти из системы"
            name="exit_system"
            title="">
            </form>'
        );

    else
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

?>
</body>
</html>


