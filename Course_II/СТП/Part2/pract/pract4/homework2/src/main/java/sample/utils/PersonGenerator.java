/**
 * Класс для генерации рандомных данных для пользователей системы
 */
package sample.utils;


import com.github.javafaker.Faker;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

public class PersonGenerator {

    Faker faker = new Faker();
    private String firstName;
    private String lastName;
    private String street;
    private String city;
    private Integer postalCode;
    private LocalDate date;

    public PersonGenerator() {

        this.firstName = generatorFirstName();
        this.lastName = generatorLastName();
        this.street = generatorStreet();
        this.city = generatorCity();
        this.postalCode = generatorPostalCode();
        this.date = generatorDate();
    }

    private LocalDate generatorDate() {
        return convertToLocalDateViaInstant(faker.date().birthday());
    }

    public LocalDate convertToLocalDateViaInstant(Date dateToConvert) {
        return dateToConvert.toInstant()
                .atZone(ZoneId.systemDefault())
                .toLocalDate();
    }

    private String generatorFirstName() {
        return faker.name().firstName();
    }

    private String generatorLastName() {
        return faker.name().lastName();
    }

    private String generatorStreet() {
        return faker.address().streetAddress();
    }

    private String generatorCity() {
        return faker.address().city();
    }

    private Integer generatorPostalCode() {
        return 100000 + (int) (Math.random() * ((999999 - 100000) + 1));
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

    public LocalDate getDate() {
        return date;
    }
}
