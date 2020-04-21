/*
5. Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке,
разделяя их пробелами или новыми строками.
При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы,
разумеется). Разрешена только рекурсия и целочисленная арифметика.
 */
package com.company;

public class Main {
    public static int recursion(int n) {
        // Базовый случай
        if (n < 10) {
            return n;
        }// Шаг рекурсии / рекурсивное условие
        else {
            System.out.print(n % 10 + " ");
            return recursion(n / 10);
        }
    }
    public static void main(String[] args) {
        System.out.println(recursion(123)); // вызов рекурсивной функции
    }
}
