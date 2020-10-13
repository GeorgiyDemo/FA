package com.demka;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.print("Введите температуру в градусах цельсия -> ");
        Scanner scanner = new Scanner(System.in);
        double inputValue = scanner.nextDouble();
        Fahrenheit obj = new Fahrenheit();
        System.out.println(obj.getTemp(inputValue));

	// write your code here
    }
}
