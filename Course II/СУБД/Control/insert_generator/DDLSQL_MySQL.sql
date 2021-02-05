/*
DROP TABLE staffs_houses;
DROP TABLE products_count;
DROP TABLE orders;
DROP TABLE houses;
DROP TABLE bookings;
DROP TABLE staffs;
DROP TABLE clients;
DROP TABLE products;
*/
CREATE TABLE clients (
    id                 INT,
    first_name         VARCHAR(40) NOT NULL,
    last_name          VARCHAR(40) NOT NULL,
    email              VARCHAR(40) NOT NULL,
    phone              VARCHAR(40) NOT NULL,
    document_title     VARCHAR(40) NOT NULL,
    document_file      VARBINARY(2000) NOT NULL,
    document_text      VARCHAR(400) NOT NULL,
    document_comments  VARCHAR(400),
    special_requests   VARCHAR(400),
    CONSTRAINT client_pk PRIMARY KEY ( id )
);

CREATE TABLE staffs (
    id          INT,
    first_name  VARCHAR(40) NOT NULL,
    last_name   VARCHAR(40) NOT NULL,
    position    VARCHAR(40) NOT NULL,
    type        VARCHAR(40) NOT NULL,
    phone       VARCHAR(40) NOT NULL,
    CONSTRAINT staff_pk PRIMARY KEY ( id )
);

CREATE TABLE bookings (
    id         INT,
    client_id  INT NOT NULL,
    date_in    DATE NOT NULL,
    date_out   DATE NOT NULL,
    cost       FLOAT NOT NULL,
    staff_id   INT NOT NULL,
    CONSTRAINT booking_pk PRIMARY KEY ( id ),
    CONSTRAINT booking_client_fk FOREIGN KEY ( client_id ) REFERENCES clients ( id ),
    CONSTRAINT booking_staff_fk FOREIGN KEY ( staff_id ) REFERENCES staffs ( id )
);

CREATE TABLE houses (
    id           INT,
    name         VARCHAR(40) NOT NULL,
    price        FLOAT NOT NULL,
    ac           INT NOT NULL,
    tv           INT NOT NULL,
    safe         INT NOT NULL,
    description  VARCHAR(400),
    type         VARCHAR(40),
    booking_id   INT,
    CONSTRAINT house_pk PRIMARY KEY ( id ),
    CONSTRAINT house_booking_fk FOREIGN KEY ( booking_id ) REFERENCES bookings ( id )
);

CREATE TABLE orders (
    id          INT,
    order_date  DATE NOT NULL,
    client_id   INT NOT NULL,
    cost        FLOAT NOT NULL,
    CONSTRAINT order_pk PRIMARY KEY ( id ),
    CONSTRAINT order_client_fk FOREIGN KEY ( client_id ) REFERENCES clients ( id )
);

CREATE TABLE products (
    id     INT,
    title  VARCHAR(40) NOT NULL,
    price  FLOAT NOT NULL,
    CONSTRAINT product_pk PRIMARY KEY ( id )
);

CREATE TABLE products_count (
    product_id  INT NOT NULL,
    count       INT NOT NULL,
    order_id    INT NOT NULL,
    CONSTRAINT product_count_pk PRIMARY KEY ( product_id, order_id ),
    CONSTRAINT product_count_order_fk FOREIGN KEY ( order_id ) REFERENCES orders ( id ),
    CONSTRAINT product_count_product_fk FOREIGN KEY ( product_id ) REFERENCES products ( id )
);

CREATE TABLE staffs_houses (
    house_id  INT NOT NULL,
    staff_id  INT NOT NULL,
    CONSTRAINT staff_house_pk PRIMARY KEY ( house_id, staff_id ),
    CONSTRAINT staff_house_house_fk FOREIGN KEY ( house_id ) REFERENCES houses ( id ),
    CONSTRAINT staff_house_staff_fk FOREIGN KEY ( staff_id ) REFERENCES staffs ( id )
);

/*
INSERT INTO clients (id, first_name, last_name, email, phone, document_title, document_file, document_text) VALUES (1, 'Георгий', 'Деменчук', 'demenchuk.george@protonmail.com','79999645590','Паспорт гражданина РФ', hextoraw('453d7a34'), 'document_text')
*/