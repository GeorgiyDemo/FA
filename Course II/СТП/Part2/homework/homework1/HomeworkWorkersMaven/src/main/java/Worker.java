import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;

import java.util.HashMap;
import java.util.Map;

/**
 * Абстрактный класс рабочего
 */
public abstract class Worker {
    //Идентификатор рабочего (предположим, что это PK СУБД)
    int id;
    //ФИО
    String name;
    //Тип рабочего (нужен для обратного преобразования из JSON
    String type;
    //зарплата за промежуток времени (час/месяц)
    double salary;
    //итоговая зарплата (вычисляемое значение в SalaryCalculation)
    double totalSalary;

    /**
     * Вычисление заработной платы рабочего
     */
    abstract void SalaryCalculation();

    /**
     * Запаковка для записи в файл
     */
    abstract Map<String, String> Serialize();

    /*
    Группа геттеров для нормального автопреобразования в json
     */
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public String getType() {
        return type;
    }
}

/**
 * Класс работника с почасовой оплатой труда
 */
class HourlyWorker extends Worker{

    /**
     * Конструктор класса HourlyWorker
     * @param name - ФИО рабочего для его идентификации
     */
    public HourlyWorker(int id, String name, double salary){
        this.id = id;
        this.name = name;
        this.salary = salary;
        this.type = "hourly";

        SalaryCalculation();
    }

    public HourlyWorker(Map<String, String> data) {
        this.id = Integer.parseInt(data.get("id"));
        this.name = data.get("name");
        this.salary = Double.parseDouble(data.get("salary"));
        this.type = data.get("type");

        SalaryCalculation();
    }

    /**
     * Вычисление заработной платы рабочего
     */
    @Override
    void SalaryCalculation() {
        //Для «почасовщиков» формула для расчета такая: «среднемесячная зарплата = 20.8*8*ставка в час»,
        this.totalSalary = 20.8*8* this.salary;
    }

    /** TODO
     * Конвертация данного экземпляра класса в строку
     */
    @Override
    public String toString() {
        return "ЭТО HourlyWorker";
    }

    /**
     * Запаковка для записи в файл
     */
    @Override
    Map<String, String> Serialize(){

        Map<String, String> map=new HashMap<String, String>();
        map.put("id", String.valueOf(this.id));
        map.put("name", this.name);
        map.put("salary", Double.toString(this.salary));
        map.put("type", this.type);
        return map;
    }

}

/**
 * Класс работника с фиксированной месячной оплатой
 */
class MonthlyWorker extends  Worker{

    public MonthlyWorker(int id, String name, double salary){
        this.id = id;
        this.name = name;
        this.salary = salary;
        this.type = "monthly";

        SalaryCalculation();
    }

    public MonthlyWorker(Map<String, String> data) {
        this.id = Integer.parseInt(data.get("id"));
        this.name = data.get("name");
        this.salary = Double.parseDouble(data.get("salary"));
        this.type = data.get("type");

        SalaryCalculation();
    }

    /**
     * Вычисление заработной платы рабочего
     */
    @Override
    void SalaryCalculation() {
        this.totalSalary = this.salary;
    }

    /** TODO
     * Конвертация данного экземпляра класса в строку
     */
    @Override
    public String toString() {
        return "ЭТО MonthlyWorker";
    }

    /**
     * Запаковка для записи в файл
     */
    @Override
    Map<String, String> Serialize(){

        Map<String, String> map=new HashMap<String, String>();
        map.put("id", String.valueOf(this.id));
        map.put("name", this.name);
        map.put("salary", Double.toString(this.salary));
        map.put("type", this.type);
        return map;
    }
}
