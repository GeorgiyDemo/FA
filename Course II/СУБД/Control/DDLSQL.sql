DROP TABLE staffs_houses;
DROP TABLE products_count;
DROP TABLE orders;
DROP TABLE houses;
DROP TABLE bookings;
DROP TABLE staffs;
DROP TABLE clients;
DROP TABLE products;

CREATE TABLE clients (
    id                 NUMBER,
    first_name         VARCHAR2(40) NOT NULL,
    last_name          VARCHAR2(40) NOT NULL,
    email              VARCHAR2(40) NOT NULL,
    phone              VARCHAR2(40) NOT NULL,
    document_title     VARCHAR2(40) NOT NULL,
    document_file      RAW(2000) NOT NULL,
    document_text      VARCHAR2(400) NOT NULL,
    document_comments  VARCHAR2(400),
    special_requests   VARCHAR2(400),
    CONSTRAINT client_pk PRIMARY KEY ( id )
);

CREATE TABLE staffs (
    id          NUMBER,
    first_name  VARCHAR2(40) NOT NULL,
    last_name   VARCHAR2(40) NOT NULL,
    position    VARCHAR2(40) NOT NULL,
    type        VARCHAR2(40) NOT NULL,
    phone       VARCHAR2(40) NOT NULL,
    CONSTRAINT staff_pk PRIMARY KEY ( id )
);

CREATE TABLE bookings (
    id         NUMBER,
    client_id  NUMBER NOT NULL,
    date_in    DATE NOT NULL,
    date_out   DATE NOT NULL,
    cost       FLOAT NOT NULL,
    staff_id   NUMBER NOT NULL,
    CONSTRAINT booking_pk PRIMARY KEY ( id ),
    CONSTRAINT booking_client_fk FOREIGN KEY ( client_id ) REFERENCES clients ( id ),
    CONSTRAINT booking_staff_fk FOREIGN KEY ( staff_id ) REFERENCES staffs ( id )
);

CREATE TABLE houses (
    id           NUMBER,
    name         VARCHAR2(40) NOT NULL,
    price        FLOAT NOT NULL,
    ac           NUMBER NOT NULL,
    tv           NUMBER NOT NULL,
    safe         NUMBER NOT NULL,
    description  VARCHAR2(400),
    type         VARCHAR2(40),
    booking_id   NUMBER,
    CONSTRAINT house_pk PRIMARY KEY ( id ),
    CONSTRAINT house_booking_fk FOREIGN KEY ( booking_id ) REFERENCES bookings ( id )
);

CREATE TABLE orders (
    id          NUMBER,
    order_date  DATE NOT NULL,
    client_id   NUMBER NOT NULL,
    cost        FLOAT NOT NULL,
    CONSTRAINT order_pk PRIMARY KEY ( id ),
    CONSTRAINT order_client_fk FOREIGN KEY ( client_id ) REFERENCES clients ( id )
);

CREATE TABLE products (
    id     NUMBER,
    title  VARCHAR2(40) NOT NULL,
    price  FLOAT NOT NULL,
    CONSTRAINT product_pk PRIMARY KEY ( id )
);

CREATE TABLE products_count (
    product_id  NUMBER NOT NULL,
    count       NUMBER NOT NULL,
    order_id    NUMBER NOT NULL,
    CONSTRAINT product_count_pk PRIMARY KEY ( product_id, order_id ),
    CONSTRAINT product_count_order_fk FOREIGN KEY ( order_id ) REFERENCES orders ( id ),
    CONSTRAINT product_count_product_fk FOREIGN KEY ( product_id ) REFERENCES products ( id )
);

CREATE TABLE staffs_houses (
    house_id  NUMBER NOT NULL,
    staff_id  NUMBER NOT NULL,
    CONSTRAINT staff_house_pk PRIMARY KEY ( house_id, staff_id ),
    CONSTRAINT staff_house_house_fk FOREIGN KEY ( house_id ) REFERENCES houses ( id ),
    CONSTRAINT staff_house_staff_fk FOREIGN KEY ( staff_id ) REFERENCES staffs ( id )
);