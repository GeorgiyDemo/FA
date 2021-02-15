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
    Map<String, String> Serialize() {
        Map<String, String> map = new HashMap<>();
        map.put("id", String.valueOf(this.id));
        map.put("name", this.name);
        map.put("salary", Double.toString(this.salary));
        map.put("type", this.type);
        return map;
    }

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

    public double getTotalSalary() {
        return totalSalary;
    }
}

