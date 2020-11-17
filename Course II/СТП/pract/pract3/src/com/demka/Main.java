//Работа с потоками в Java

package com.demka;

//Наследование от Thread
class MyThread extends Thread {

    String value;
    int delay;

    public MyThread(String value, int delay){
        this.value = value;
        this.delay = delay;

    }
    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            try {
                Thread.sleep(delay);
                System.out.println(this.value);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }

    }
}




//С помощью Runable

public class Main {

    public static void main(String[] args) throws InterruptedException {
        Thread thread1 = new MyThread("1111",1000);
        Thread thread2 = new MyThread("2222",500);
        thread1.start();
        thread2.start();

        for (int i = 0; i < 100; i++) {
            System.out.println("ПРИВЕТ ОТ MAIN");
            Thread.sleep(500);
        }

    }
}
