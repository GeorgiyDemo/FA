/**
 * Класс для генерации рандомных данных для пользователей системы
 */
package sample.utils;


import com.github.javafaker.Faker;

public class PersonGenerator {

    Faker faker = new Faker();
    private  String firstName;
    private  String lastName;
    private  String street;
    private  String city;
    private Integer postalCode;
    private  Integer dateYear;
    private Integer dateMonth;
    private Integer dateDayOfMonth;

    public PersonGenerator(){

        this.firstName = generatorFirstName();
        this.lastName = generatorLastName();
        this.street = generatorStreet();
        this.city = generatorCity();
        this.postalCode = generatorPostalCode();
        this.dateYear = 1980 + (int)(Math.random() * ((2006 - 1980) + 1));
        this.dateMonth = 1 + (int)(Math.random() * ((12 - 1) + 1));
        this.dateDayOfMonth = 1 + (int)(Math.random() * ((31 - 1) + 1));
    }

    private String generatorFirstName(){
        return faker.name().firstName();
    }
    private String generatorLastName(){
        return faker.name().lastName();
    }

    private String generatorStreet(){
        return faker.address().streetAddress();
    }

    private String generatorCity(){
        return faker.address().city();
    }

    private Integer generatorPostalCode(){
        return 100000 + (int)(Math.random() * ((999999 - 100000) + 1));
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getStreet() {
        return street;
    }

    public String getCity() {
        return city;
    }

    public Integer getPostalCode() {
        return postalCode;
    }

    public Integer getDateYear() {
        return dateYear;
    }

    public Integer getDateMonth() {
        return dateMonth;
    }

    public Integer getDateDayOfMonth() {
        return dateDayOfMonth;
    }
}
