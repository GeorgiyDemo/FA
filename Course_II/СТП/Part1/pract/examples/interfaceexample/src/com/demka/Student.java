package com.demka;

import java.util.ArrayList;
import java.util.Scanner;

public class Student implements Person{

    Scanner scanner;
    ArrayList <String> student;

    public Student(){
        this.student = new ArrayList<String>();
        scanner = new Scanner(System.in);
    }

    @Override
    public ArrayList setName(){
        System.out.println("Input student name ");
        String s = scanner.next();
        student.add(s);
        return student;
    }


    //Пример с большим кол-вом аргументов
    public String setAge(String ... student){

        String students = null;
        System.out.println(student);

        if (student.length == 2){

            student[0] = "23";
            student[1] = "66";
        }

        students = student[0] + student[1];

        return students;
    }


}
