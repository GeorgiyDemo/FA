package com.demka;

class Converter implements ConverterInterface {

    @Override
    public double Celsius2Fahrenheit(double value) {
        return 1.8 * value + 32;
    }

    @Override
    public double Fahrenheit2Celsius(double value) {
        return (value - 32) / 1.8;
    }

    @Override
    public  double Celsius2Kelvin(double value){
        return value + 273.15;
    }

    @Override
    public double Kelvin2Celsius(double value) {
        return value - 273.15;
    }
}
