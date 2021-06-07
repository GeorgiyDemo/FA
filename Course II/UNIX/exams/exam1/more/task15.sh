#!/bin/bash
: '
Необходимо разработать сценарий, который будет запускать скрипт с
именем script13 каждые 13 секунд, но не более
одного одновременно запущенного процесса.
'

script_name="./script13.sh"

#Проверка на уже запущенный процесс, смотрим общее кол-во линий
lines_count=$(ps -aux | grep "sleep 13" | wc -l)

if (($lines_count == 2)) ; then
    echo "Процесс уже запущен" >&2
    exit 1
fi

while :
do
    echo $(date)
	echo "Выполняем скрипт $script_name" 
    $script_name
    echo "Ждем 13 сек."
	sleep 13
done