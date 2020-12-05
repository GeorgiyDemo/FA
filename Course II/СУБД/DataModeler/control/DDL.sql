CREATE TABLE booking (
    id         NUMBER,
    client_id  NUMBER NOT NULL,
    date_in    DATE NOT NULL,
    date_out   DATE NOT NULL,
    cost       FLOAT NOT NULL,
    staff_id   NUMBER NOT NULL,
    CONSTRAINT booking_pk PRIMARY KEY ( id )
);

CREATE TABLE client (
    id                 NUMBER NOT NULL,
    first_name         VARCHAR2(400) NOT NULL,
    last_name          VARCHAR2(400) NOT NULL,
    email              VARCHAR2(400) NOT NULL,
    phone              VARCHAR2(400) NOT NULL,
    document_title     VARCHAR2(400) NOT NULL,
    document_file      RAW(2000) NOT NULL,
    special_requests   VARCHAR2(400),
    document_text      VARCHAR2(400),
    document_comments  VARCHAR2(400)
);

ALTER TABLE client ADD CONSTRAINT client_pk PRIMARY KEY ( id );

CREATE TABLE house (
    id           NUMBER NOT NULL,
    name         VARCHAR2(400) NOT NULL,
    price        FLOAT NOT NULL,
    ac           NUMBER NOT NULL,
    tv           NUMBER NOT NULL,
    safe         NUMBER NOT NULL,
    description  VARCHAR2(400),
    type         VARCHAR2(400),
    booking_id   NUMBER
);

ALTER TABLE house ADD CONSTRAINT house_pk PRIMARY KEY ( id );

CREATE TABLE house_staff (
    house_id  NUMBER NOT NULL,
    staff_id  NUMBER NOT NULL
);

ALTER TABLE house_staff ADD CONSTRAINT house_staff_pk PRIMARY KEY ( house_id,
                                                                    staff_id );

CREATE TABLE "ORDER" (
    id         NUMBER NOT NULL,
    "date"     DATE NOT NULL,
    client_id  NUMBER NOT NULL,
    cost       FLOAT NOT NULL
);

ALTER TABLE "ORDER" ADD CONSTRAINT order_pk PRIMARY KEY ( id );

CREATE TABLE product (
    id     NUMBER NOT NULL,
    title  VARCHAR2(400) NOT NULL,
    price  FLOAT NOT NULL
);

ALTER TABLE product ADD CONSTRAINT product_pk PRIMARY KEY ( id );

CREATE TABLE product_count (
    product_id  NUMBER NOT NULL,
    count       NUMBER NOT NULL,
    order_id    NUMBER NOT NULL
);

ALTER TABLE product_count ADD CONSTRAINT product_count_pk PRIMARY KEY ( product_id,
                                                                        order_id );

CREATE TABLE staff (
    id          NUMBER NOT NULL,
    first_name  VARCHAR2(400) NOT NULL,
    last_name   VARCHAR2(400) NOT NULL,
    position    VARCHAR2(400) NOT NULL,
    type        VARCHAR2(400) NOT NULL,
    phone       VARCHAR2(400) NOT NULL
);

ALTER TABLE staff ADD CONSTRAINT staff_pk PRIMARY KEY ( id );

ALTER TABLE booking
    ADD CONSTRAINT booking_client_fk FOREIGN KEY ( client_id )
        REFERENCES client ( id );

ALTER TABLE booking
    ADD CONSTRAINT booking_staff_fk FOREIGN KEY ( staff_id )
        REFERENCES staff ( id );

ALTER TABLE house
    ADD CONSTRAINT house_booking_fk FOREIGN KEY ( booking_id )
        REFERENCES booking ( id );

ALTER TABLE house_staff
    ADD CONSTRAINT house_staff_house_fk FOREIGN KEY ( house_id )
        REFERENCES house ( id );

ALTER TABLE house_staff
    ADD CONSTRAINT house_staff_staff_fk FOREIGN KEY ( staff_id )
        REFERENCES staff ( id );

ALTER TABLE "ORDER"
    ADD CONSTRAINT order_client_fk FOREIGN KEY ( client_id )
        REFERENCES client ( id );

ALTER TABLE product_count
    ADD CONSTRAINT product_count_order_fk FOREIGN KEY ( order_id )
        REFERENCES "ORDER" ( id );

ALTER TABLE product_count
    ADD CONSTRAINT product_count_product_fk FOREIGN KEY ( product_id )
        REFERENCES product ( id );