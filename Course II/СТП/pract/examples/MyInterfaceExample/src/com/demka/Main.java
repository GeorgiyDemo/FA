/*Определить интерфейс Container с методами sort() и поэлементной обработки foreach().
Реализовать интерфейс в классах Bubble (сортировка пузырьком и извлечение квадратного корня)
Choice (сортировка методом выбора и обработка – вычисление логарифма).
 */

package com.demka;


import java.util.Arrays;
import java.util.Random;

class Bubble implements Container{

    double [] array;

    public Bubble(double [] array){
        this.array = array;
    }

    @Override
    //сортировка пузырьком
    public double[] sort() {
        boolean BooleanFlag = false;
        double buf;

        while(!BooleanFlag) {
            BooleanFlag = true;

            for (int i = 0; i < array.length-1; i++) {

                if(array[i] > array[i+1]){

                    BooleanFlag = false;
                    buf = array[i];
                    array[i] = array[i+1];
                    array[i+1] = buf;
                }
            }
        }
        return  array;
    }

    @Override
    //состоит в извлечении квадратного корня
    public double[] foreach() {
        for (int i = 0; i < array.length; i++)
            array[i] = Math.sqrt(array[i]);
        return  array;
    }
}


class Choise implements Container{


    double [] array;

    public Choise(double [] array){
        this.array = array;
    }

    @Override
    //сортировка методом выбора
    public double[] sort() {
        return  array;
    }

    @Override
    //вычисление логарифма
    public double[] foreach() {
        return  array;

    }

}
public class Main {

    public static void printer(double[] array){
        for (int i = 0; i < array.length; i++)
            System.out.print(array[i] + " ");
        System.out.println();
    }

    public static double[] ArrayGenerator(int range){
        double [] array = new double[range];
        Random rand = new Random();
        for (int i = 0; i < array.length; i++) {
            array[i] = rand.nextDouble()*100;
        }
        return array;

    }
    public static void main(String[] args) {
        double [] array = ArrayGenerator(10);
        System.out.println("Исходный массив:");
        printer(array);
        Container obj1 = new Bubble(array);
        System.out.println("Массив после сортировки пузырьком:");
        printer(obj1.sort());
        System.out.println("Массив после извлечения квадратного корня из каждого элемента:");
        printer(obj1.foreach());

        Container obj2 = new Choise(array);
    }
}
