/*
1. Дано натуральное число n. Выведите все числа от 1 до n.
Ввод: 5
Вывод 1 2 3 4 5
*/
package com.company;
import java.util.Scanner;

public class Main {

        public static String recursion(int n) {
            // Базовый случай
            if (n == 1) {
                return "1";
            }
            // Шаг рекурсии / рекурсивное условие
            return recursion(n - 1) + " " + n;
        }
        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            System.out.print("Введите число: ");
            int num = in.nextInt();

            System.out.println(recursion(num)); // вызов рекурсивной функции
        }
    }
