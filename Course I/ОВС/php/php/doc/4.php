<?php

    /*
    Ваше задание — создать массив, наполнить его случайными значениями
    (можно использовать функцию rand), найти максимальное и минимальное
    значение массива и поменять их местами.
    */

        $a = array();
        $arrmaxlength = 15;
        print("Исходный массив:<br>");
        for($i = 0; $i < $arrmaxlength; $i++)
        {
            $a[$i] = rand(1, 100);
            print($a[$i])." ";
        }
        
        $min = $a[0]; $index_min = 0;
        $max = $a[0]; $index_max = 0;
    
        for($i = 1; $i < $arrmaxlength; $i++) {    
            if($min > $a[$i]) {
                $min = $a[$i];
                $index_min = $i;
            }
    
            if($max < $a[$i]) {
                $max = $a[$i];
                $index_max = $i;
            }
        }
    
        $a[$index_min] = $max;
        $a[$index_max] = $min;
        print("<br>Преобразованный массив:<br>");
        for($i = 0; $i < $arrmaxlength; $i++)
            print($a[$i])." ";
        print('<br>Min: ' . $min . ', Max: ' . $max."<br>");
    
?>