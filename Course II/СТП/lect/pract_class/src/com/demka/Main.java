package com.demka;

import java.util.Random;

/*
Класс матрицы
 */
class Matrix {

    int n;
    int m;
    int[][] thisMatrix;

    /*
    Конструктор
     */
    public Matrix(int n, int m) {
        this.thisMatrix = new int[n][m];
        this.n = n;
        this.m = m;
        this.initiliser();

    }

    /*
    Инициализация матрицы
     */
    private void initiliser() {

        Random random = new Random();
        for (int i = 0; i < thisMatrix.length; i++) {
            for (int j = 0; j < thisMatrix[i].length; j++) {
                thisMatrix[i][j] = random.nextInt(100);
            }
        }
    }

    /*
    Вывод матрицы на экран
     */
    public void getvalue() {
        System.out.println("\nИсходная матрица: ");
        for (int i = 0; i < thisMatrix.length; i++) {
            for (int j = 0; j < thisMatrix[i].length; j++) {
                System.out.print(thisMatrix[i][j] + " ");
            }
            System.out.print("\n");
        }
    }

    /* TODO
    Умножение матрицы на число
     */

}

/* TODO Возвращаем экземпляр матрицы
Операции с несколькими матрицами
 */
class MatrixExecuter {

    Matrix matrix1;
    Matrix matrix2;

    public MatrixExecuter(Matrix obj1, Matrix obj2) {
        this.matrix1 = obj1;
        this.matrix2 = obj2;
    }

    public void summ() {

        System.out.println("\nСумма матриц:");
        if ((matrix1.n != matrix2.n) || (matrix1.m != matrix2.m)) {
            System.out.println("Неправильная размерность матрицы");
        } else {
            for (int i = 0; i < matrix1.n; i++) {
                for (int j = 0; j < matrix1.m; j++) {
                    int result = matrix1.thisMatrix[i][j] + matrix2.thisMatrix[i][j];
                    System.out.print(result + " ");
                }
                System.out.print("\n");
            }
        }
    }
}


public class Main {

    public static void main(String[] args) {

        Matrix obj1 = new Matrix(3, 5);
        Matrix obj2 = new Matrix(3, 5);
        obj1.getvalue();
        obj2.getvalue();

        //Сумма матриц
        MatrixExecuter executerObj = new MatrixExecuter(obj1, obj2);
        executerObj.summ();

        //Матрица на число
    }
}
