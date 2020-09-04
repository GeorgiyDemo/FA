package com.demka;

public class Main {

    public static double pointerCalc(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    public static double geometricMean(int value1, int value2) {
        return Math.sqrt(value1 * value2);
    }

    public static double arithmeticMean(int value1, int value2) {
        return (value1 + value2) / 2;
    }

    public static int subtracter(int number) {
        return number - 21;
    }

    public static double HypotenuseCalculator(double cathetus1, double cathetus2) {
        return Math.sqrt(Math.pow(cathetus1, 2.0) + Math.pow(cathetus2, 2.0));
    }

    public static void main(String[] args) {
        //1. Вывести текст
        System.out.println("Hello world");

        //2. Создайте переменную, присвойте ей целочисленное значение. Выведите на экран
        int testVar = 42;
        System.out.println(testVar);

        //3. Создайте переменную, увеличьте ее несколькими способами и выведите её на экран
        int testVar1 = 1;
        System.out.println("Начальное значение: "+testVar1);
        testVar1++;
        System.out.println("Начальное значение +1: "+testVar1);
        testVar1 = testVar1 + 1;
        System.out.println("Начальное значение +1: "+testVar1);
        ++testVar1;
        System.out.println("Начальное значение +1: "+testVar1);

        //4. Даны две переменные. Поменяйте значения переменных друг с другом двумя способами
        int a = 5;
        int b = 2;
        System.out.println("\nA = "+a);
        System.out.println("B = "+b);

        int buffer = a;
        a = b;
        b = buffer;
        System.out.println("A = "+a);
        System.out.println("B = "+b);

        a=a+b-(b=a);
        System.out.println("A = "+a);
        System.out.println("B = "+b);

        a += b;
        b = a - b;
        a -= b;
        System.out.println("A = "+a);
        System.out.println("B = "+b);

        //5. Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами
        double side1 = 3.4;
        double side2 = 4.6;
        System.out.println(HypotenuseCalculator(side1, side2));

        //6. Дано натуральное число. Выведите его последнюю цифру.
        int value = 1003;
        String valueStr = String.valueOf(value);
        System.out.println(valueStr.charAt(valueStr.length()-1));

        //7. Дано неотрицательное целое число. Найдите число десятков в его десятичной записи
        // (т.е. вторую справа цифру его десятичной записи
        int mainValue = 255026;
        if (mainValue > 0)
            System.out.println(mainValue % 100 / 10);
        else
            System.out.println("Значение не отрицательно");

        //8. Дано двухзначное число. Найдите число десятков в нем
        int value8 = 51;
        System.out.println(value8 / 10);

        //9. Реализуйте метод, который получает целое число на вход и возвращает разницу между данным числом и 21
        //Выведите значения на экран с различными целыми числами
        System.out.println(subtracter(50));
        System.out.println(subtracter(24));
        System.out.println(subtracter(21));

        //10. Реализуйте метод, в который передаётся две целочисленные переменные
        // и возврвщает их среднее арифметическое
        System.out.println(arithmeticMean(4, 5));
        System.out.println(arithmeticMean(8, 10));
        System.out.println(arithmeticMean(3, 2));

        //11. Реализуйте метод, в который передаётся две целочисленные переменные
        // и возврвщает их среднее геометрическое
        System.out.println(geometricMean(3, 4));
        System.out.println(geometricMean(2, 45));
        System.out.println(geometricMean(5, 1));

        //12. Реализуйте метод, в который передаётся 4 числа с плавающей точкой.
        // Первые два числа - координаты x, y первой точки
        // Вторые два числа - координаты x, y второй точки. Найдите расстояние между двумя точками
        double result = pointerCalc(3.434, 5.533, 10.5356, 6.30240);
        System.out.println("\nРасстояние между двумя точками: " + result);

    }
}
