import java.util.HashMap;
import java.util.Map;

/**
 * Класс работника с фиксированной месячной оплатой
 */
public class MonthlyWorker extends  Worker{

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

        Map<String, String> map= new HashMap<>();
        map.put("id", String.valueOf(this.id));
        map.put("name", this.name);
        map.put("salary", Double.toString(this.salary));
        map.put("type", this.type);
        return map;
    }
}