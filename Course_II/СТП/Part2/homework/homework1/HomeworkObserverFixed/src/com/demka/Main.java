/*
Написать класс StringBuilder с оповещением других объектов-слушателей об изменении своего состояния.
Делегировать стандартные методы стандартному StringBuilder. Паттерн «Наблюдатель»
 */
package com.demka;

public class Main {

    public static void main(String[] args) {

        //Создаем экземпляр оповещателя
        StringBuilderObserver observer = new StringBuilderObserver("оповещалка №1");

        //Создаем слушателей
        for (int i = 0; i < 3; i++) {
            Alerter listener = new Listener("слушатель №" + (i + 1));
            //Добавляем их оповещалке
            observer.addObserver(listener);
        }

        //Делаем изменение в оповещалке путем вызова методов, аналогичных StringBuilderовским
        observer.append("Произвольный текст");
        observer.reverse();
        observer.reverse();
        observer.replace(0,12,"ЗАМЕНЕННЫЙ");
    }
}
