<?php

if (isset($_COOKIE['logined'])) {
    unset($_COOKIE['logined']);
    setcookie('logined', null, -1, '/');
}

header("Location: http://127.0.0.1:8888/index.php");
exit;

?>