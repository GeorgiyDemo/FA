package sample.models;

import com.google.gson.Gson;
import javafx.beans.property.*;
import sample.utils.DateUtil;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

public class Person implements APIModel {

    private final StringProperty firstName;
    private final StringProperty lastName;
    private final StringProperty street;
    private final StringProperty city;
    private final IntegerProperty postalCode;
    private final ObjectProperty<LocalDate> birthday;

    private final IntegerProperty id;


    public Person() {
        this(null, null, null, null, null, null);
    }

    //Перегрузка, чтоб с JSON было удобно извлекать, уже указывается определенный id
    public Person(String firstName, String lastName, String street, String city, Integer postalCode, LocalDate birthday, Integer id) {
        this.firstName = new SimpleStringProperty(firstName);
        this.lastName = new SimpleStringProperty(lastName);
        this.street = new SimpleStringProperty(street);
        this.city = new SimpleStringProperty(city);
        this.postalCode = new SimpleIntegerProperty(postalCode);
        this.birthday = new SimpleObjectProperty<>(birthday);
        this.id = new SimpleIntegerProperty(id);
    }

    public Person(String firstName, String lastName, String street, String city, Integer postalCode, LocalDate birthday) {
        this.firstName = new SimpleStringProperty(firstName);
        this.lastName = new SimpleStringProperty(lastName);
        this.street = new SimpleStringProperty(street);
        this.city = new SimpleStringProperty(city);
        this.postalCode = new SimpleIntegerProperty(postalCode);
        this.birthday = new SimpleObjectProperty<>(birthday);
        this.id = null;
    }

    @Override
    public String toJson() {

        Map<String, String> map = new HashMap<>();
        map.put("firstName", firstName.get());
        map.put("lastName", lastName.get());
        map.put("street", street.get());
        map.put("postalCode", String.valueOf(postalCode.get()));
        map.put("city", city.get());
        map.put("birthday", DateUtil.format(birthday.get()));

        Gson gson = new Gson();
        return gson.toJson(map);
    }

    public String getLastName() {
        return lastName.get();
    }

    public void setLastName(String lastName) {
        this.lastName.set(lastName);
    }

    public StringProperty getLastNameProperty() {
        return lastName;
    }

    public String getFirstName() {
        return firstName.get();
    }

    public void setFirstName(String firstName) {
        this.firstName.set(firstName);
    }

    public StringProperty getFirstNameProperty() {
        return firstName;
    }

    public String getStreet() {
        return street.get();
    }

    public void setStreet(String street) {
        this.street.set(street);
    }

    public StringProperty getStreetProperty() {
        return street;
    }

    public int getPostalCode() {
        return postalCode.get();
    }

    public void setPostalCode(String postalCode) {
        this.postalCode.set(Integer.parseInt(postalCode));
    }

    public IntegerProperty getPostalCodeProperty() {
        return postalCode;
    }

    public String getCity() {
        return city.get();
    }

    public void setCity(String city) {
        this.city.set(city);
    }

    public StringProperty getCityProperty() {
        return city;
    }

    public LocalDate getBirthday() {
        return birthday.get();
    }

    public void setBirthday(LocalDate birthday) {
        this.birthday.set(birthday);
    }

    public ObjectProperty<LocalDate> getBirthdayProperty() {
        return birthday;
    }

    public int getId() {
        return id.get();
    }
}
