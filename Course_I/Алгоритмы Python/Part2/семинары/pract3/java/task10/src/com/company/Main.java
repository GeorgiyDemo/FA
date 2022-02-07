/*
10. Даны числа a и b. Определите, сколько существует последовательностей из a нулей и b
единиц, в которых никакие два нуля не стоят рядом
*/

package com.company;

public class Main {
    public static int recursion(int a, int b) {
        // Базовый случай
        if (a > b + 1) {
            return 0;
        }
        // Базовый случай
        if (a == 0 || b == 0) {
            return 1;
        }
        // Шаг рекурсии / рекурсивное условие
        return recursion(a, b - 1) + recursion(a - 1, b - 1);
    }
    public static void main(String[] args) {
        System.out.println(recursion(5, 8)); // вызов рекурсивной функции
    }
}
