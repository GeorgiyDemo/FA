package com.demka;

import java.util.Stack;

/*
Пропатченный StringBuilder с оповещателем
 */
class DEMKAStringBuilder implements ObserverInterface {
    private interface Action {
        void undo();
    }

    private class DeleteAction implements Action {
        private int size;

        public DeleteAction(int size) {
            this.size = size;
        }

        public void undo() {
            stringBuilder.delete(
                    stringBuilder.length() - size, stringBuilder.length());
        }
    }

    private StringBuilder stringBuilder; // делегат

    private Stack<Action> actions = new Stack<Action>();

    // конструктор
    public DEMKAStringBuilder() {
        stringBuilder = new StringBuilder();
    }

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

    public void undo() {
        if (!actions.isEmpty()) {
            actions.pop().undo();
        }
    }

    @Override
    public String toString() {
        return stringBuilder.toString();
    }
}
