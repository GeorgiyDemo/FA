package com.demka;

import java.util.ArrayList;
import java.util.List;

/*
Та штука, котрая оповещает всех о чем-либо
 */
class StringBuilderObserver {

    //Список для оповещения
    private List<ObserverInterface> channels = new ArrayList<>();


    //Добавление объекта-оповещателя
    public void addObserver(ObserverInterface channel) {
        this.channels.add(channel);
    }

    //Удаление объекта-оповещателя
    public void removeObserver(ObserverInterface channel) {
        this.channels.remove(channel);
    }

    //Метод для оповещения всех StringBuilderов
    public void alert(String someData) {
        for (ObserverInterface sb: this.channels) sb.alert(someData);
    }

    //Добавление во все StringBuilder'ы данных
    public void append(String someData){
        for (ObserverInterface sb: this.channels) sb.append(someData);
    }

    //Удаление последней операции во всех StringBuilderах
    public void undo(){
        for (ObserverInterface sb: this.channels) sb.undo();
    }

    //Получение списка слушателей
    public List<ObserverInterface> getChannels() {
        return channels;
    }

    @Override
    public String toString() {
        StringBuilder resultString = new StringBuilder();
        for (ObserverInterface sb: this.channels) {
            resultString.append(sb.toString()).append("\n");
        }
        return resultString.toString();
    }

}