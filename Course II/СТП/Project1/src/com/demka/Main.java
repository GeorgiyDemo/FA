package com.demka;

import java.util.*;
public class Main {

    /*
    Метод для рассчета гипотенузы по заданию №5
    На вход принимает 2 катета в double
     */
    public static double HypotenuseCalculator(double cathetus1, double cathetus2){
        return Math.sqrt( Math.pow(cathetus1, 2.0) + Math.pow(cathetus2, 2.0));
    }

    public static void main(String[] args) {
        //1. Вывести текст
        System.out.println("Hello world");

        //2. Создайте переменную, присвойте ей целочисленное значение. Выведите на экран
        int testVar = 42;
        System.out.println(testVar);

        //3. Создайте переменную, увеличьте ее несколькими способами и выведите её на экран
        int testVar1 = 1;
        System.out.println("Начальное значение: "+testVar1);
        testVar1++;
        System.out.println("Начальное значение +1: "+testVar1);
        testVar1 = testVar1 + 1;
        System.out.println("Начальное значение +1: "+testVar1);
        ++testVar1;
        System.out.println("Начальное значение +1: "+testVar1);

        //4. Даны две переменные. Поменяйте значения переменных друг с другом двумя способами
        int a = 5;
        int b = 2;
        System.out.println("\nA = "+a);
        System.out.println("B = "+b);

        int buffer = a;
        a = b;
        b = buffer;
        System.out.println("A = "+a);
        System.out.println("B = "+b);

        a=a+b-(b=a);
        System.out.println("A = "+a);
        System.out.println("B = "+b);

        a += b;
        b = a - b;
        a -= b;
        System.out.println("A = "+a);
        System.out.println("B = "+b);

        //5. Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами
        double side1 = 3.4;
        double side2 = 4.6;
        System.out.println(HypotenuseCalculator(side1, side2));
    }
}
