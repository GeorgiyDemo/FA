package com.demka;

import java.util.Scanner;
import java.util.Random;



class RecurserClass{

    /*
        1)	Дано натуральное число n. Выведите все числа от 1 до n.
     */
    public void task1(int n){
        System.out.println(n);
        n--;
        if (n == -1)
            return;
        else
            task1(n);
    }

}

class Searcher {
    /*
    2)	Напишите метод, который проверяет, входит ли в массив заданный элемент или нет.
        Используйте перебор и двоичный поиск для решения этой задачи.
        Сравните время выполнения обоих решений для больших массивов (например, 100000000 элементов).
    */

    int [] array;
    public Searcher(int [] array){
        this.array = array;
    }

    public boolean SimpleSearcher(int searchValue){
        for (int i = 0; i < array.length; i++) {

            if (array[i] == searchValue){
                return true;
            }
        }
        return false;
    }

    /*
    Рекурсивный бинарный поиск
     */
    public static int BinarySearch(int arr[], int firstElement, int lastElement, int elementToSearch) {

        // условие прекращения
        if (lastElement >= firstElement) {

            //Серединка
            int mid = firstElement + (lastElement - firstElement) / 2;

            // если средний элемент - целевой элемент, вернуть его индекс
            if (arr[mid] == elementToSearch)
                return mid;

            // если средний элемент больше целевого
            // вызываем метод рекурсивно по суженным данным
            if (arr[mid] > elementToSearch)
                return BinarySearch(arr, firstElement, mid - 1, elementToSearch);

            // также, вызываем метод рекурсивно по суженным данным
            return BinarySearch(arr, mid + 1, lastElement, elementToSearch);
        }

        return -1;
    }

}


public class Main {


    /*
    Стат генератор массивов
     */
    public static int [] generator(int n){

        int [] thisarr = new int[n];
        Random random = new Random();
        for (int i = 0; i < n; i++)
            thisarr[i] = random.nextInt(100);
        return thisarr;

    }

    /*
    Получение рандомного элемента в массиве
     */
    public static int getRandom(int[] array) {
        int rnd = new Random().nextInt(array.length);
        return array[rnd];
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

        Searcher obj2 = new Searcher(arr2);

        //Вычисляем время выполнения обыкновенного поиска
        long startTime = System.nanoTime();
        obj2.SimpleSearcher(randomValue);
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Время работы метода простого поиска: "+ duration);

        startTime = System.nanoTime();
        Searcher.BinarySearch(arr2,0,arrayLength,randomValue);
        endTime = System.nanoTime();
        duration = (endTime - startTime);
        System.out.println("Время работы метода бинарного поиска: "+ duration);

    }

}
