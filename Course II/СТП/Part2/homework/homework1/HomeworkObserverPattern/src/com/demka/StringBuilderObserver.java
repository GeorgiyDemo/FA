package com.demka;


import java.nio.channels.Channel;
import java.util.ArrayList;
import java.util.List;

class StringBuilderObserver {

    private String news;
    //Список для оповещения
    private List<ObserverInterface> channels = new ArrayList<>();

    /*
    Добавление объекта-оповещателя
     */
    public void addObserver(ObserverInterface channel) {
        this.channels.add(channel);
    }

    /*
    Удаление объекта-оповещателя
     */
    public void removeObserver(ObserverInterface channel) {
        this.channels.remove(channel);
    }

    /*
    Метод для оповещения всех StringBuilderов
     */
    public void setString(String news) {
        for (ObserverInterface sb : this.channels) {
            sb.alert(this.news);
        }
    }

    @Override
    public void alert(Object o) {
        for (int i = 0; i < this.channels.size(); i++) {


        }
    }
}