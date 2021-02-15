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

