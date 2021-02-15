import java.util.Map;

/**
 * Класс работника с почасовой оплатой труда
 */
public class HourlyWorker extends Worker {

    /**
     * Конструктор класса HourlyWorker
     *
     * @param name - ФИО рабочего для его идентификации
     */
    public HourlyWorker(int id, String name, double salary) {
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
        this.totalSalary = Utils.round(20.8 * 8 * this.salary,2);
    }

    /**
     * Конвертация данного экземпляра класса в строку
     */
    @Override
    public String toString() {
        return "*Рабочий с почасовой зарплатой*\nID: " + id + "\nИмя: " + name + "\nЗарплата: " + salary;
    }
}
