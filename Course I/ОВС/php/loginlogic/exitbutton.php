<?php
require_once('../tasks/connector.php');
if (isset($_COOKIE['logined'])) {
    unset($_COOKIE['logined']);
    setcookie('logined', null, -1, '/');
}

header("Location: ".$URLADDRESS."/index.php");
exit;

?>