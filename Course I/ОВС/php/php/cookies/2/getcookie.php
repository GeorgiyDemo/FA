<?php
print(
  "<style type='text/css'>
  p {
    color: white;
  }
  body {
    background:".$_COOKIE["color"]."
  }
  a {
    color: white;
  }
  </style>".
    "<p>Цвет фона:</p><form action='getcookie.php' method='post'>
      <select id='background' name='background'>
        <option value='black'>Черный</option>
        <option value='silver'>Серый</option>
        <option value='red'>Красный</option>
        <option value='maroon'>Бордовый</option>
        <option value='yellow'>Желтый</option>
        <option value='lime'>Лайм</option>
        <option value='green'>Зеленый</option>
        <option value='aqua'>Аква</option>
        <option value='teal'>Морская волна</option>
        <option value='blue'>Голубой</option>
        <option value='navy'>Синий</option>
        <option value='fuchsia'>Фуксия</option>
        <option value='purple'>Фиолетовый</option>
      </select>
    <input type='submit' value='Выбрать'>
    </form>".

    "<p>Цвет текста и ссылок:</p><form action='getcookie.php' method='post'>
    <select id='textcolor' name='textcolor'>
    <option value='black'>Черный</option>
    <option value='silver'>Серый</option>
    <option value='red'>Красный</option>
    <option value='maroon'>Бордовый</option>
    <option value='yellow'>Желтый</option>
    <option value='lime'>Лайм</option>
    <option value='green'>Зеленый</option>
    <option value='aqua'>Аква</option>
    <option value='teal'>Морская волна</option>
    <option value='blue'>Голубой</option>
    <option value='navy'>Синий</option>
    <option value='fuchsia'>Фуксия</option>
    <option value='purple'>Фиолетовый</option>
    </select>
    <input type='submit' value='Выбрать'>
    </form>".
    "<a href='URL'>Ссылка №1</a><br>".
    "<a href='URL'>Ссылка №2</a><br>".
    "<a href='URL'>Ссылка №3</a><br>"
);

if ($_POST["background"] != Null)
{
    $styleBlock = sprintf('
      <style type="text/css">
         body {
           background:%s
         }
      </style>
      
    ', $_POST["background"]);
    SetCookie("color",$_POST["background"],time()+3600);
    print($styleBlock);
}

if ($_POST["textcolor"] != Null)
{
    $color = $_POST["textcolor"];
    $styleBlock = sprintf('
      <style type="text/css">
      p{
        color:%s
      }
      a {
        color:%s
      }
      </style>
      
    ', $color, $color);
    SetCookie("textcolor",$_POST["textcolor"],time()+3600);
    print($styleBlock);
}

?>