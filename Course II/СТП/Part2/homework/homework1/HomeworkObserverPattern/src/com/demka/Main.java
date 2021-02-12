/*
Написать класс StringBuilder с оповещением других объектов-слушателей об изменении своего состояния.
Делегировать стандартные методы стандартному StringBuilder. Паттерн «Наблюдатель»

Данное решение реализовывает классический Observer (не StringBuilder) StringBuilderObserver
и он хранит внутри себя надстройки над StringBuilder'ом, где можно делать возврат операции DEMKAStringBuilder.
Также для возможного масшитабирования используется ObserverInterface

Если нужна реализация именно по заданию выше, то смотрите в соседнюю директорию HomeworkObserverFixed
 */
package com.demka;

public class Main {

    public static void main(String[] args) {

        //Запускаем оповещатель
        StringBuilderObserver observer = new StringBuilderObserver();

        //Генерируем слушателей для оповещалки
        for (int i = 0; i < 10; i++) {
            DEMKAStringBuilder channel = new DEMKAStringBuilder("StringBuilder номер "+i);
            observer.addObserver(channel);
        }

        //Оповещение всех sb
        observer.alert("Какие-то данные для оповещения");

        //Добавление данных для всех
        observer.append("Какие-то данные для всех ОДИН");
        observer.append(", какие-то данные для всех ДВА");
        System.out.println(observer.toString());

        //Добавляем строку для 1 элемента
        observer.getChannels().get(0).append(", данные только для 0 элемента");
        System.out.println(observer.toString());

        //Удаляем последние добавленные элементы в sb
        observer.undo();
        System.out.println(observer.toString());

    }
}
