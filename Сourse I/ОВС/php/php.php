<!DOCtype html>

<html>
<head>
    <meta charset=“utf-8”>
    <title>Приют "Котикус"</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <style> [class*="col-"] {
            background-color: #eee;
            text-align: center;
            padding-top: 10px;
            padding-bottom: 10px;
            margin-bottom: 10px;
            font-size: 2rem;
        }
    </style>

</head>
<body>

<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<style>
    p {
        font-size: 120%;
    }

    .col-lg-6:first-child {
        background-color: white;
    }

    .table-responsive {
        font-size: 120%;
        background-color: #eee;
    }

    .label-default {
        background-color: #337ab7;
    }

    #table {
        font-size: 115%;
        background-color: #d6edf8;
        border: 1px solid black;
    }

    #table th {
        border-bottom: 1px solid black;
        padding: 0;
    }

    #table td {
        border: 1px solid black;
        padding: 0;
    }

    #table tr {
        border: 1px solid black;
    }

    select {
        margin-left: 1cm;
        margin-bottom: 0.5cm;
    }
</style>

<?php
if (isset($_COOKIE['logined'])) {
    print('
					<ul class="nav nav-pills">
					<li role="presentation"><a href="#"><b>Добро пожаловать, ' . base64_decode($_COOKIE['logined']) . '</b></a></li>
                    <li role="presentation"><a href="./index.php">Основное</a></li>
					<li role="presentation"><a href="./history.php">История породы</a></li>
					<li role="presentation"><a href="./veterinary.php">Уход</a></li>
					<li role="presentation"><a href="./other.php">Спонсоры</a></li>
					<li role="presentation"><a href="./about.php">О нас</a></li>
					<li role="presentation"><a href="./canvas.php">Canvas</a></li>
					<li role="presentation"><a href="./js.php">Javascript</a></li>
					<li role="presentation" class="active"><a href="#">PHP</a></li>
					<li role="presentation"><a href="./computergraph.php">Графика</a></li>
					<li class="dropdown">
					<a href="#" data-toggle="dropdown" class="dropdown-toggle">
						Игры 
						<b class="caret"></b>
					</a>
						<ul class="dropdown-menu">
							<li><a href="./citygame.php">Игра "Города" на PHP</a></li>
							<li><a href="./snakegame.php">Игра "Змейка" на JS</a></li>
						</ul>
					</li>
					</ul>'
    );
} else if (isset($_COOKIE['registrated'])) {
    print('
					<ul class="nav nav-pills">
					<li role="presentation"><a href="./login.php">Вход</a></li>
                    <li role="presentation"><a href="./index.php">Основное</a></li>
					<li role="presentation"><a href="./history.php">История породы</a></li>
					<li role="presentation"><a href="./veterinary.php">Уход</a></li>
					<li role="presentation"><a href="./other.php">Спонсоры</a></li>
					<li role="presentation"><a href="./about.php">О нас</a></li>
					<li role="presentation"><a href="./canvas.php">Canvas</a></li>
					<li role="presentation"><a href="./js.php">Javascript</a></li>
					<li role="presentation" class="active"><a href="#">PHP</a></li>
					<li role="presentation"><a href="./computergraph.php">Графика</a></li>
					<li class="dropdown">
					<a href="#" data-toggle="dropdown" class="dropdown-toggle">
						Игры 
						<b class="caret"></b>
					</a>
						<ul class="dropdown-menu">
							<li><a href="./citygame.php">Игра "Города" на PHP</a></li>
							<li><a href="./snakegame.php">Игра "Змейка" на JS</a></li>
						</ul>
					</li>
					</ul>'
    );
} else {
    print('
					<ul class="nav nav-pills">
					<li role="presentation"><a href="./login.php">Регистрация</a></li>
                    <li role="presentation"><a href="./index.php">Основное</a></li>
					<li role="presentation"><a href="./history.php">История породы</a></li>
					<li role="presentation"><a href="./veterinary.php">Уход</a></li>
					<li role="presentation"><a href="./other.php">Спонсоры</a></li>
					<li role="presentation"><a href="./about.php">О нас</a></li>
					<li role="presentation"><a href="./canvas.php">Canvas</a></li>
					<li role="presentation"><a href="./js.php">Javascript</a></li>
					<li role="presentation" class="active"><a href="#">PHP</a></li>
					<li role="presentation"><a href="./computergraph.php">Графика</a></li>
					<li class="dropdown">
					<a href="#" data-toggle="dropdown" class="dropdown-toggle">
						Игры 
						<b class="caret"></b>
					</a>
						<ul class="dropdown-menu">
							<li><a href="./citygame.php">Игра "Города" на PHP</a></li>
							<li><a href="./snakegame.php">Игра "Змейка" на JS</a></li>
						</ul>
					</li>
					</ul>'
    );
}
?>

<div class="alert alert-info" role="alert">В данном разделе представлены все работы, связанные с PHP</div>

<div class="container">
    <h2>Практика с сортировкой массива</h2>
    <div>
        <?php
        $link = mysqli_connect("localhost", "root", "root", "SortDatabaseExample");
        $array = [];
        if ($result = mysqli_query($link, "SELECT * FROM Datatable")) {
            while ($stringresult = $result->fetch_array())
                array_push($array, array(
                        'id' => $stringresult["id"],
                        'age' => $stringresult["age"],
                        'gender' => $stringresult["gender"],
                        'login' => $stringresult["login"])
                );
            mysqli_free_result($result);
        }

        print
            ("
                    <form method = 'POST'>
                    Параметры сортировки:
                    <br>
                    
                    <select name='firstkey'>
                        <option value='id'>id</option>
                        <option value='age'>age</option>
                        <option value='gender'>gender</option>
                        <option value='login'>login</option>
                    </select>

                    <select name='secondkey'>
                        <option value='id'>id</option>
                        <option value='age'>age</option>
                        <option value='gender'>gender</option>
                        <option value='login'>login </option>
                    
                        </select>
                    
                    <br>
                    
                    <table id = 'tableselect1'>
                    
                    <tr>
                    <td><input type='radio' name='firstsortparam' value='true' checked>По возрастанию</td>
                    <td><input type='radio' name='secondsortparam' value='true' checked>По возрастанию</td>
                    </tr>

                    <tr>
                    <td><input type='radio' name='firstsortparam' value='false'>По убыванию</td>       
                    <td><input type='radio' name='secondsortparam' value='false'>По убыванию</td>
                    </tr>
                    </table>
                    <br>
                    <input type='submit' name='ex9' value='Сортировать' />
                </form>
                <br>
                Результат:
                ");

        $firstparam = $_POST['firstsortparam'];
        $secondparam = $_POST['secondsortparam'];

        $firstkey = $_POST['firstkey'];
        $secondkey = $_POST['secondkey'];

        for ($i = 0; $i < count($array); $i++)
            for ($j = $i + 1; $j < count($array); $j++) {
                if (($array[$i][$firstkey] > $array[$j][$firstkey] && $firstparam == "true") || ($array[$i][$firstkey] < $array[$j][$firstkey] && $firstparam == "false")) {
                    $bufkey1 = $array[$i];
                    $array[$i] = $array[$j];
                    $array[$j] = $bufkey1;
                }
            }

        for ($i = 0; $i < count($array); $i++)
            for ($j = $i + 1; $j < count($array); $j++) {
                if ($array[$i][$firstkey] == $array[$j][$firstkey] && (($array[$i][$secondkey] > $array[$j][$secondkey] && $secondparam == "true") || ($array[$i][$secondkey] < $array[$j][$secondkey] && $secondparam == "false"))) {
                    $bufkey2 = $array[$i];
                    $array[$i] = $array[$j];
                    $array[$j] = $bufkey2;
                }
            }

        print(
        "
                <br>
                <table id = 'table'>
                <tr>
                    <td><b>id&#8195;</b></td>
                    <td><b>age&#8195;</b></td>
                    <td><b>gender&#8195;</b></td>
                    <td><b>login&#8195;</b></td>
                </tr>"
        );

        foreach ($array as $element) {
            print("<tr>");
            foreach ($element as $value)
                print("<td>" . $value . "</td>");
            print("</tr>");
        }
        print("</table>");

        ?>

    </div>
    <h2>Практики с документа Word</h2>
    <table class="table table-hover">
        <thead>
        <tr>
            <th>№</th>
            <th>Описание</th>
            <th>Задание</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>Вам нужно разработать программу, которая считала бы сумму цифр числа введенного пользователем. Например:
                есть число 123, то программа должна вычислить сумму цифр 1, 2, 3, т. е. 6.
                По желанию можете сделать проверку на корректность введения данных пользователем.
            </td>
            <td>
                <form action="./php/doc/1.php" method="POST">
                    <input type="text" name="number"/>
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>2</td>
            <td>Вам нужно разработать программу, которая считала бы количество вхождений какой-нибудь выбранной вами
                цифры в выбранном вами числе. Например: цифра 5 в числе 442158755745 встречается 4 раза
            </td>
            <td>
                <form action="./php/doc/2.php" method="POST">
                    Введите число
                    <input type="text" name="number"/>
                    Введите подстроку
                    <input type="text" name="count_number"/>
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>3</td>
            <td>Разработайте программу, которая из чисел 20 .. 45 находила те, которые делятся на 5 и найдите сумму этих
                чисел. Рекомендую использовать функцию fmod для определения "делится число" или "не делится".
            </td>
            <td>
                <form action="./php/doc/3.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>4</td>
            <td>Ваше задание — создать массив, наполнить его случайными значениями (можно использовать функцию rand),
                найти максимальное и минимальное значение массива и поменять их местами.
            </td>
            <td>
                <form action="./php/doc/4.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>5</td>
            <td>Вам нужно создать массив и заполнить его случайными числами от 1 до 100 (ф-я rand). Далее, вычислить
                произведение тех элементов, которые больше ноля и у которых парные индексы. После вывести на экран
                элементы, которые больше ноля и у которых не парный индекс.
            </td>
            <td>
                <form action="./php/doc/5.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>6</td>
            <td>Ваши задание будет создание создание сокращенного варианта ФИО, т. е.
                вводим: Иванов Иван Петрович и нам выводит: Иванов И. П.
            </td>
            <td>
                <form action="./php/doc/6.php" method="POST">
                    ФИО: <input type="text" name="name">
                    <input type="submit" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>7</td>
            <td>Разработайте программу, которая определяла количество прошедших часов по введенным пользователем
                градусах. Введенное число может быть от 0 до 360.
            </td>
            <td>
                <form action="./php/doc/7.php" method="POST">
                    Введите число:
                    <input type="text" name="number"/>
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>9</td>
            <td>Вам нужно разработать программу, которая проверяла бы введенное пользователем число (год). Число может
                быть в диапазоне от 1 до 9999
            </td>
            <td>
                <form action="./php/doc/9.php" method="POST">
                    Введите число:
                    <input type="text" name="year"/>
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>

        <tr>
            <td>10</td>
            <td>Игральным картам присвоены следующие порядковые номера в зависимости от их достоинства: "валет" - 11,
                "дама" - 12, "король" - 13, "туз" - 14. Порядковые номера остальных карт соответствуют их
                названиям("семерка", "восмерка" и т. д.). Вам нужно разработать программу, которая выводила достоинство
                карты по заданному номеру, который будет вводит пользователь.
            </td>
            <td>
                <form action="./php/doc/10.php" method="POST">
                    Введите число:
                    <input type="text" name="karta"/>
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>11</td>
            <td>Составить программу, которая бы по заданному числу выводила его название по китайском календаре.
                Заданное число не может быть меньше 1924.
            </td>
            <td>
                <form action="./php/doc/11.php" method="POST">
                    Год: <input type="text" name="year">
                    <input type="submit" value="Отправить">
                </form>
            </td>
        </tr>
        </tbody>
    </table>

    <h2>Практики с презентации PowerPoint</h2>
    <table class="table table-hover">
        <thead>
        <tr>
            <th>№</th>
            <th>Описание</th>
            <th>Задание</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>Создайте файл 1-1.php, содержащий 5 раных переменных, присвойте переменным значения разного типа.
                Используя gettype() выведите тип каждой переменной.
            </td>
            <td>
                <form action="./php/ppt/1-1.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>2</td>
            <td>Создайте файл 1-2.php, содержаций 2 переменные числового типа. Произвидите над переменными произвольное
                арифметическое действие и выведите его результат.
            </td>
            <td>
                <form action="./php/ppt/1-2.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>3</td>
            <td>Создайте файл 1-3.php, содержащий 2 переменные строкового типа. Инициализируйте переменные произвольным
                текстом. С помощью конкатинации объедините содержимое переменных и выведите результат.
            </td>
            <td>
                <form action="./php/ppt/1-3.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>4</td>
            <td>Создайте файл 1-4.php, содержащий 2 переменные с одинаковым типом значений. Используя тернарный оператор
                сравнения проведите исследование на возвращаемые результаты.
            </td>
            <td>
                <form action="./php/ppt/1-4.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>5</td>
            <td>Используя условный переход, выведите сообщение «Счастливчик!» если $age попадает в диапазон между 19 и
                35. Если значение иное, выведите «Не повезло». Расширьте предыдущую конструкцию сообщением «Слишком
                молод», если $age в диапазоне между 1 и 17
            </td>
            <td>
                <form action="./php/ppt/1-5.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>6</td>
            <td>Используя циклы, сформируйте массив четных чисел из диапазона от 1 до 100. Выводя массив на экран,
                исключите из вывода все числа, которые не делятся на 5.
            </td>
            <td>
                <form action="./php/ppt/1-6.php" method="POST">
                    <input type="submit" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>7</td>
            <td>Создайте массив со следующими элементами: Name, Address, Phone, Mail и заполните его. С помощью цикла
                foreach осуществите форматированный вывод массива в виде: «элемент: значение»
            </td>
            <td>
                <form action="./php/ppt/1-7.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        </tbody>
    </table>

    <h2>Практики по работе с cookies</h2>
    <table class="table table-hover">
        <thead>
        <tr>
            <th>№</th>
            <th>Описание</th>
            <th>Задание</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>Создайте два PHP-скрипта: index.php и test.php. Сделайте в первом скрипте index.php форму опроса
                пользователя с предложенными ниже в заданиях параметрами (или в варианте 8-9 просто заполните параметры
                нужными значениями). Сохраните значения введенных параметров в переменных массива $_COOKIE или
                $_SESSION. Передайте управление скрипту test.php без использования GET или POST запросов.
            </td>
            <td>
                <form action="./php/cookies/1/phpcookie.html" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>2</td>
            <td>В index.php предложите пользователю выбрать цвет ссылок и цвет фона страницы с помощью выпадающего
                списка. В test.php окрасьте страницу и гиперссылки в тексте в выбранные цвета.
            </td>
            <td>
                <form action="./php/cookies/2/getcookie.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>3</td>
            <td>В index.php спросите с помощью формы город и возраст пользователя. В test.php сделайте форму с полями
                'Имя', 'Возраст', 'Город' причем поля 'Возраст' и 'Город' заполните уже известными значениями.
            </td>
            <td>
                <form action="./php/cookies/3/" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>4</td>
            <td>В index.php сделайте 5 картинок с товарами и ценой. Реализуйте корзину в test.php. Под каждой картинкой
                должна быть ссылка 'положить в корзину'. По нажатию на эту ссылку этот товар должен попасть в корзину и
                посчитаться общая сумма товара, которую должен заплатить пользователь.
            </td>
            <td>
                <form action="./php/cookies/4/" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>5</td>
            <td>На страницах index.php и test.php покажите пользователю баннер с кнопкой 'Не показывать больше'. Если он
                нажмет на эту кнопку — не показывайте ему баннер в течении 5 минут.
            </td>
            <td>
                <form action="./php/cookies/5/" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>6</td>
            <td>В index.php спросите дату рождения пользователя. В test.php напишите сколько дней осталось до его дня
                рождения. Если сегодня день рождения пользователя — поздравьте его!
            </td>
            <td>
                <form action="./php/cookies/6/" method="POST">
                    <input type="submit" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>7</td>
            <td>В index.php создайте форму теста-опросника с двумя вопросами и несколькими вариантами ответов. В
                test.php подведите итоги опроса. Разрешите пользователю менять свои ответы.
            </td>
            <td>
                <form action="./php/cookies/7/" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>8</td>
            <td>Создайте вариант игры "Спортлото 6 из 36". В index.php пользователь выбирает 6 номеров из 36. В test.php
                показывается количество угаданных.
            </td>
            <td>
                <form action="./php/cookies/8/index.php" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>9</td>
            <td>Сделайте счетчик обновления страницы index.php пользователем. Скрипт test.php должен выводить на экран
                количество обновлений страницы index.php. При первом заходе на страницу index.php он должен вывести
                сообщение о том, что вы еще не обновляли страницу.
            </td>
            <td>
                <form action="./php/cookies/9/" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        <tr>
            <td>10</td>
            <td>Запомните время первого захода пользователя на страницу index.php. На странице test.php выводите сколько
                секунд назад пользователь зашел на сайт.
            </td>
            <td>
                <form action="./php/cookies/10/" method="POST">
                    <input type="submit" name="send" value="Отправить">
                </form>
            </td>
        </tr>
        </tbody>
    </table>

    <?php
    if (isset($_COOKIE['logined'])) {
        print("
                    <form action='./php/loginlogic/exitbutton.php' method='POST'>
                    <button type='submit' class='btn btn-primary btn-lg'>Выход</button><br>
                    </form>");
    }
    ?>

    <small>Данная организация работает исключительно на деньги с ВАШИХ пожертвований</small>
</body>

</html>