/*
Создать 3 класса(базовый и 2 предка) которые описывают некоторых работников с почасовой оплатой (один из предков) и фиксированной оплатой (второй предок).
Описать в базовом классе абстрактный метод для расчета среднемесячной зарплаты.
Для «почасовщиков» формула для расчета такая: «среднемесячная зарплата = 20.8*8*ставка в час»,
для работников с фиксированной оплатой «среднемесячная зарплата = фиксированной месячной оплате».
a)Упорядочить всю последовательность рабочих по убыванию среднемесячной зарплаты.
При совпадении зарплаты – упорядочить данные в алфавитном порядке по имени. Вывести идентификатор работника,
имя и среднемесячную зарплату для всех элементов списка.
b)Вывести первые 5 имен работников из полученного выше списка (задача А).
c)Вывести последние 3 идентификаторы работников из полученного више списка (задача А).
d)Организовать запись и чтение коллекции в/из файл(а)
e)Организовать обработку некорректного формата входного файла

 */

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.*;

public class Main {


    private static final String filename = "./dump.json";
    private static FileProcessing fileprocessing;
    private static List<Worker> valuesList;

    private static boolean getRandomBoolean() {
        Random random = new Random();
        return random.nextBoolean();
    }

    /**
     * Сортировка данных коллекции по зарплате.
     * Если зарплата совпадает - по имени
     *
     * @param localeWorkers
     */
    private static void order(List<Worker> localeWorkers) {

        localeWorkers.sort((Comparator) (o1, o2) -> {

            double salary1 = ((Worker) o1).getTotalSalary();
            double salary2 = ((Worker) o2).getTotalSalary();
            if (salary1 > salary2) {
                return -1;
            } else if (salary1 < salary2) {
                return 1;
            }
            //Если зарпалты равны, то сравниваем по именам
            else {
                String name1 = ((Worker) o1).getName();
                String name2 = ((Worker) o2).getName();
                return name1.compareTo(name2);
            }
        });
    }

    /**
     * Логика для выполнения дополнительных заданий с выводом элементов коллекции
     */
    private static void taskSolver() {
        /*
        a)Упорядочить всю последовательность рабочих по убыванию среднемесячной зарплаты.
        При совпадении зарплаты – упорядочить данные в алфавитном порядке по имени. Вывести идентификатор работника,
        имя и среднемесячную зарплату для всех элементов списка.
        b)Вывести первые 5 имен работников из полученного выше списка (задача А).
        c)Вывести последние 3 идентификаторы работников из полученного више списка (задача А).
        d)Организовать запись и чтение коллекции в/из файл(а)
        e)Организовать обработку некорректного формата входного файла
         */

        //Сортировка
        order(valuesList);

        System.out.println("\nВывести первые 5 имен работников из полученного выше списка.");
        for (int i = 0; i < 5; i++) {
            Worker worker = valuesList.get(i);
            System.out.println(worker.getName() + " зарплата " + worker.getTotalSalary());
        }

        System.out.println("\nВывести последние 3 идентификаторы работников из полученного выше списка.");
        Collections.reverse(valuesList);
        for (int i = 0; i < 3; i++) {
            Worker worker = valuesList.get(i);
            System.out.println("ID" + worker.getId() + " зарплата " + worker.getTotalSalary());
        }

    }

    private static List<Worker> generator() {

        List<Worker> workers = new ArrayList<>();
        for (int i = 0; i < 5000; i++) {

            //Генерируем рандомную зарплату
            Random r = new Random();
            double randomSalary = 100 + (10000 - 100) * r.nextDouble();

            //Случайно выбираем между HourlyWorker и MonthlyWorker
            Worker worker = getRandomBoolean() ? new HourlyWorker(i, "Рабочий №" + i, randomSalary) : new MonthlyWorker(i, "Рабочий №" + i, randomSalary);

            //Добавляем рабочего в список
            workers.add(worker);
        }

        System.out.println("Успешная генерация");

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
            System.out.println("Успешная запись в файл");
        } catch (Exception e) {
            System.out.println("Возникла ошибка при записи в файл");
            e.printStackTrace();
        }

        return workers;

    }

    /**
     * Чтения преобразования данных JSON из файла
     * В готовую коллекцию моделей, с которыми можно работать
     *
     * @return
     * @throws IOException
     */
    private static List<Worker> reader() throws IOException {

        List<Worker> workers = new ArrayList<>();

        String result = fileprocessing.Read();

        //Переводим строку в list с map
        try {
            ObjectMapper mapper = new ObjectMapper();
            List<Map<String, String>> mapList = mapper.readValue(result, new TypeReference<List<Map<String, String>>>() {
            });

            //Цикл по каждому элементу списка
            for (Map<String, String> data : mapList) {
                if (data.get("type").equals("hourly"))
                    workers.add(new HourlyWorker(data));
                else
                    workers.add(new MonthlyWorker(data));
            }

            System.out.println("Успешно прочитали данные из файла");
        } catch (JsonProcessingException e) {
            System.out.println("Ошибка преобразования данных из файла, перегенерируем данные..");
            workers = generator();
        }
        return workers;
    }

    /**
     * Точка входа в программе
     *
     * @param args
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
        System.out.println("Как вы хотите получить информацию о рабочих?\n1. Сгенерировать данные\n2. Прочитать данные из файла\n->");
        Scanner scanner = new Scanner(System.in);
        String commandInput = scanner.next();

        fileprocessing = new FileProcessing(filename);

        //Генерация данных
        if (commandInput.equals("1")) {
            valuesList = generator();
        }
        //Чтение из файла
        else if (commandInput.equals("2")) {
            valuesList = reader();
        } else {
            System.out.println("Нет такой команды");
            return;
        }
        //Выполнение второстепенных заданий
        taskSolver();
    }
}
