import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;

/**
 * Абстрактный класс рабочего
 */
public abstract class Worker {
    //Идентификатор рабочего (предположим, что это PK СУБД)
    int id;
    //ФИО
    String name;
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
    abstract String Serialize() throws JsonProcessingException;

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
    String Serialize() throws com.fasterxml.jackson.core.JsonProcessingException{
        return new ObjectMapper().writeValueAsString(this);
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
    String Serialize() throws com.fasterxml.jackson.core.JsonProcessingException{
        return new ObjectMapper().writeValueAsString(this);
    }
}
