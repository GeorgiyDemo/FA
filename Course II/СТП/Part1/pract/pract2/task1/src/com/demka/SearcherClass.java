package com.demka;

public class SearcherClass {

    /*
    2)	Напишите метод, который проверяет, входит ли в массив заданный элемент или нет.
        Используйте перебор и двоичный поиск для решения этой задачи.
        Сравните время выполнения обоих решений для больших массивов (например, 100000000 элементов).
    */

    int [] array;
    public SearcherClass(int [] array){
        this.array = array;
    }

    public boolean SimpleSearcher(int searchValue){
        for (int i = 0; i < array.length; i++) {

            if (array[i] == searchValue)
                return true;

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