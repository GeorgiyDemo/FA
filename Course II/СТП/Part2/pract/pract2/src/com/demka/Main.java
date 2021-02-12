/*
Реализовать класс обертку StringBuilder с поддержкой undo
Добавить и удалить
 */



package com.demka;

public class Main {
    public static void main(String[] strings) {
        DEMKAStringBuilder thisString = new DEMKAStringBuilder();
        thisString.append("РАЗ РАЗ РАЗ ");
        thisString.append("ДВА ДВА ДВА ");
        thisString.append("ТРИ ТРИ ТРИ ");

        System.out.println("Строка:"+thisString.toString());
        thisString.undo();
        thisString.undo();
        System.out.println("После отмены: "+thisString.toString());
    }
}