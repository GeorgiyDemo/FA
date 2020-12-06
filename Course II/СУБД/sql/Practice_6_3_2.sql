DROP TABLE STUDENT_COURSE_DETAILS;
DROP TABLE EXAM_RESULTS;
DROP TABLE EXAMS;
DROP TABLE EXAM_TYPES;
DROP TABLE FACULTY_COURSE_DETAILS;
DROP TABLE FACULTY_LOGIN_DETAILS;
DROP TABLE STUDENT_ATTENDANCES;
DROP TABLE STUDENTS;
DROP TABLE PARENTS_INFORMATION;
DROP TABLE FULL_TIMES;
DROP TABLE PART_TIMES;
DROP TABLE FACULTIES;
DROP TABLE COURSES;
DROP TABLE DEPARTMENTS;
DROP TABLE "ONLINE";
DROP TABLE SEATED;
DROP TABLE ACADEMIC_SESSIONS;

CREATE TABLE ACADEMIC_SESSIONS (
    id    NUMBER NOT NULL,
    name  VARCHAR2(400) NOT NULL,
    CONSTRAINT academic_session_pk PRIMARY KEY ( id )
);

CREATE TABLE SEATED (
    building     VARCHAR2(400) NOT NULL,
    room         VARCHAR2(400) NOT NULL,
    "DateTime"  TIMESTAMP NOT NULL,
    CONSTRAINT seated_pk PRIMARY KEY ( "DateTime", building, room )
);

CREATE TABLE "ONLINE" (
    logon_id  NUMBER NOT NULL,
    password  VARCHAR2(400) NOT NULL,
    CONSTRAINT online_pk PRIMARY KEY ( logon_id )
);

CREATE TABLE DEPARTMENTS (
    id    NUMBER NOT NULL,
    name  VARCHAR2(400) NOT NULL,
    head  VARCHAR2(400) NOT NULL,
    CONSTRAINT department_pk PRIMARY KEY ( id )
);

CREATE TABLE COURSES (
    id                   NUMBER NOT NULL,
    name                 VARCHAR2(400) NOT NULL,
    department_id        NUMBER NOT NULL,
    academic_session_id  NUMBER NOT NULL,
    online_logon_id      NUMBER,
    seated_building      VARCHAR2(400),
    seated_room          VARCHAR2(400),
    SEATED_DateTime   TIMESTAMP,
    id1                  NUMBER NOT NULL,
    id2                  NUMBER NOT NULL,
    building             VARCHAR2(400) NOT NULL,
    room                 VARCHAR2(400) NOT NULL,
    CONSTRAINT course_pk PRIMARY KEY ( id ),
    CONSTRAINT course_academic_session_fk FOREIGN KEY ( academic_session_id ) REFERENCES ACADEMIC_SESSIONS ( id ),
    CONSTRAINT course_department_fk FOREIGN KEY ( department_id ) REFERENCES DEPARTMENTS ( id ),
    CONSTRAINT course_online_fk FOREIGN KEY ( online_logon_id ) REFERENCES "ONLINE" ( logon_id ),
    CONSTRAINT course_seated_fk FOREIGN KEY ( SEATED_DateTime, seated_building, seated_room ) REFERENCES SEATED ( "DateTime", building, room )
);

CREATE TABLE FACULTIES (
    id             NUMBER NOT NULL,
    first_name     VARCHAR2(400) NOT NULL,
    last_name      VARCHAR2(400) NOT NULL,
    email          VARCHAR2(400) NOT NULL,
    department_id  NUMBER NOT NULL,
    id1            NUMBER NOT NULL,
    CONSTRAINT faculty_pk PRIMARY KEY ( id ),
    CONSTRAINT faculty_department_fk FOREIGN KEY ( department_id ) REFERENCES DEPARTMENTS ( id )
);

CREATE TABLE FULL_TIMES (
    id              NUMBER NOT NULL,
    salary          NUMBER NOT NULL,
    insurance_plan  VARCHAR2(400) NOT NULL,
    CONSTRAINT full_time_pk PRIMARY KEY ( id ),
    CONSTRAINT full_time_faculty_fk FOREIGN KEY ( id ) REFERENCES FACULTIES ( id )
);

CREATE TABLE PART_TIMES (
    id           NUMBER NOT NULL,
    hourly_rate  NUMBER NOT NULL,
    CONSTRAINT part_time_pk PRIMARY KEY ( id ),
    CONSTRAINT part_time_faculty_fk FOREIGN KEY ( id ) REFERENCES FACULTIES ( id )

);

CREATE TABLE PARENTS_INFORMATION (
    id                   NUMBER NOT NULL,
    parent_1_first_name  VARCHAR2(400) NOT NULL,
    parent_1_last_name   VARCHAR2(400) NOT NULL,
    parent_2_first_name  VARCHAR2(400) NOT NULL,
    parent_2_last_name   VARCHAR2(400) NOT NULL,
    CONSTRAINT parent_information_pk PRIMARY KEY ( id )
);

CREATE TABLE STUDENTS (
    id                     NUMBER NOT NULL,
    first_name             VARCHAR2(400) NOT NULL,
    last_name              VARCHAR2(400) NOT NULL,
    registration_year      TIMESTAMP NOT NULL,
    email                  VARCHAR2(400) NOT NULL,
    parent_information_id  NUMBER,
    id1                    NUMBER,
    CONSTRAINT student_pk PRIMARY KEY ( id ),
    CONSTRAINT student_parent_information_fk FOREIGN KEY ( parent_information_id ) REFERENCES PARENTS_INFORMATION ( id )
);

CREATE TABLE STUDENT_ATTENDANCES (
    number_of_working_days  NUMBER NOT NULL,
    number_of_days_off      NUMBER NOT NULL,
    eligibility_for_exam    NUMBER,
    student_id              NUMBER NOT NULL,
    academic_session_id     NUMBER NOT NULL,
    id                      NUMBER NOT NULL,
    id1                     NUMBER NOT NULL,
    CONSTRAINT student_attendance_pk PRIMARY KEY ( id, id1 ),
    CONSTRAINT student_aa_session_fk FOREIGN KEY ( academic_session_id ) REFERENCES ACADEMIC_SESSIONS ( id ),
    CONSTRAINT student_attendance_student_fk FOREIGN KEY ( student_id ) REFERENCES STUDENTS ( id )

);

CREATE TABLE FACULTY_LOGIN_DETAILS (
    login_datetime  TIMESTAMP NOT NULL,
    faculty_id      NUMBER NOT NULL,
    CONSTRAINT faculty_login_detail_pk PRIMARY KEY ( faculty_id ),
    CONSTRAINT faculty_ldetail_faculty_fk FOREIGN KEY ( faculty_id ) REFERENCES FACULTIES ( id )
);

CREATE TABLE FACULTY_COURSE_DETAILS (
    contact_hours  VARCHAR2(400) NOT NULL,
    course_id      NUMBER NOT NULL,
    faculty_id     NUMBER NOT NULL,
    CONSTRAINT faculty_course_detail_pk PRIMARY KEY ( course_id, faculty_id ),
    CONSTRAINT faculty_cdetail_course_fk FOREIGN KEY ( course_id ) REFERENCES COURSES ( id ),
    CONSTRAINT faculty_cdetail_faculty_fk FOREIGN KEY ( faculty_id ) REFERENCES FACULTIES ( id )
);

CREATE TABLE EXAM_TYPES (
    type         NUMBER NOT NULL,
    name         VARCHAR2(400) NOT NULL,
    description  VARCHAR2(400),
    CONSTRAINT exam_type_pk PRIMARY KEY ( type )
);


CREATE TABLE EXAMS (
    id              NUMBER NOT NULL,
    start_date      TIMESTAMP,
    course_id       NUMBER NOT NULL,
    exam_type_type  NUMBER NOT NULL,
    CONSTRAINT exam_pk PRIMARY KEY ( id ),
    CONSTRAINT exam_course_fk FOREIGN KEY ( course_id ) REFERENCES COURSES ( id ),
    CONSTRAINT exam_exam_type_fk FOREIGN KEY ( exam_type_type ) REFERENCES EXAM_TYPES ( type )
);

CREATE TABLE EXAM_RESULTS (
    grade       NUMBER NOT NULL,
    course_id   NUMBER NOT NULL,
    student_id  NUMBER NOT NULL,
    exam_id     NUMBER NOT NULL,
    id          NUMBER NOT NULL,
    CONSTRAINT EXAM_RESULTS_pk PRIMARY KEY ( course_id, exam_id, id ),
    CONSTRAINT EXAM_RESULTS_course_fk FOREIGN KEY ( course_id ) REFERENCES COURSES ( id ),
    CONSTRAINT EXAM_RESULTS_exam_fk FOREIGN KEY ( exam_id ) REFERENCES EXAMS ( id ),
    CONSTRAINT EXAM_RESULTS_student_fk FOREIGN KEY ( student_id ) REFERENCES STUDENTS ( id )
);

CREATE TABLE STUDENT_COURSE_DETAILS (
    grade       NUMBER NOT NULL,
    course_id   NUMBER NOT NULL,
    student_id  NUMBER NOT NULL,
    id          NUMBER NOT NULL,
    CONSTRAINT STUDENT_COURSE_DETAILS_pk PRIMARY KEY ( course_id, id ),
    CONSTRAINT student_cdetail_course_fk FOREIGN KEY ( course_id ) REFERENCES COURSES ( id ),
    CONSTRAINT student_cdetail_student_fk FOREIGN KEY ( student_id ) REFERENCES STUDENTS ( id )
);