<!DOCtype html>

<html>
<head>
    <meta charset=“utf-8”>
    <title>Работы по ОВС</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.css" rel="stylesheet">

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
    <li class="nav-item">
        <a class="nav-link" href="./login.php">Регистрация</a>
    </li>
    <li class="nav-item">
        <a class="nav-link active" href="#">Основное</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#">Работа с БД</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#">Работа с формами</a>
    </li>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true"
           aria-expanded="false">Базовые задания</a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="#">№1</a>
            <a class="dropdown-item" href="#">№2</a>
            <a class="dropdown-item" href="#">№3</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">Separated link</a>
        </div>
    </li>
</ul>

<div class="jumbotron">
    <h1 class="display-4">Лаба ОВС</h1>
    <p class="lead">Да пацаны, ето жестко © Джейсон Стетхем</p>
    <hr class="my-4">
    <p>Здесь собраны все задания, связанные с защитой 3 практической по ОВС.</p>
    <a class="btn btn-primary btn-lg" href="https://github.com/GeorgiyDemo/FA" role="button">Мой Github</a>
</div>

<div class="h2">
    Описание каждого задания
</div>
<div class="row">
    <div class="col-4">
        <div class="list-group" id="list-tab" role="tablist">
            <a class="list-group-item list-group-item-action active" id="list-home-list" data-toggle="list" href="#list-home" role="tab" aria-controls="home">Home</a>
            <a class="list-group-item list-group-item-action" id="list-profile-list" data-toggle="list" href="#list-profile" role="tab" aria-controls="profile">Profile</a>
            <a class="list-group-item list-group-item-action" id="list-messages-list" data-toggle="list" href="#list-messages" role="tab" aria-controls="messages">Messages</a>
            <a class="list-group-item list-group-item-action" id="list-settings-list" data-toggle="list" href="#list-settings" role="tab" aria-controls="settings">Settings</a>
        </div>
    </div>
    <div class="col-8">
        <div class="tab-content" id="nav-tabContent">
            <div class="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list">цукцукцуцу</div>
            <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">ееееееее</div>
            <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">аааааааа</div>
            <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">ччччч</div>
        </div>
    </div>
</div>
<?php
/*
if (isset($_COOKIE['logined']))
{
    print('
    <ul class="nav nav-pills">
    <li class="nav-item">
        <a class="nav-link active" href="#"><b>Добро пожаловать, '.base64_decode($_COOKIE['logined']).'</b></a>
    </li>
    <li class="nav-item">
        <a class="nav-link active" href="#">Основное</a>
    </li>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Задания PHP</a>
        <div class="dropdown-menu">
        <a class="dropdown-item" href="#">Action</a>
        <a class="dropdown-item" href="#">Another action</a>
        <a class="dropdown-item" href="#">Something else here</a>
        <div class="dropdown-divider"></div>
        <a class="dropdown-item" href="#">Separated link</a>
        </div>
    </li>
    </ul>'
        );
}

else if (isset($_COOKIE['registrated']))
    {
        print('
        <ul class="nav nav-pills">
        <li class="nav-item">
                <a class="nav-link active" href="./login.php"><b>Вход</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" href="#">Основное</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Задания PHP</a>
                <div class="dropdown-menu">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <a class="dropdown-item" href="#">Something else here</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Separated link</a>
                </div>
            </li>
            </ul>'
        );
    }

else
{
        print('
        <ul class="nav nav-pills">
        <li class="nav-item">
                <a class="nav-link active" href="./login.php"><b>Регистрация</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" href="#">Основное</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Задания PHP</a>
                <div class="dropdown-menu">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <a class="dropdown-item" href="#">Something else here</a>
                    <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Separated link</a>
                    </div>
            </li>
        </ul>'
        );
}
*/
?>

<h4>Уже приютили 20% от всех кошек</h4>
<div class="progress">
    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 20%;">20%
    </div>
</div>

<div class="row">
    <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
            <img src="./img/cat1.jpg" alt="...">
            <div class="caption">
                <h3>ЛАСКУН</h3>
                <p><a href="#" class="btn btn-primary" role="button">Купить</a></p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
            <img src="./img/cat2.jpg" alt="...">
            <div class="caption">
                <h3>ВИТОША</h3>
                <p><a href="#" class="btn btn-primary" role="button">Купить</a></p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
            <img src="./img/cat3.jpg" alt="...">
            <div class="caption">
                <h3>МАХА</h3>
                <p><a href="#" class="btn btn-primary" role="button">Купить</a></p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
            <img src="./img/cat4.jpg" alt="...">
            <div class="caption">
                <h3>КАРИНА</h3>
                <p><a href="#" class="btn btn-primary" role="button">Купить</a></p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
            <img src="./img/cat5.jpg" alt="...">
            <div class="caption">
                <h3>РОБИНЗОН</h3>
                <p><a href="#" class="btn btn-primary" role="button">Купить</a></p>
            </div>
        </div>
    </div>

    <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
            <img src="./img/cat6.jpg" alt="...">
            <div class="caption">
                <h3>ПЕТРАКОВ</h3>
                <p><a href="#" class="btn btn-primary" role="button">Купить</a></p>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-lg-6">
        <div class="input-group">
            <input type="text" class="form-control" placeholder="Поиск...">
            <span class="input-group-btn" .bg-light>
        <button class="btn btn-default" type="button">
        	<span class="glyphicon glyphicon-search" aria-hidden="true"></span>
        </button>
      </span>
        </div>
    </div>
</div>
<h2>Характер <span class="label label-default">индивидуально</span></h2>
<p>Активные кошки. Нуждаются во внимании, любят физический контакт. Общительные, ласковые и доверчивые. Кошки из
    сиамо-ориентальной группы умеют пользоваться своими голосовыми связками, меняя тональность и высоту звука для
    выражения своих требований и чувств. Легко поддаются дрессировке.</p>

<h2>Виды</h2>
<p>Существует несколько подвидов данной породы:</p>
<div class="table-responsive">
    <table class="table">
        <thead>
        <tr>
            <th>Вид</th>
            <th>Описание</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>Балийская</td>
            <td>длинношёрстная порода кошек</td>
        </tr>
        <tr>
            <td>Бурманская</td>
            <td>порода кошек, выведенная из породы «Wong Mau». Джозеф Томпсон обнаружил её в Бирме в 1930 году. Он
                привез её в Калифорнию, где и была выведена бирманская порода кошек путём скрещивания «Wong Mau» с
                сиамской.
            </td>
        </tr>
        <tr>
            <td>Гималайская</td>
            <td>длинношёрстная порода кошек, выведенная путём скрещивания персидской и сиамской кошки.</td>
        </tr>
        <tr>
            <td>Яванская (Ориентальная длинношёрстная)</td>
            <td>длинношёрстная порода кошек</td>
        </tr>
        <tr>
            <td>Тайская</td>
            <td>старотипный экстерьер сиамской кошки. Сохранён. Сейчас выделен в отдельную породу.</td>
        </tr>
        </tbody>
    </table>
</div>

<h2>Внешний вид</h2>

<p>Современная сиамская кошка имеет весьма характерную внешность, отличительными чертами которой являются тонкое,
    длинное, трубообразное гибкое тело, голова в виде длинного клина, большие миндалевидные косо поставленные глаза
    ярко-синего цвета, очень большие уши, широкие в основании и заостренные на концах, поставленные таким образом, чтобы
    между мочкой носа и кончиками ушей образовывался равносторонний треугольник. Шерсть короткая, плотно прилегающая к
    телу, без подшерстка. Очень длинный хлыстообразный хвост, тонкий от самого основания с заостренным длинным
    кончиком.</p>
<p>Для сиамских кошек характерен окрас колор-поинт (светлая шерсть с более тёмным окрасом на лапах, морде, ушах и
    хвосте). Такой окрас — это проявление неполного альбинизма, называемого акромеланизм. Действие акромеланизма связано
    с температурными особенностями живого организма: в теплых частях тела вырабатывается меньше пигмента, чем в
    холодных, поэтому уши, лапы, хвост и морда окрашены в более тёмный по сравнению с остальным телом цвет. С возрастом
    контраст поинтов по сравнению с телом может стать меньше. После года большинство кошек поинтового окраса имеют
    затемнение по корпусу. Сиамские котята рождаются абсолютно белыми, через несколько дней после рождения начинают
    темнеть поинты, окончательно окрас устанавливается в 6—10 месяцев.</p>
<small>Данная организация работает исключительно на деньги с ВАШИХ пожертвований</small>

<?php
if (isset($_COOKIE['logined'])) {
    print("
				<form action='./php/loginlogic/exitbutton.php' method='POST'>
				<button type='submit' class='btn btn-primary btn-lg'>Выход</button><br>
				</form>");
}
?>

</body>

</html>