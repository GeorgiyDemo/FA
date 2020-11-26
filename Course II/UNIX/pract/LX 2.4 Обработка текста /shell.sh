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

#Создание файла index.html
echo $(cat index.html) $splitter $(cat root.total) "Пользователь root" $splitter $(cat root.html) $splitter $(cat user.total) "Пользователь" $(whoami) $splitter $(cat user.html) $footer > index.html

echo $footer >> index.html
echo "Завершение работы скрипта"