package com.demka;

import java.util.Random;

class Vector {

    int x;
    int y;
    int z;

    //a. Конструктор
    public Vector(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public void value() {
        System.out.format("(%d, %d, %d)%n", x, y, z);
    }

    //b. Вычисление длины вектоа
    public double length() {
        return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2));
    }

    //c. Скалярное произведение
    public double DotProduct(Vector vector) {
        return x * vector.x + y * vector.y + z * vector.z;
    }

    //d. Векторное произведение с другим вектором
    public Vector CrossProduct(Vector vector) {
        int newX = y * vector.z - z * vector.y;
        int newY = z * vector.x - x * vector.z;
        int newZ = x * vector.y - y * vector.x;
        return new Vector(newX, newY, newZ);
    }

    //e. вычисляющий угол между векторами (или косинус угла)
    public double VectorCos(Vector vector) {
        //Скалярное произведение
        double dotproduct = DotProduct(vector);
        //Длина текущего вектора
        double length1 = length();
        //Длина другого вектора
        double length2 = vector.length();
        return dotproduct / (Math.abs(length2) * Math.abs(length1));
    }

    //f. 1. Сумма векторов
    public Vector summ(Vector vector) {
        return new Vector(x + vector.x, y + vector.y, z + vector.z);
    }

    //f. 2. Разность векторов
    public Vector difference(Vector vector) {
        return new Vector(x - vector.x, y - vector.y, z - vector.z);
    }

    //g.	статический метод, который принимает целое число N, и возвращает массив случайных векторов размером N
    public static Vector[] generator(int N) {
        Vector vectorsArr[];
        vectorsArr = new Vector[N];
        for (int i = 0; i < N; i++) {
            Random rand = new Random();
            // Generate random integers in range 0 to 999
            int randx = rand.nextInt(100);
            int randy = rand.nextInt(100);
            int randz = rand.nextInt(100);
            vectorsArr[i] = new Vector(randx, randy, randz);
        }

        return vectorsArr;
    }

}

public class Main {

    public static void main(String[] args) {

        //Случайные вектора из стат метода
        Vector[] vectors = Vector.generator(10);
        for (int i = 0; i < vectors.length; i++) {
            vectors[i].value();
        }

        //
        Vector vector1 = new Vector(2, 5, 5);
        Vector vector2 = new Vector(10, 25, 2);
        System.out.println("\nВектор 1");
        vector1.value();
        System.out.println("\nВектор 2");
        vector2.value();

        System.out.println("\nДлина вектора 1: " + vector1.length());
        System.out.println("Длина вектора 2: " + vector2.length());
        System.out.println("Скалярное произведение вектора 1 и 2: " + vector1.DotProduct(vector2));
        System.out.println("Векторное произведение вектора 1 и 2:");
        vector1.CrossProduct(vector2).value();

        System.out.println("Угол между векторами 1 и 2: " + vector1.VectorCos(vector2));
        System.out.println("Сумма векторов 1 и 2");
        vector1.summ(vector2).value();
        System.out.println("Разность векторов 1 и 2");
        vector1.difference(vector2).value();

    }
}
