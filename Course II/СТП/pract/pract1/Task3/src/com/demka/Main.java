/*
3)	Реализовать иерархию классов, описывающие трехмерные фигуры (Рисунок 1)
Класс Box является контейнером, он можем содержать в себе другие фигуры. Метод add() принимает на вход Shape.
Нужно добавлять новые фигуры до тех пор, пока для них хватаем места в Box
(будем считать только объём, игнорируя форму. Допустим, мы переливаем жидкость).
Если места для добавления новой фигуры не хватает, то метод должен вернуть false.
*/

package com.demka;

class Shape {
    double volume;

    public double getVolume() {
        return volume;
    }
}

class Pyramid extends Shape {
    double s;
    double h;

}


/*
TODO Класс Box является контейнером,
 Нужно добавлять новые фигуры до тех пор, пока для них хватаем места в Box
 (будем считать только объём, игнорируя форму. Допустим, мы переливаем жидкость).
 Если места для добавления новой фигуры не хватает, то метод должен вернуть false.
 */
class Box extends Shape {

    void Box(double value) {
        System.out.println("Метод Box");
    }

    public boolean add(Shape shape) {
        return false;
    }
}

class SolidOfRevolution extends Shape {
    double radius;

    public double getRadius() {
        return radius;
    }

}

class Cylinder extends SolidOfRevolution {
    double height;


}

class Ball extends SolidOfRevolution {

}


public class Main {

    public static void main(String[] args) {
        // write your code here
    }
}
