#!/bin/bash

#Базовые переменные
code=0
ip=0
url=0
#Доп аргументы фильтрации
filter=0
filter_data=0

# Если не передали название файла
if [ $# -eq 0 ]
	then
		echo "Пожалуйста, укажите файл в аргументах скрипта"
		exit
fi

#Если вызывали с доп аргументами фильтрации
if [ "$#" = "3" ]; then
	file=$1
	filter=$2
	filter_data=$3

#Если вызвали без фильтрации
elif [ "$#" = "1" ]; then
	file=$1

#Если вызвали с несколькими аргументами
else
	echo "Некорректное кол-во аргументов"
	exit
fi

#Проверка на существование переданного файла
if [ -f "$file" ]; then
    echo "Файл $file существует"
else 
    echo "Файла $file не существует"
	exit
fi

#Дополнительне аргументы при вызове script
case "$filter" in	
	--code)
	code="$filter_data"
	shift;;

	--ip)
	ip="$filter_data"
	shift;;

	--url)
	url="$filter_data"
	shift;;
esac

#Парсинг данных с awk и вывод на экран
awk -v code="$code" -v ip="$ip" -v url="$url" '
{
if (substr($11,2,length($11) - 2) == "-") { 
request="Запрос выполнялся напрямую, а не по ссылке с другого сайта (поле реферер - пустое)"
} else {
request="Запрос выполнялся с " $11
}
check = 1
if (int(code) && int($9) != code) {
check = 0
}
if (ip != 0 && $1 != ip) {
check = 0
}
if (url != 0 && substr($11,2,length($11) - 2) != url) {
check = 0
}
if (check == 1) {
print substr($4,2) " " substr($5, 0, length($5) - 1) " с хоста " $1 " по протоколу " substr($8,1,length($8) - 1) " был выполнен запрос типа " substr($6,2) " для получения ресурса находящегося по ссылке " $7 ". Код ответа на запрос от сервера: " $9 ". Такой ответ не предполагает наличия тела ответа (количество переданных байт - " $10, "). " request ". Клиент использовал для обращения программу " substr($12,2) ", ОС клиента: " substr($13,2)
}
}' "$file"