<?php
$mas = array('Room1' => 'Офис', 'Room1' => 'Склад', 55 => 100);
foreach ($mas as $value) {
    print($value . "<br>");
}


$mas = array("Room1" => "Офис", "Room2" => "Склад", 55 => 100);
echo $mas["Room1"] . "<br>";
echo $mas ["Room2"] . "<br>";
echo $mas [55] . "<br>";
?>
