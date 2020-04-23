<?php


  $link = mysqli_connect("127.0.0.1", "root", "root", "OVS", "8889");

  $userlogin = md5($_POST['login']);
  $userpassword = md5($_POST['pass']);
  $username = base64_encode($_POST['name']);
  
  if (mysqli_connect_errno())
  {
      printf("Ошибка соединения: %s\n", mysqli_connect_error());
      exit();
  }

  $result = mysqli_query($link, "INSERT INTO Users (login, password, name) VALUES ('$userlogin', '$userpassword', '$username')");
  var_dump($result);
  
  if ($result === TRUE)
  {
    setcookie('registrated', 'true', time() + 60*60*24*30, '/');
    header("Location: http://127.0.0.1:8888/index.php");
    exit;
  }

  else
  {
    print(
      "<script>
        if(!alert('Пользователь с таким логином уже зарегистрирован'))
          document.location = 'http://127.0.0.1:8888/login.php';
      </script>"
    );
  }

  $mysqli->close();

?>