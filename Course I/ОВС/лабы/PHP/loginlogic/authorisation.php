<?php
$userlogin = md5($_POST["login"]);
$userpassword = md5($_POST["pass"]);
require_once('../tasks/connector.php');

if (mysqli_connect_errno()) {
    printf("Не удалось подключиться: %s\n", mysqli_connect_error());
    exit();
}

$result = mysqli_query($link, "SELECT name FROM Users WHERE (login='" . $userlogin . "' AND password='" . $userpassword . "')");
if ($result->num_rows != 0) {
    setcookie('logined', $result->fetch_assoc()["name"], time() + 60 * 60 * 24 * 30, '/');
    header("Location: ".$URLADDRESS."/index.php");
    exit;
} else {
    print(
    "<script>
      if(!alert('Неверная пара логин/пароль'))
        document.location = '".$URLADDRESS."/pages/login.php';
    </script>"
    );
}
mysqli_free_result($result);
mysqli_close($link);
?>