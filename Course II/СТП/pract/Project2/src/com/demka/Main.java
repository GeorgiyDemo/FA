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
    Конструктор по дефолту
     */
    public Matrix(int n, int m) {
        this.thisMatrix = new int[n][m];
        this.n = n;
        this.m = m;
        this.initiliser();

    }

    /*
    Констуктор при передаче готовой матрицы
     */
    public Matrix(int [][] thisMatrix)
    {
        this.thisMatrix = thisMatrix;
        this.n = thisMatrix.length;
        this.m  = thisMatrix[0].length;
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
    /*
    a.	Сложение и вычитание матриц.
    b.	Умножение матрицы на число.
    c.	Произведение двух матриц.
    d.	Транспонированная матрица.
    e.	Возведение матрицы в степень.
     */


}

/*
Операции с несколькими матрицами
 */
class MatrixExecuter {

    Matrix matrix1;
    Matrix matrix2;

    public MatrixExecuter(Matrix obj1, Matrix obj2) {
        this.matrix1 = obj1;
        this.matrix2 = obj2;
    }

    public Matrix summ() {
        if ((matrix1.n != matrix2.n) || (matrix1.m != matrix2.m)) {
            System.out.println("Неправильная размерность матрицы");
            return null;
        } else {

            int[][] resultMatrix = new int[matrix1.n][matrix1.m];

            for (int i = 0; i < matrix1.n; i++) {
                for (int j = 0; j < matrix1.m; j++) {
                    int result = matrix1.thisMatrix[i][j] + matrix2.thisMatrix[i][j];
                    resultMatrix[i][j] = result;
                }
            }

            Matrix obj = new Matrix(resultMatrix);
            return obj;
        }
    }
}


public class Main {

    public static void main(String[] args) {

        Matrix obj1 = new Matrix(3, 5);
        Matrix obj2 = new Matrix(3, 5);
        System.out.println("Матрица А:");
        obj1.getvalue();
        System.out.println("\nМатрица B:");
        obj2.getvalue();

        //Сумма матриц
        MatrixExecuter executerObj = new MatrixExecuter(obj1, obj2);
        System.out.println("\nРезультат:");
        Matrix result = executerObj.summ();
        result.getvalue();

        //Матрица на число

    }
}
