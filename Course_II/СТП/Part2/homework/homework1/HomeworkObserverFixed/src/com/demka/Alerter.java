package com.demka;

//Инткерфейс, чтоб не забывать реализовывать метод alert
public interface Alerter {

    //Уведомление о событии
    void alert(StringBuilderObserver sb);

}
