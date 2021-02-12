package com.demka;

/*
Интерфейс через который оповещаем в StringBuilderObserver
 */
public interface ObserverInterface {

    /*
    Оповещение в String о том, что было оповещение определенного StringBuilder
     */
    public void alert(String data);

    /*
    Добавление строки
     */
    public DEMKAStringBuilder append(String str);

    /*
    Удаление строки
     */
    public void undo();

}