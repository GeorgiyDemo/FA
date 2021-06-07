#!/bin/bash
: '
Необходимо перенести файлы, имеющие расширения html и htm,
из каталога data в каталог tabs. 
'

#Текущий каталог
current_path=$(pwd)

#Переход в папку data
cd data

#Перемещение всех файлов
mv *htm ../tabs 2>/dev/null
mv *html ../tabs 2>/dev/null

#Переход к начальному пути, откуда запускали скрипт
cd $current_path
