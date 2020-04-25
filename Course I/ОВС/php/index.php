<?php
require_once('./pages/header.php');


$tasks = array(
    array("type" => "Базовое задание", "link" => "/tasks/task1.php", "description" => "Пример использования переменных в ЯП PHP"),
    array("type" => "Базовое задание", "link" => "/tasks/task2.php", "description" => "Пример использования констант в ЯП PHP"),
    array("type" => "Базовое задание", "link" => "/tasks/task3.php", "description" => "Пример использования массивов в ЯП PHP"),
    array("type" => "Базовое задание", "link" => "/tasks/task4.php", "description" => "Работа с файлами в PHP. Счетчик количества посещений сайта"),
    array("type" => "Работа с формами", "link" => "/tasks/task5.php", "description" => "Пример работы с формами c полем text, password и radio. Запись результатов в файл"),
    array("type" => "Работа с формами", "link" => "/tasks/task6.php", "description" => "Пример формы с раскрывающимся списком и записью в файл"),
    array("type" => "Работа с формами", "link" => "/tasks/task7.php", "description" => "Пример формы обратной связи на PHP"),
    array("type" => "Работа с формами", "link" => "/tasks/task8.php", "description" => "Пример гостевой книги на PHP"),
    array("type" => "Работа с БД", "link" => "/tasks/task9/task9.php", "description" => "Пример работы с базами данных на PHP. Менеджмент товаров на складе."),

);


print('
<div class="jumbotron">
    <h1 class="display-4"><h1 class="display-4">Лабораторные работы PHP по ОВС</h1>
    <p class="lead">Деменчук Георгий, группа ПИ19-4</p>
    <hr class="my-4">
    <p>Здесь собраны все задания, связанные с защитой 3 практической по ОВС.</p>
    <a class="btn btn-primary btn-lg" href="https://github.com/GeorgiyDemo/FA" role="button">Github</a>
</div>

<div class="h2">
    Описание заданий
</div>
<div class="row">
    <div class="col-4">
        <div class="list-group" id="list-tab" role="tablist">');


for ($i = 0; $i < count($tasks); $i++)
    print(' <a class="list-group-item list-group-item-action" id="' . strval($i + 1) . '" data-toggle="list" href="#list' . strval($i + 1) . '" role="tab" >Задание №' . strval($i + 1) . '</a>');


print('
        </div>
    </div>
    <div class="col-8">
        <div class="tab-content" id="nav-tabContent">');

for ($i = 0; $i < count($tasks); $i++)
    print('<div class="tab-pane fade show" id="list' . strval($i + 1) . '" role="tabpanel" aria-labelledby="' . strval($i + 1) . '">
                
            <h3>' . $tasks[$i]["type"] . '</h3>' . $tasks[$i]["description"] . '<br><br>
            <a class="btn btn-outline-primary" href="' . $tasks[$i]["link"] . '">Перейти к заданию</a></div>');

print('
        </div>
    </div>
</div>
');

if (isset($_COOKIE['logined']))
    print("<form action='./loginlogic/exitbutton.php' method='POST'>
<button type='submit' class='btn btn-primary btn-lg'>Выход</button><br>
</form>");

require_once('./pages/footer.php');
print('</body></html>')

?>