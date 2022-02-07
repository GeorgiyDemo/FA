/*
Пропатченный StringBuilder с оповещателем
 */

package com.demka;
import java.util.Stack;

class DEMKAStringBuilder implements ObserverInterface {
    private interface Action {
        void undo();
    }

    //Делегат
    private StringBuilder stringBuilder;
    //Стек операций
    private Stack<Action> actions = new Stack<Action>();
    //Название конкретного sb
    private String name;

    public DEMKAStringBuilder(String name) {
        this.stringBuilder = new StringBuilder();
        this.name = name;
    }

    @Override
    public void alert(String data) {
        System.out.println("[Оповещение для "+this.name+"] -> "+data);
    }

    @Override
    public DEMKAStringBuilder append(String str) {
        stringBuilder.append(str);

        Action action = new Action() {
            public void undo() {
                stringBuilder.delete(
                        stringBuilder.length() - str.length() - 1,
                        stringBuilder.length());
            }
        };
        actions.add(action);
        return this;
    }

    @Override
    public void undo() {
        if (!actions.isEmpty()) {
            actions.pop().undo();
        }
    }

    @Override
    public String toString() {
        return "["+this.name+"] -> "+stringBuilder.toString();
    }
}
