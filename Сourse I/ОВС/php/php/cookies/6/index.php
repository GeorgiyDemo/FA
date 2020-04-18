<?php  

	
    $now = date('d.m.Y');
    $nowArr = explode('.', $now);
    $monthNow = date('t', mktime(0, 0, 0, $nowArr[1], $nowArr[0], $nowArr[2]));
    $birthday = '23.03.1994';
    $arr = explode('.', $birthday);
    $monthBirthday = date('t', mktime(0, 0, 0, $arr[1], $arr[0], $arr[2])); 
    $rest = $monthBirthday - $arr[0];
    $days = 0;
 
    for($i = $nowArr[1]; $i <= 12; $i++) {
        $days = $days + date('t', mktime(0, 0, 0, $i, $nowArr[0], $nowArr[2])); 
        if($i == 12) {
            for($j = 1; $j <= $arr[1]; $j++)
                $days = $days + date('t', mktime(0, 0, 0, $j, $nowArr[0], $nowArr[2]));
        }
    }
 
    print($days - $nowArr[0] - $rest);