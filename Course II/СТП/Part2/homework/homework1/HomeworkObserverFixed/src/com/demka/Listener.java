package com.demka;

//Слушатель обсервера
public class Listener implements Alerter {

    //Название слушателя
    private final String name;

    public Listener(String name) {
        this.name = name;
    }

    @Override
    public void alert(StringBuilderObserver sb) {
        System.out.println("[Изменение от " + sb.getName() + " для " + this.name + "] Значение StringBuilder \"" + sb.toString() + "\"");
    }
}
