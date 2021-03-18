package com.rest_demenchuk.REST.controller;


import com.rest_demenchuk.REST.entity.Person;
import com.rest_demenchuk.REST.repository.PersonRepository;
import com.rest_demenchuk.REST.service.PersonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class PersonController {
    private final PersonService personService;

    @Autowired
    public PersonController(PersonService personService) {
        this.personService = personService;
    }

    @PostMapping(value = "/persons")
    public ResponseEntity<?> create(@RequestBody Person person) {
        Person newPerson = personService.create(person);
        return new ResponseEntity<>(person, HttpStatus.CREATED);
    }

    @GetMapping(value = "/persons")
    public ResponseEntity<List<Person>> read() {
        final List<Person> persons = personService.readAll();
        return persons != null && !persons.isEmpty() ? new ResponseEntity<>(persons, HttpStatus.OK) : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @GetMapping(value = "/persons/{id}")
    public ResponseEntity<Person> read(@PathVariable(name = "id") int id) {
        final Person person = personService.read(id);
        return person != null ? new ResponseEntity<>(person, HttpStatus.OK) : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    /**
     * Обновление пользователей
     *
     * @param id
     * @param newPerson
     * @return
     */
    @PutMapping(value = "/persons/{id}")
    public ResponseEntity<Person> put(@PathVariable(name = "id") int id, @RequestBody Person newPerson) {

        //Если успешно обновлили данные
        if (personService.update(newPerson, id)) {
            //id персоны чтоб отдавался
            Person newPersonWithId = personService.read(id);
            return new ResponseEntity<>(newPersonWithId, HttpStatus.OK);
        }
        //Если не получилось обновить данные
        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    /**
     * Удаление пользователей
     *
     * @param id
     * @return
     */
    @DeleteMapping(value = "/persons/{id}")
    public ResponseEntity<?> delete(@PathVariable(name = "id") int id) {
        final Person person = personService.read(id);
        //Если есть такой пользователь
        if (person != null) {
            personService.delete(id);
            return new ResponseEntity<>(HttpStatus.OK);
        }
        //Если такого пользователя нет
        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

}
