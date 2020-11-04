package com.demka;


public class BinaryTreeClass {

    String key;
    BinaryTreeClass parent = null;
    BinaryTreeClass leftChild = null;
    BinaryTreeClass rightChild = null;

    public BinaryTreeClass(String key, BinaryTreeClass parent){
        this.key = key;
        this.parent = parent;
    }
    public BinaryTreeClass(String key){
        this.key = key;
    }

    //Вставка элемента слева
    public void InsertLeft(String key){

        //Если ничего нет слева
        if (this.leftChild == null) {
            this.leftChild = new BinaryTreeClass(key,this);
        }
        //Если у элемента что-то есть слева - перезаписываем
        else {
            BinaryTreeClass t = new BinaryTreeClass(key, this);
            t.leftChild = this.leftChild;
            this.leftChild = t;
        }
    }

    //Вставка элемента вправо
    public void InsertRight(String key){

        //Если ничего нет справа
        if (this.rightChild == null) {
            this.rightChild = new BinaryTreeClass(key,this);
        }
        //Если у элемента что-то есть справа - перезаписываем
        else {
            BinaryTreeClass t = new BinaryTreeClass(key, this);
            t.rightChild = this.rightChild;
            this.rightChild = t;
        }
    }

    //Получение родителя
    public BinaryTreeClass getParent() {
        return parent;
    }

    //Получение элемента справа
    public BinaryTreeClass getrightChild() {
        return rightChild;
    }
    //Получение элемента слева
    public BinaryTreeClass getleftChild() {
        return leftChild;
    }

    //Выставление значения
    public void setKey(String key) {
        this.key = key;
    }

    //Получение значения
    public String getKey() {
        return key;
    }
}
