/*
Деменчук Георгий ПИ19-4

24.	Создать класс для выведения в консоль изображения квадрата при помощи символа '+'. Координата [0,0] в верхнем левом углу. Вводятся пользователем сторона квадрата и сдвиг квадрата от начала координат. Пример вывода:

Квадрат со стороной 5 и координатами (0,0):
+ + + + +
+           +
+           +
+ + + + +

 */

package com.demka;

import java.util.Scanner;

/*
    Класс квадрата
    На вход:
    - lineInput - сторона квадрата
    - offsetInput - сдвиг квадрата
 */
class Square {

    int lineInput;
    int offsetInput;
    String[][] thisMatrix;

    public Square(int lineInput, int offsetInput) {
        this.lineInput = lineInput;
        this.offsetInput = offsetInput;
        this.generator();

    }

    /*
        Генератор данных матрицы
     */
    public void generator() {

        //Чтоб не было выхода из массива
        this.thisMatrix = new String[100][100];
        //Заполняем пробелами
        for (int i = 0; i < thisMatrix.length; i++) {
            for (int j = 0; j < thisMatrix[i].length; j++) {
                thisMatrix[i][j] = " ";
            }
        }
        //Заполняем плюсами
        for (int i = 0; i < lineInput; i++) {
            thisMatrix[i + offsetInput][offsetInput] = "+";
            thisMatrix[offsetInput][i + offsetInput] = "+";
            thisMatrix[lineInput - 1 + offsetInput][i + offsetInput] = "+";
            thisMatrix[i + offsetInput][lineInput - 1 + offsetInput] = "+";
        }


    }

    /*
    Отображение матрицы на экране
     */
    public void drawer() {
        System.out.println("Квадрат со стороной " + lineInput + " и сдвигом (" + offsetInput + "," + offsetInput + ")");
        for (int i = 0; i < lineInput + offsetInput; i++) {
            for (int j = 0; j < lineInput + offsetInput; j++) {
                System.out.print(thisMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }

}

public class Main {

    private static int lineInput;
    private static int offsetInput;

    public static void main(String[] args) {
        System.out.println("Введите длину стороны квадрата:");
        Scanner scanner = new Scanner(System.in);
        lineInput = scanner.nextInt();
        System.out.println("Введите длину сдвига:");
        offsetInput = scanner.nextInt();

        //Создаем экземпляр квадрата
        Square square = new Square(lineInput, offsetInput);

        //Выводим квадрат на экран
        square.drawer();

    }
}
