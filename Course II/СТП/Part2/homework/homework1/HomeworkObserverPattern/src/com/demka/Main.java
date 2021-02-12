/*
Написать класс StringBuilder с оповещением других объектов-слушателей об изменении своего состояния.
Делегировать стандартные методы стандартному StringBuilder. Паттерн «Наблюдатель»
 */
package com.demka;

public class Main {

    public static void main(String[] args) {
        System.out.println("MEOW");

        StringBuilderObserver observer = new StringBuilderObserver();

        for (int i = 0; i < 10; i++) {
            StringBuilderChannel channel = new StringBuilderChannel();
            observer.addObserver(channel);
        }
        observer.setString("LOL");



    }
}
