package com.demka;

import java.util.ArrayList;
import java.util.List;


/*
Оповещалка-StringBuilder
 */
public class StringBuilderObserver {

    //Делегат данного StringBuilder
    private final StringBuilder stringBuilder;

    //Список для оповещения слушателей
    private final List<Alerter> channels = new ArrayList<Alerter>();

    //Название конкретного обсервера
    private final String name;

    public StringBuilderObserver(String name) {
        this.stringBuilder = new StringBuilder();
        this.name = name;
    }

    //Метод оповещения
    private void alert() {
        for (Alerter alerter : this.channels) alerter.alert(this);
    }

    //Добавление объекта-слушателя
    public void addObserver(Alerter alerter) {
        this.channels.add(alerter);
    }

    //Удаление объекта-слушателя
    public void removeObserver(Alerter alerter) {
        this.channels.remove(alerter);
    }

    public String getName() {
        return name;
    }

    /*
    Далее пошли дефолтные методы stringBuilder'а
     */

    //Добавление элемента
    public StringBuilderObserver append(String str) {
        stringBuilder.append(str);
        alert();
        return this;
    }

    //Замена
    public StringBuilderObserver replace(int start, int end, String str) {
        stringBuilder.replace(start, end, str);
        alert();
        return this;
    }

    //Реверс
    public StringBuilderObserver reverse() {
        stringBuilder.reverse();
        alert();
        return this;
    }

    @Override
    public String toString() {
        return stringBuilder.toString();
    }

}
