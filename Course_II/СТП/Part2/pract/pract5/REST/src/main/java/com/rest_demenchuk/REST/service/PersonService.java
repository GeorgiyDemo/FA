package com.rest_demenchuk.REST.service;



import com.rest_demenchuk.REST.entity.Person;

import java.util.List;

public interface PersonService {

    Person create(Person person);

    List<Person> readAll();

    Person read(int id);

    boolean update(Person person, int id);

    boolean delete(int id);
}