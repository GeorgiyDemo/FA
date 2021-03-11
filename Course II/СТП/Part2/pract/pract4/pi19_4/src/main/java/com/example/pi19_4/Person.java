package com.example.pi19_4;

public class Person {
    private Integer id;
    private String firstName;
    private String lastName;
    private String street;
    private String postalCode;
    private String birthday;
    private String city;

    public String getCity() {
        return city;
    }

    public String getBirthday() {
        return birthday;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public Integer getId() {
        return id;
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

    public void setId(Integer id) {
        this.id = id;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
