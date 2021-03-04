package com.example.pi19_4;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

@Service
public class PersonServiceImpl implements  PersonService{

    private  static Map<Integer, Person> REPOSITORY_MAP = new HashMap<>();

    private  static  final AtomicInteger PERSON_ID = new AtomicInteger();
    @Override
    public Person create(Person person) {

        final  int personId = PERSON_ID.incrementAndGet();
        person.setId(personId);
        REPOSITORY_MAP.put(personId,person);
        return person;
    }

    @Override
    public List<Person> readAll() {
        return new ArrayList<>(REPOSITORY_MAP.values());
    }

    @Override
    public Person read(int id) {
        return REPOSITORY_MAP.get(id);
    }

    @Override
    public boolean update(Person person, int id) {
        if (REPOSITORY_MAP.containsKey(id)){
            person.setId(id);
            REPOSITORY_MAP.put(id, person);
            return true;
        }
        return false;
    }

    @Override
    public boolean delete(int id) {
        return  REPOSITORY_MAP.remove(id) != null;
    }
}
