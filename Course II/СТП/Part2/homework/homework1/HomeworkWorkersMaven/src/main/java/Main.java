import java.io.File;
import java.io.IOException;
import java.util.*;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {


    private static FileProcessing fileprocessing;
    private static final String filename = "./dump.json";

    private static boolean getRandomBoolean() {
        Random random = new Random();
        return random.nextBoolean();
    }

    private static List<Worker> generator() throws IOException {

        List<Worker> workers = new ArrayList<Worker>();
        for (int i = 0; i < 5000; i++) {

            //Генерируем рандомную зарплату
            Random r = new Random();
            double randomSalary = 100 + (10000 - 100) * r.nextDouble();

            //Случайно выбираем между HourlyWorker и MonthlyWorker
            Worker worker = getRandomBoolean() ? new HourlyWorker(i, "Рабочий №" + i, randomSalary) : new MonthlyWorker(i, "Рабочий №" + i, randomSalary);

            //Добавляем рабочего в список
            workers.add(worker);
        }

        List<Map<String, String>> SerializeList = new ArrayList<>();
        //Цикл по каждому элементу списка
        workers.forEach(worker -> {
            SerializeList.add(worker.Serialize());
        });

        //Конвертация в JSON и запись в файл
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            String result = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(workers);
            fileprocessing.Write(result);
        } catch(Exception e) {
            System.out.println("Возникла ошибка при записи в файл");
            e.printStackTrace();
        }

        return workers;

    }

    private static List<Worker> reader() throws IOException {

        List<Worker> workers = new ArrayList<Worker>();

        String result = fileprocessing.Read();
        System.out.println(result);

        //Переводим строку в list с map
        ObjectMapper mapper = new ObjectMapper();
        List<Map<String, String>> mapList = mapper.readValue(result, new TypeReference<List<Map<String, String>>>(){});


        //Цикл по каждому элементу списка
        mapList.forEach(data -> {

            if (data.get("type").equals("hourly"))
                workers.add(new HourlyWorker(data));
            else
                workers.add(new MonthlyWorker(data));
        });

        return workers;

    }

    public static void main(String[] args) throws IOException {
        System.out.println("Откуда вы хотите получить данные о рабочих?\n1. Сгенерировать данные\n2. Прочитать из файла\n->");
        Scanner scanner = new Scanner(System.in);
        String commandInput = scanner.next();
        System.out.println(commandInput);

        fileprocessing = new FileProcessing(filename);

        //Генерация данных
        if (commandInput.equals("1")) {
            List<Worker> workers = generator();
        }
        //Чтение из файла
        else if (commandInput.equals("2")) {
            List<Worker> workers = reader();
        }
        else {
            System.out.println("Нет такой команды");
        }

    }
}
