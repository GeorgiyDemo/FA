<?php
$userlogin = md5($_POST["login"]);
$userpassword = md5($_POST["pass"]);

$link = mysqli_connect("localhost", "root", "root", "Pract5");

if (mysqli_connect_errno()) {
    printf("Не удалось подключиться: %s\n", mysqli_connect_error());
    exit();
}

$result = mysqli_query($link, "SELECT name FROM Site1 WHERE (login='".$userlogin."' AND pass='".$userpassword."')");
if ($result->num_rows != 0)
{
  setcookie('logined', $result->fetch_assoc()["name"], time() + 60*60*24*30, '/');
  header("Location: http://127.0.0.1:8888/SITE/index.php");
  exit;
}
else
{
  print(
    "<script>
      if(!alert('Неверная пара логин/пароль'))
        document.location = 'http://127.0.0.1:8888/SITE/login.php';
    </script>"
  );
}
mysqli_free_result($result);
mysqli_close($link);
?>