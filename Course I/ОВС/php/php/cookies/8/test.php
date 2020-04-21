
    <?php 

        if (!isset($_COOKIE['numbers']))
        {
            header("Location: http://127.0.0.1:8888/SITE/php/cookies/8/index.php");
            exit;
        }

        else
        {
            $ug = 0;
            $numbers = explode(',', $_COOKIE['numbers']);

            $random = array(rand(1, 5), 
                rand(6, 11), 
                rand(12, 17), 
                rand(18, 23),
                rand(24, 29),
                rand(30, 36));

            if(sizeof($numbers) >= 6)
            {
                for ($i = 0; $i < sizeof($numbers); $i++)
                    if ((integer)$numbers[$i] > 36 && (integer)$numbers[$i] < 1)
                    {
                        print("Числа не соотвуют правилам ( 1 >= n <= 36)");
                        return;
                    }
                print("<b>Ваши числа: </b>".$numbers[0]);
                for ($i = 1; $i < sizeof($numbers); $i++)
                    print(", ".$numbers[$i]);
                
                print("<br><br><b>Результат:</b><br>");
                for ($i = 0; $i < sizeof($numbers); $i++)
                {
                    print("Число ".$random[$i]."<br>");
                    for ($j = 0; $j < sizeof($random); $j++)
                        if ($numbers[$j] == $random[$i])
                            $ug++;
                }
                print("<br><b>Вы угадали ".$ug." числа/чисел</b>");
            }
            else 
                print("Количество чисел не соответствует правилам");
            
            print("<br><a href='index.php'>Загадать другие числа</a>");
        }
    ?>