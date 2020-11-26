#!/bin/bash

#Список процессов
ps -aux > ps.out

#TODO ЦИКЛ ПО КАЖДОМУ ПОЛЬЗОВАТЕЛЮ

#Отсортированный список процессов по имени пользователя-владельца
sort ps.out > sorted.ps
cat sorted.ps | grep root > root.ps
cat sorted.ps | grep $(whoami) > user.ps

#Добавление тега <li>
sed -e "s/root/<li> root/g" root.ps > root.html
sed -e "s/$/<li> $/g" user.ps > user.html

#Подсчет колличества строк
echo "<p><b>Итого процессов: $(cat root.html | wc -l) </b></p>" > root.total
echo "<p><b>Итого процессов: $(cat user.html | wc -l) </b></p>" > user.total

#Создание файла index.html
splitter='<hr noshade>'
body='<html><head><meta charset="utf-8"><title>Статистика процессов</title></head><body><h1>Распределение процессов по пользователям</h1><div class="row"><div class="col-12">'
footer='</div></div></body></html>'
echo $body > index.html

#Создание файла index.html
echo $(cat index.html) $splitter $(cat root.total) "Пользователь root" $splitter $(cat root.html) $splitter $(cat user.total) "Пользователь" $(whoami) $splitter $(cat user.html) $footer > index.html

echo "Завершение работы скрипта"