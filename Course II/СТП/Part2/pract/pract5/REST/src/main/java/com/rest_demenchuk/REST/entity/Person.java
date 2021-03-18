package com.rest_demenchuk.REST.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.GeneratorType;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.time.LocalDate;

@Entity
@Data
@NoArgsConstructor
public class Person {
    @Id
    private Long id;

    private String firstName;
    private String lastName;
    private String street;
    private String postalCode;
    private LocalDate birthday;
    private String city;
}
