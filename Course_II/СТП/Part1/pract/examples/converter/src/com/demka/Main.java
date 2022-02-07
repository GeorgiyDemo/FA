package com.demka;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.print("Введите температуру в градусах цельсия -> ");
        Scanner scanner = new Scanner(System.in);
        double value = scanner.nextDouble();
        Converter obj = new Converter();

        double result = obj.Celsius2Fahrenheit(value);
        System.out.println("В градусах фаренгейта: "+result);

        double reverseResult = obj.Fahrenheit2Celsius(result);
        System.out.println("Обратный перевод с фаренгейтов с цельсий: "+reverseResult);

        double kelvinResult = obj.Celsius2Kelvin(reverseResult);
        System.out.println("Перевод с цельсия с кельвин: "+kelvinResult);

        double celsiusResult = obj.Kelvin2Celsius(kelvinResult);
        System.out.println("Обратный перевод с кельвина в цельсий: "+celsiusResult);


    }
}
