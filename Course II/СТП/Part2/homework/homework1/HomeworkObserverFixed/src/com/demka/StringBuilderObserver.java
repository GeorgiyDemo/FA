package com.demka;

import java.util.ArrayList;
import java.util.List;


public class StringBuilderObserver {
    //Делегат данного StringBuilder
    private StringBuilder stringBuilder;

    //Список для оповещения
    private List<StringBuilder> channels = new ArrayList<StringBuilder>();

    //Инициализация StringBuilder
    public StringBuilderObserver() {
        this.stringBuilder = new StringBuilder();
    }

    //Добавление элемента
    public StringBuilderObserver append(String str) {
        stringBuilder.append(str);
        return this;
    }

    //Добавление объекта-оповещателя
    public void addObserver(StringBuilder sb) {
        this.channels.add(sb);
    }

    //Удаление объекта-оповещателя
    public void removeObserver(StringBuilder sb) {
        this.channels.remove(sb);
    }

}
