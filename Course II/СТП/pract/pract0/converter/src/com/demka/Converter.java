package com.demka;

public abstract class Converter {
    public abstract double getTemp(double value);
}

class Fahrenheit extends  Converter{

    @Override
    public double getTemp(double value) {
        return 9.0/5.0 * value + 32;
    }
}
