package com.demka;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Student student = new Student();
        ArrayList<String> person = student.setName();
        String result = student.setAge("5","4","3");
        System.out.println(result);
        System.out.println(person.toString());


    }
}
