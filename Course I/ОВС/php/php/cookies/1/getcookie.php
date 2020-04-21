<?php

    $radiochoise_type_arr = array("1"=>"Недалеко от дома/работы", "2"=>"Увидел рекламу",  "3"=>"Посоветовали", "4"=>"Оптимальное соотношение цены и качества");
    $radiochoise_advice_arr = array("true"=>"Да", "false"=>"Нет");
    $food_kitchen_arr = array("1"=>"Русская", "2"=>"Армянская","3"=>"Грузинская","4"=>"Узбекская");
    print("<h3>Контактная информация</h3>Имя: ".$_COOKIE['name']."<br>");
    print("Телефон: ".$_COOKIE['phone']."<br>"); 
    print("E-mail: ".$_COOKIE['email']."<br>");
    print("Дата посещения: ".$_COOKIE['date']."<br>");

    print("<h3>Персональная информация</h3>Возраст: ".$_COOKIE['age']."<br>");
    print("Любимая кухня: ".$food_kitchen_arr[$_COOKIE['food_kitchen']]."<br>");
    print("Какие блюда вы бы хотели увидеть в меню? -->  ".$_COOKIE['food_list']."<br>");
    
    print("<h3>Оценка нашего заведения</h3>Почему вы выбрали наше заведение? -->  ".$radiochoise_type_arr[$_COOKIE['radiochoise_type']]."<br>");
    print("Вы будете рекомендовать наше заведение своим знакомым? -->  ".$radiochoise_advice_arr[$_COOKIE['radiochoise_advice']]."<br>");
?>