/*
2. Дано натуральное число N. Выведите слово YES, если число N является точной степенью
двойки, или слово NO в противном случае. Операцией возведения в степень пользоваться
нельзя!
Ввод: 8
Вывод: Yes
Ввод: 3
Вывод: No
*/

package com.company;


public class Main {
    public static int recursion(double n) {
        // Базовый случай
        if (n == 1) {
            return 1;
        } // Базовый случай
        else if (n > 1 && n < 2) {
            return 0;
        } // Шаг рекурсии / рекурсивное условие
        else {
            return recursion(n / 2);
        }
    }

    public static void main(String[] args) {
        double n = 54;
        // вызов рекурсивной функции
        if (recursion(n) == 1) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
