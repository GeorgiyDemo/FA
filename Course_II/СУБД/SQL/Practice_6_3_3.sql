/*
6-3-3-1
*/
CREATE TABLE dept (
    dept_id    NUMBER(8) NOT NULL,
    dept_name  NVARCHAR2(30) NOT NULL,
    loc_id     NUMBER(4) NOT NULL,
    CONSTRAINT dept_pk PRIMARY KEY ( dept_id, loc_id )
);

/*
6-3-3-2
*/
CREATE TABLE products (
    id              NUMBER(10) NOT NULL,
    suppliers_id    NUMBER(15) NOT NULL,
    suppliers_name  NVARCHAR2(30) NOT NULL,
    CONSTRAINT products_pk PRIMARY KEY ( id ),
    CONSTRAINT products_suppliers_fk FOREIGN KEY ( suppliers_id, suppliers_name ) REFERENCES suppliers ( id, name )
);

CREATE TABLE suppliers (
    id            NUMBER(15) NOT NULL,
    name          NVARCHAR2(30) NOT NULL,
    contact_name  NUMBER(4) NOT NULL,
    CONSTRAINT suppliers_pk PRIMARY KEY ( id, name )
);

/*
6-3-3-3
*/
CREATE TABLE dept_sample (
    id      NUMBER(8) NOT NULL,
    name    NVARCHAR2(30) NOT NULL,
    loc_id  NUMBER(4) NOT NULL,
    CONSTRAINT dept_sample_pk PRIMARY KEY ( id, name )
);