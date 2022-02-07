#!/bin/bash
: '
Написать скрипт, которые выведет на экран все файлы,
размер которых больше 50 Мб в директории /var/log
'

# Директория
path="/var/log"

find $path -type f -size +50M 2>/dev/null | while read line 
do
    echo $line
done

echo "Успешно выполнили скрипт"