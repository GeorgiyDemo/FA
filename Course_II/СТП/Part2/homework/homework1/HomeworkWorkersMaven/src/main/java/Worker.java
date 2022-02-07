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
     *
     * @return
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

    /**
     * Getter id
     *
     * @return
     */
    public int getId() {
        return id;
    }

    /**
     * Getter name
     *
     * @return
     */
    public String getName() {
        return name;
    }

    /**
     * Getter salary
     *
     * @return
     */
    public double getSalary() {
        return salary;
    }

    /**
     * Getter type
     *
     * @return
     */
    public String getType() {
        return type;
    }

    /**
     * Getter totalSalary
     *
     * @return
     */
    public double getTotalSalary() {
        return totalSalary;
    }
}

