/*
3. Дано натуральное число N. Вычислите сумму его цифр. При решении этой задачи нельзя
использовать строки, списки, массивы (ну и циклы, разумеется).
Ввод: 234
Вывод: 9
*/
package com.company;

public class Main {
    public static int recursion(int n) {
        // Базовый случай
        if (n < 10) {
            return n;
        }// Шаг рекурсии / рекурсивное условие
        else {
            return n % 10 + recursion(n / 10);
        }
    }
    public static void main(String[] args) {
        System.out.println(recursion(234)); // вызов рекурсивной функции
    }
}