<?php
require_once('./pages/header.php');

print('
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
');

if (isset($_COOKIE['logined']))
    print("<form action='./loginlogic/exitbutton.php' method='POST'>
<button type='submit' class='btn btn-primary btn-lg'>Выход</button><br>
</form>");

print('</body></html>')

?>