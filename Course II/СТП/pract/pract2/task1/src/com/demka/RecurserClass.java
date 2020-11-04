package com.demka;

public class RecurserClass{

    /*
        1)	Дано натуральное число n. Выведите все числа от 1 до n.
     */
    public void task1(int n){
        System.out.println(n);
        n--;
        if (n == -1)
            return;
        else
            task1(n);
    }

}