<?php 

    /*
    Составить программу, которая бы по заданному числу выводила его название по китайском календаре.
    Заданное число не может быть меньше 1924
    */

    $year = $_POST['year'];
    $year = $year - 1924;
    $year = $year%12;

    switch ($year) {
        case 0:
            echo "Год крысы"; break;
        case 1:
            echo "Год быка"; break;
        case 2:
            echo "Год тигра"; break;
        case 3:
            echo "Год кота"; break;
            case 4:
            echo "Год дракона"; break;
            case 5:
            echo "Год змеи"; break;
            case 6:
            echo "Год лошади"; break;
            case 7:
            echo "Год козы"; break;
            case 8:
            echo "Год обезьяны"; break; 
            case 9:
            echo "Год петуха"; break;
            case 10:
            echo "Год собаки"; break;
            case 11: 
            echo "Год свиньи"; break;
            default: echo "Неправильно введен год";
    }

?>