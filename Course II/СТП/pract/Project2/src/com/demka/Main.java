package com.demka;

import java.util.Random;

/*
Класс матрицы
 */
class Matrix {

    int n;
    int m;
    double[][] thisMatrix;

    //Конструктор по дефолту
    public Matrix(int n, int m) {
        this.thisMatrix = new double[n][m];
        this.n = n;
        this.m = m;
        this.initiliser();

    }

    //Констуктор при передаче готовой матрицы
    public Matrix(double[][] thisMatrix) {
        this.thisMatrix = thisMatrix;
        this.n = thisMatrix.length;
        this.m = thisMatrix[0].length;
    }

    //Инициализация матрицы
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
                System.out.printf("%.3f  ",thisMatrix[i][j]);
            }
            System.out.print("\n");
        }
    }


    public Matrix numberMultiplication(double inputNumber){
        double[][] resultMatrix = new double[this.n][this.m];

        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.m; j++) {
                double result = this.thisMatrix[i][j] * inputNumber;
                resultMatrix[i][j] = result;
            }
        }
        return new Matrix(resultMatrix);
    }

    /* TODO Умножение матрицы на число
    TODO d.	Транспонированная матрица.
    TODO e.	Возведение матрицы в степень.
     */

}

/*
Операции с несколькими матрицами
 */
class MatrixExecuter {

    //TODO c.	Произведение двух матриц.
    Matrix matrix1;
    Matrix matrix2;

    public MatrixExecuter(Matrix obj1, Matrix obj2) {
        this.matrix1 = obj1;
        this.matrix2 = obj2;
    }

    //Сумма
    public Matrix summ() {
        if ((matrix1.n != matrix2.n) || (matrix1.m != matrix2.m)) {
            System.out.println("Неправильная размерность матрицы");
            return null;
        } else {

            double[][] resultMatrix = new double[matrix1.n][matrix1.m];

            for (int i = 0; i < matrix1.n; i++) {
                for (int j = 0; j < matrix1.m; j++) {
                    double result = matrix1.thisMatrix[i][j] + matrix2.thisMatrix[i][j];
                    resultMatrix[i][j] = result;
                }
            }
            return new Matrix(resultMatrix);
        }
    }

    //Разность
    public Matrix difference() {
        if ((matrix1.n != matrix2.n) || (matrix1.m != matrix2.m)) {
            System.out.println("Неправильная размерность матрицы");
            return null;
        } else {

            double[][] resultMatrix = new double[matrix1.n][matrix1.m];

            for (int i = 0; i < matrix1.n; i++) {
                for (int j = 0; j < matrix1.m; j++) {
                    double result = matrix1.thisMatrix[i][j] - matrix2.thisMatrix[i][j];
                    resultMatrix[i][j] = result;
                }
            }

            return new Matrix(resultMatrix);
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

        double multiNumber = 4.2;
        System.out.println("\nУмножение матрицы А на число "+multiNumber);
        Matrix matrixResult = obj1.numberMultiplication(multiNumber);
        matrixResult.getvalue();


        //Сумма матриц
        MatrixExecuter executerObj = new MatrixExecuter(obj1, obj2);
        System.out.println("\nСумма:");
        Matrix result = executerObj.summ();
        result.getvalue();

        //Разность
        System.out.println("\nРазность:");
        result = executerObj.difference();
        result.getvalue();


    }
}
