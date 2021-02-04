package com.demka;
/*
Написать класс для работы с файлами.
По введенному пути файл или копируется в заданное место,
или вырезается и копируется в заданное место
 */

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.channels.FileChannel;

class FileClass {

    String filepath;

    public FileClass(String filepath) {
        this.filepath = filepath;

    }

    public void move(String location) {
        File file = new File(this.filepath);

        if (file.renameTo(new File(location))) {
            file.delete();
            System.out.println("Успешно переместили файл");
        } else {
            System.out.println("Не получилось переместить файл");
        }

    }


    public void copy(String location) throws IOException {

        File fileToCopy = new File(this.filepath);

        FileInputStream inputStream = new FileInputStream(fileToCopy);
        FileChannel inChannel = inputStream.getChannel();

        File newFile = new File(location);
        FileOutputStream outputStream = new FileOutputStream(newFile);
        FileChannel outChannel = outputStream.getChannel();

        inChannel.transferTo(0, fileToCopy.length(), outChannel);

        inputStream.close();
        outputStream.close();


    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        FileClass obj = new FileClass("./check.meow");
        obj.move("./meow/check.meow");

        FileClass obj1 = new FileClass("./meow/check.meow");
        obj1.copy("./meow/check3.meow");

    }
}
