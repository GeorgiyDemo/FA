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
    name  VARCHAR2(400) NOT NULL
);

CREATE TABLE SEATED (
    building     VARCHAR2(400) NOT NULL,
    room         VARCHAR2(400) NOT NULL,
    "DateTime"  TIMESTAMP NOT NULL
);

CREATE TABLE "ONLINE" (
    logon_id  NUMBER NOT NULL,
    password  VARCHAR2(400) NOT NULL
);

CREATE TABLE DEPARTMENTS (
    id    NUMBER NOT NULL,
    name  VARCHAR2(400) NOT NULL,
    head  VARCHAR2(400) NOT NULL
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
    room                 VARCHAR2(400) NOT NULL
);

CREATE TABLE FACULTIES (
    id             NUMBER NOT NULL,
    first_name     VARCHAR2(400) NOT NULL,
    last_name      VARCHAR2(400) NOT NULL,
    email          VARCHAR2(400) NOT NULL,
    department_id  NUMBER NOT NULL,
    id1            NUMBER NOT NULL

);

CREATE TABLE FULL_TIMES (
    id              NUMBER NOT NULL,
    salary          NUMBER NOT NULL,
    insurance_plan  VARCHAR2(400) NOT NULL
);

CREATE TABLE PART_TIMES (
    id           NUMBER NOT NULL,
    hourly_rate  NUMBER NOT NULL
);

CREATE TABLE PARENTS_INFORMATION (
    id                   NUMBER NOT NULL,
    parent_1_first_name  VARCHAR2(400) NOT NULL,
    parent_1_last_name   VARCHAR2(400) NOT NULL,
    parent_2_first_name  VARCHAR2(400) NOT NULL,
    parent_2_last_name   VARCHAR2(400) NOT NULL
);

CREATE TABLE STUDENTS (
    id                     NUMBER NOT NULL,
    first_name             VARCHAR2(400) NOT NULL,
    last_name              VARCHAR2(400) NOT NULL,
    registration_year      TIMESTAMP NOT NULL,
    email                  VARCHAR2(400) NOT NULL,
    parent_information_id  NUMBER,
    id1                    NUMBER
);

CREATE TABLE STUDENT_ATTENDANCES (
    number_of_working_days  NUMBER NOT NULL,
    number_of_days_off      NUMBER NOT NULL,
    eligibility_for_exam    NUMBER,
    student_id              NUMBER NOT NULL,
    academic_session_id     NUMBER NOT NULL,
    id                      NUMBER NOT NULL,
    id1                     NUMBER NOT NULL
);

CREATE TABLE FACULTY_LOGIN_DETAILS (
    login_datetime  TIMESTAMP NOT NULL,
    faculty_id      NUMBER NOT NULL
);

CREATE TABLE FACULTY_COURSE_DETAILS (
    contact_hours  VARCHAR2(400) NOT NULL,
    course_id      NUMBER NOT NULL,
    faculty_id     NUMBER NOT NULL
);

CREATE TABLE EXAM_TYPES (
    type         NUMBER NOT NULL,
    name         VARCHAR2(400) NOT NULL,
    description  VARCHAR2(400)
);


CREATE TABLE EXAMS (
    id              NUMBER NOT NULL,
    start_date      TIMESTAMP,
    course_id       NUMBER NOT NULL,
    exam_type_type  NUMBER NOT NULL
);

CREATE TABLE EXAM_RESULTS (
    grade       NUMBER NOT NULL,
    course_id   NUMBER NOT NULL,
    student_id  NUMBER NOT NULL,
    exam_id     NUMBER NOT NULL,
    id          NUMBER NOT NULL
);

CREATE TABLE STUDENT_COURSE_DETAILS (
    grade       NUMBER NOT NULL,
    course_id   NUMBER NOT NULL,
    student_id  NUMBER NOT NULL,
    id          NUMBER NOT NULL
);