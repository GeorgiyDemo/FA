import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {
    public static boolean getRandomBoolean() {
        Random random = new Random();
        return random.nextBoolean();
    }

    public static void main(String[] args) {

        List<Worker> workers = new ArrayList<Worker>();

        for (int i = 0; i < 5; i++) {

            //Генерируем рандомную зарплату
            Random r = new Random();
            double randomSalary = 100 + (10000 - 100) * r.nextDouble();

            //Случайно выбираем между HourlyWorker и MonthlyWorker
            Worker worker = getRandomBoolean() ? new HourlyWorker(i, "Рабочий №1" + i, randomSalary) : new MonthlyWorker(i, "Рабочий №1" + i, randomSalary);

            //Добавляем рабочего в список
            workers.add(worker);
        }

        //Цикл по каждому элементу списка
        workers.forEach(worker -> {
            String string = null;
            try {
                string = worker.Serialize();
            } catch (JsonProcessingException e) {
                e.printStackTrace();
            }
            System.out.println(string);
        });

    }
}
