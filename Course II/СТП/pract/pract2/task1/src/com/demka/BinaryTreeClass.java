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

    //Вставка элемента слева (строка)
    public void InsertLeft(String key){

        //Если ничего нет слева
        if (this.leftChild == null) {
            this.leftChild = new BinaryTreeClass(key,this);
        }
        //Если у элемента что-то есть слева - добавляем переданный, а старый закидываем влево переданного
        else {
            BinaryTreeClass obj = new BinaryTreeClass(key, this);
            obj.leftChild = this.leftChild;
            this.leftChild = obj;
        }
    }

    //Вставка элемента слева (объект BinaryTreeClass)
    public void InsertLeft(BinaryTreeClass obj){

        //Если ничего нет слева
        if (this.leftChild == null) {
            this.leftChild = obj;
        }
        //Если у элемента что-то есть слева - добавляем переданный, а старый закидываем влево переданного
        else {
            obj.leftChild = this.leftChild;
            this.leftChild = obj;
        }
    }

    //Вставка элемента вправо (строка)
    public void InsertRight(String key){

        //Если ничего нет справа
        if (this.rightChild == null) {
            this.rightChild = new BinaryTreeClass(key,this);
        }
        //Если у элемента что-то есть справа - добавляем переданный, а старый закидываем вправо переданного
        else {
            BinaryTreeClass obj = new BinaryTreeClass(key, this);
            obj.rightChild = this.rightChild;
            this.rightChild = obj;
        }
    }

    //Вставка элемента вправо (объект BinaryTreeClass)
    public void InsertRight(BinaryTreeClass obj){

        //Если ничего нет слева
        if (this.rightChild == null) {
            this.rightChild = obj;
        }
        //Если у элемента что-то есть справа - добавляем переданный, а старый закидываем вправо переданного
        else {
            obj.rightChild = this.rightChild;
            this.rightChild = obj;
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
