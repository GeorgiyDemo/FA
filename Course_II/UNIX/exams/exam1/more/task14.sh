#!/bin/bash
: '
Написать скрипт, который выдает список разделов жесткого диска,
на которых свободной памяти осталось менее 100 Мб в
формате name|free memory
'

#Цикл по каждому разделу
df -m | awk ' { print $6, $4 }' | while read line 
do

    #Свободная память для раздела
    free_memory=$(echo $line | awk ' { print $2 }')
    
    #Если памяти меньше 100, то отображаем
    if (( $free_memory < 100 )); then
        echo "$line Mb"
    fi
done 
