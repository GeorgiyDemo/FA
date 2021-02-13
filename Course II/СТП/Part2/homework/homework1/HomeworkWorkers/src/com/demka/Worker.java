package com.demka;

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
     * Конвертация данного экземпляра класса в строку
     */
    abstract String ToString();

    //TODO: Организовать запись и чтение коллекции в/из файл(а)
    //TODO: Организовать обработку некорректного формата входного файла
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
    String ToString() {
        return null;
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
    String ToString() {
        return null;
    }
}