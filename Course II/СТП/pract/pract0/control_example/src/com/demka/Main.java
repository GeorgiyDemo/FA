
/*
Реализовать класс Car и дочерние классы отдельных моделей автомобиля.
Все классы должны содержать атрибуты цвет, максимальная скорость, тип коробки передач, текущая скорость, цена;
методы start(), stop(), accelerate(int speed). Продумать атрибуты и/или методы для отдельных моделей автомобилей.

Защитить классы от изменения данных извне.
Реализуйте класс Garage, который в себе будет хранить экземпляры автомобилей.
Атрибуты – максимальная вместимость, какие автомобили и в каком количестве хранятся в гараже.
Реализуйте методы, которые выводят на консоль построчно автомобили и их количество, отсортированных по количеству в гараже,
отсортированных по цене автомобиля (если они есть в наличии)

 */
package com.demka;

/*
Класс автомобиля
 */
class Car {
    private String color;
    private double maxSpeed;
    //1 - механка, 0 - автомат
    private boolean shiftType;
    //Перемещение
    private boolean movement;
    private double currentSpeed;
    private double price;


    /*
        Разгон. Если машина движется, то к текущей скорости прибавляется указанная скорость.
     */
    private boolean accelerate(){

    }
    private boolean start(){
        if ((currentSpeed == 0.0) && (!movement)) {
            movement = true;
            currentSpeed = 0.1;
            return  true;
        }
        return false;
    }

    private boolean stop(){
        if ((currentSpeed != 0.0) && (movement)){
            movement = false;
            currentSpeed = 0.0;
            return true;
        }
        return false;
    }

}

/*
Класс гаража, где хранятся автомобили
 */
class Garage {

}


public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}
