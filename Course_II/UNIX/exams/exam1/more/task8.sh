#!/bin/bash
: '
Написать скрипт, который принимает в качестве аргумента
количество минут и название директории и удаляет
все файлы из данной директории,
созданные раньше указанного количества минут.
'

# Если кол-во переданных параметров не 2
if [[ $(($#)) -ne 2 ]] ; then
    echo "Ошибка: Некорректное кол-во переданных аргументов" >&2
    exit 1
fi

current_dir=$(pwd)

minutes_count=$1
dir_path=$2

# Если директория есть
if [ -d "$dir_path" ] 
then
    echo "Директория $dir_path существует"
# Если ее нет
else
    echo "Директории $dir_path НЕ существует"  >&2
    exit 1
fi

# Переходим в директорию
cd $dir_path

find . -type f -cmin -$minutes_count -print | while read line 
do
    echo "Удалили файл $line"
    rm -f $line
done 

cd $current_dir