#!/bin/bash

#Список процессов
ps -aux > ps.out

#Отсортированный список процессов по имени пользователя-владельца
sort ps.out > sorted.ps

#Создание файла index.html
splitter='<hr noshade>'
body='<html><head><meta charset="utf-8"><title>Статистика процессов</title></head><body><h1>Распределение процессов по пользователям</h1><div class="row"><div class="col-12">'
footer='</div></div></body></html>'
echo $body > index.html

for CURRENT_USER in $(cat sorted.ps | awk '{print $1}' | uniq)
do

    #Процессы по пользователю
    cat sorted.ps | grep $CURRENT_USER > $CURRENT_USER.ps
    #Добавление тега <li>
    sed -e "s/$/<li> $/g" $CURRENT_USER.ps > $CURRENT_USER.html
    #Подсчет количества процессов
    PROC_COUNT=$(cat $CURRENT_USER.html | wc -l)
    echo "<p><b>Итого процессов: $PROC_COUNT</b></p>" > $CURRENT_USER.total
    #Добавляем данные в index.html
    echo $splitter $(cat $CURRENT_USER.total) "Пользователь $CURRENT_USER" $splitter $(cat $CURRENT_USER.html) >> index.html

done

echo $footer >> index.html
echo "Завершение работы скрипта"