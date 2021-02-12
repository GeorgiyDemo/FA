#!/bin/bash
: '
Написать скрипт, который в качестве первого параметра принимает
команду, которую нужно выполнить, а в качестве
остальных имена пользователей, от
имени которых она должна быть выполнена.
Скрипт должен выполнить команду по очереди от имени каждого пользователя.
'
#Проверяем, чтоб скрипт закпускался от root
current_user=$(whoami)

if [ "$current_user" = "root" ]; then

    #Команда, которую надо выполнить
    command=$1

    n=0
    #Цикл по каждому аргументу
    for arg do 

        #Если это не 1 аргумент
        if [ $n -ne 0 ]; then
            echo "Выполнили команду $command от имени $arg"
            runuser -l $arg -c $command
        fi

        #+1
        n=$((n+1))
    done
else
    echo "Этот скрипт надо запускать от root" >&2
    exit 1
fi