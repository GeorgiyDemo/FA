#!/bin/bash
cd $(dirname "$0")

#	Расширенный список процессов
ps aux > ps.out

#	Отсортированный расширенный список процессов по имени пользователя-владельца
sort ps.out > sorted.ps
cat sorted.ps | grep root > root.ps
cat sorted.ps | grep $(whoami) > user.ps

#	Добавление тега <li>
sed -e "s/root/<li> root/g" root.ps > root.html
sed -e "s/$/<li> $/g" user.ps > user.html

#	Подсчет колличества строк
echo "<p><b>Итого процессов: $(cat root.html | wc -l) </b></p>" > root.total
echo "<p><b>Итого процессов: $(cat user.html | wc -l) </b></p>" > user.total

#	Создание файла index.html
noshade='<hr noshade>'
body='<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"><title>Статистика процессов</title></head><body><header><nav class="navbar navbar-light bg-light"><div class="container"><h1><a style="font-size:1.3rem" class="navbar-brand">Распределение процессов по пользователям</a></h1></div></nav></header><div class="container"><div class="row"><div class="col-12">'
footer='</div></div></div></body></html>'
echo $body > index.html

#	Создание файла
echo $(cat index.html) $noshade $(cat root.total) "Пользователь root" $noshade $(cat root.html) $noshade $(cat user.total) "Пользователь" $(whoami) $noshade $(cat user.html) $footer > index.html
