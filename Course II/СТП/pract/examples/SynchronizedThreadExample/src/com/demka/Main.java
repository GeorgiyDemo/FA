package com.demka;

class MyThreadMy implements Runnable{
    Thread thrd;
    static  SumArray sa = new SumArray();
    int a[];
    int answer;

    public MyThreadMy(String name, int nums[]){
        thrd = new Thread(this, name);
        a = nums;
        thrd.start();
    }

    @Override
    public void run(){
        int sum;
        System.out.println(thrd.getName() + "- запуск");
        answer = sa.sumArray(this.a);
        System.out.println("СУММА для "+thrd.getName()+": "+answer);
        System.out.println(thrd.getName()+" - завершение");

    }

}
class SumArray {
    private int sum;
    //Метод sumArray синхронизирован
    synchronized int sumArray(int nums[]){
        //Обнуление суммы
        sum = 0;
        for (int i=0; i<nums.length;i++)
            sum += nums[i];

        System.out.println("Текущее значение cуммы для " + Thread.currentThread().getName() + ": "+ sum);
        try {
            Thread.sleep(10); //разрешаем переключение задач
        } catch (InterruptedException exc){
            System.out.println("Прерывание основного потока");
        }

        return sum;
    }
}
public class Main {

    public static void main(String[] args) {
        int a[] = {1,2,3,4,5};
        MyThreadMy mt1 = new MyThreadMy("Child 1", a);
        MyThreadMy mt2 = new MyThreadMy("Child 2", a);
    }
}
