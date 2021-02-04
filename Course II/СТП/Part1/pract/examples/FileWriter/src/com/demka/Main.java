/*
Разработать класс, который создает новый файл, имя файла - текущая дата,
и записывает в файл каждые три секунды дату и время.
На вход подается время в секундах, сколько времени нужно выполнять запись
 */

package com.demka;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

class DemkaWriter {
    int AllSeconds;
    String filename;

    public DemkaWriter(int AllSeconds) {
        this.AllSeconds = AllSeconds;
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy.MM.dd");
        LocalDateTime now = LocalDateTime.now();
        this.filename = "./" + dtf.format(now) + ".txt";
        this.processing();
    }

    public String getFilename() {
        return filename;
    }

    void processing() {
        System.out.println("Открыли файл" + this.filename + " на запись");
        try (FileWriter writer = new FileWriter(this.filename, false)) {
            while (AllSeconds > 0) {
                DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
                LocalDateTime now = LocalDateTime.now();
                String buffer = dtf.format(now);
                writer.append(dtf.format(now) + "\n");
                System.out.println("Записали строчку " + buffer);
                AllSeconds = AllSeconds - 3;
                Thread.sleep(3000);
            }
            writer.flush();
        } catch (IOException | InterruptedException ex) {
            System.out.println(ex.getMessage());
        }
    }

}


class DemkaReader{
    String filename;

    public DemkaReader(String filename){
        this.filename = filename;
        System.out.println("Чтение из файла..");
        this.processing();
    }

    public void processing(){

        try {
            File myObj = new File(this.filename);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Ошибка, файла нет");
            e.printStackTrace();
        }

    }


}


public class Main {

    public static void main(String[] args) {
        DemkaWriter obj = new DemkaWriter(100);
        DemkaReader obj1 = new DemkaReader(obj.getFilename());
    }
}
