//Работа с потоками в Java, 2 способа

package com.demka;

//Способ 1. Наследование от Thread
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


//Способ 2. С помощью Runable
class MyRunnable implements Runnable {
    public void run(){
        for (int i = 0; i < 100; i++) {
            try {
                System.out.println("MyRunnable running");
                Thread.sleep(250);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class Main {

    public static void main(String[] args) throws InterruptedException {
        Thread thread1 = new MyThread("1111",1000);
        Thread thread2 = new MyThread("2222",500);
        thread1.start();
        thread2.start();

        MyRunnable runnable = new MyRunnable();
        Thread thread3 = new Thread(runnable, "New Thread");

        thread3.start();
        System.out.println(thread3.getName());

        for (int i = 0; i < 100; i++) {
            System.out.println("ПРИВЕТ ОТ MAIN");
            Thread.sleep(500);
        }

    }
}
