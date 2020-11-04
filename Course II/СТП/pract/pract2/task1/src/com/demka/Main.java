package com.demka;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Main {


    /*
    Генератор массивов
     */
    public static int [] generator(int n){

        int [] thisarr = new int[n];
        Random random = new Random();
        for (int i = 0; i < n; i++)
            thisarr[i] = random.nextInt(100000);


        //Сортируем массив, чтоб бинарный поиск работал быстрее
        Arrays.sort(thisarr);
        return thisarr;

    }

    /*
    Взятие элемента с середины массива для усткорения бинарного поиска
     */
    public static int getRandom(int[] array) {

        int rnd = new Random().nextInt(array.length/10);
        int value = array.length/2+rnd;
        return array[value];
    }

    public static void main(String[] args) {
        System.out.println("Введите натуральное число n :");
        Scanner scanner = new Scanner(System.in);
        int number1 = scanner.nextInt();

        RecurserClass obj1 = new RecurserClass();
        obj1.task1(number1);

        int arrayLength = 100000000;
        //Получаем сгенерированный массив
        int [] arr2 = generator(arrayLength);
        int randomValue = getRandom(arr2);

        SearcherClass obj2 = new SearcherClass(arr2);

        System.out.println("Поиск числа "+randomValue);
        //Вычисляем время выполнения обыкновенного поиска
        long startTime = System.nanoTime();
        obj2.SimpleSearcher(randomValue);
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Время работы метода простого поиска: "+ duration);

        startTime = System.nanoTime();
        SearcherClass.BinarySearch(arr2, 0, arrayLength, randomValue);
        endTime = System.nanoTime();
        duration = (endTime - startTime);
        System.out.println("Время работы метода бинарного поиска: "+ duration);

        ExpSolverClass obj3 = new ExpSolverClass(0.0,10.0);
        System.out.println("Результат уравнения с 3 задания: "+obj3.getResult());

        BinaryTreeClass tree1Obj = new BinaryTreeClass("KOT");
        BinaryTreeClass tree2Obj = new BinaryTreeClass("КОТ ЛЕВЫЙ ОБЪЕКТ");
        tree1Obj.InsertLeft(tree2Obj);
        tree1Obj.InsertRight("КОТ ПРАВЫЙ СТРОКА");

    }

}
