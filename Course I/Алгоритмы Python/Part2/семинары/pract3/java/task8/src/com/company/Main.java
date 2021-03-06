/*
8. Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом
0. Определите значение второго по величине элемента в этой последовательности, то есть
элемента, который будет наибольшим, если из последовательности удалить наибольший
элемент.
В этой задаче нельзя использовать глобальные переменные. Функция получает данные,
считывая их с клавиатуры, а не получая их в виде параметра. В программе функция
возвращает результат в виде кортежа из нескольких чисел и функция вообще не получает
никаких параметров.
Гарантируется, что последовательность содержит хотя бы два числа (кроме нуля)
*/

package com.company;

import java.util.Scanner;

public class Main {
    public static void recursion(int max1, int max2) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // Базовый случай
        if (n > 0) {
            // Шаг рекурсии / рекурсивное условие
            if (max1 < n) {
                recursion(n, max1);
            } // Шаг рекурсии / рекурсивное условие
            else if (max2 < n) {
                recursion(max1, n);
            } // Шаг рекурсии / рекурсивное условие
            else {
                recursion(max1, max2);
            }
        } else {
            System.out.println(max2);
        }
    }
    public static void main(String[] args) {
        recursion(0, 0); // вызов рекурсивной функции
    }
}
