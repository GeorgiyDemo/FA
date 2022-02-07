/*
9. Дана последовательность натуральных чисел (одно число в строке), завершающаяся двумя
числами 0 подряд. Определите, сколько раз в этой последовательности встречается число 1.
Числа, идущие после двух нулей, необходимо игнорировать.
В этой задаче нельзя использовать глобальные переменные и параметры, передаваемые в
функцию. Функция получает данные, считывая их с клавиатуры, а не получая их в виде
параметров.
*/

package com.company;

import java.util.Scanner;

public class Main {
    public static void check(){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.print(n);
        int m = in.nextInt();
        System.out.print(m);


    }
    public static int recursion() {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // Базовый случай
        if (n == 1) {
            int m = in.nextInt();
            // Базовый случай
            if (m == 1) {
                // Шаг рекурсии / рекурсивное условие
                return recursion() + n + m;
            } else {
                int k = in.nextInt();
                // Базовый случай
                if (k == 1) {
                    // Шаг рекурсии / рекурсивное условие
                    return recursion() + n + m + k;
                } else {
                    return n + m + k;
                }
            }
        } else {
            int m = in.nextInt();
            // Базовый случай
            if (m == 1) {
                // Шаг рекурсии / рекурсивное условие
                return recursion() + n + m;
            } else {
                return n + m;
            }
        }
    }

    public static void main(String[] args) {
        //check();

        System.out.println(recursion()); // вызов рекурсивной функции
    }
}
