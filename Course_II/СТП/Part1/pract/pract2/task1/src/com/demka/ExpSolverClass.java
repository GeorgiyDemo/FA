package com.demka;

 /*3) Найдите корень уравнения cos⁡(x^5 )+ x^4-345.3*x-23=0 на отрезке [0;10]
с точностью по x не хуже 0.001. Известно, что на этом промежутке корень единственный.
Используйте для этого метод деления отрезка пополам (и рекурсию).
 */

public class ExpSolverClass {

    //точность
    double e = 0.001;
    //Результат
    double result;

    public ExpSolverClass(double begin, double end){
        setResult(solver(begin,end));
    }

    //Исходная функция
    public double exp(double x)
    {
        return Math.cos(Math.pow(x,  5)) + Math.pow(x, 4) - 345.3 * x - 23;
    }

    public double solver(double begin, double end)
    {
        //Выход из рекурсии
        if(end - begin <= e)
            return begin;

        //Деление пополам
        double x = begin + (end - begin) / 2;

        //Вызываем рекурсию с концом или началом
        if (exp(begin) * exp(x) > 0)
            return solver(x, end);
        else
            return solver(begin, x);
    }

    public double getResult() {
        return result;
    }

    public void setResult(double result) {
        this.result = result;
    }
}
