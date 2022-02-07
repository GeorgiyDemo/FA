/*
1. Напишите запрос для вывода идентификатора (номера) предмета
обучения, его наименования, семестра, в котором он читается, и
количества отводимых на него часов для всех строк таблицы SUBJECT.
*/
SELECT * FROM subject;
SELECT SUBJ_ID, SUBJ_NAME, HOUR, SEMESTER FROM subject;

/*
2. Напишите запрос, позволяющий вывести все строки таблицы
EXAM_MARKS, в которых предмет обучения имеет номер (SUBJ_ID),
равный 12.
*/
SELECT * FROM exam_marks WHERE SUBJ_ID=12;


/*
3. Напишите запрос, выбирающий все данные из таблицы STUDENT,
расположив столбцы таблицы в следующем порядке: KURS, SURNAME,
NAME, STIPEND.
*/
SELECT KURS, SURNAME, NAME, STIPEND FROM STUDENT;

/*
4. Напишите запрос SELECT, который выполняет вывод наименований
п ред метов обуч ения (SUBJ_NAME) и след ом з а ним колич еств а ч а сов
(HOUR) д ля кажд ого п ред мета обуч ения (SUBJECT) в 4-м семестре
(SEMESTR).
*/
SELECT subj_name, hour FROM subject WHERE SEMESTER=4

/*
5. Напишите запрос, позволяющий получить из таблицы EXAM_MARKS
значения столбца MARK (экзаменационная оценка) для всех студентов,
исключив из списка повторение одинаковых строк.
*/
SELECT DISTINCT MARK FROM exam_marks;

/*
6. Напишите запрос, который выполняет вывод списка фамилий студентов,
обучающихся на третьем и более старших курсах.
*/
SELECT surname FROM student WHERE KURS>2

/*
7. Напишите запрос, выбирающий данные о фамилии, имени и номерекурса
для студентов, получающих стипендию больше 140.
*/
SELECT SURNAME, NAME, KURS FROM student WHERE STIPEND>140

/*
8. Напишите запрос, выполняющий выборку из таблицы SUBJECT названий
всех предметов обучения, на которые отводится более 30 часов.
*/
SELECT SUBJ_NAME FROM julia_lisina.subject WHERE hour>30

/*
9. Напишите запрос, который выполняет вывод списка университетов,
рейтингкоторых превышает 300 баллов.
*/
SELECT UNIV_NAME FROM university WHERE RATING>300;

/*
10. Напишите запрос к таблице STUDENT для вывода списка фамилий
(SURNAME), имен (NAME) и номера курса (KURS) всех студентов со
стипендией большей или равной 100, и живущих в Воронеже.
*/
SELECT SURNAME, NAME, KURS FROM student WHERE (STIPEND>=100 AND CITY="Воронеж")


/*
11. Будут выведены данные студентов, у которых стипендия меньше 100 или студенты, у которых
ДР НЕ больше или равно 10/03/1980 и их ID НЕ больше 1003
*/
SELECT *
FROM STUDENT
WHERE (STIPEND < 100 OR
NOT (BIRTHDAY >= '10/03/1980' AND STUDENT_ID > 1003 ));

/*
*/
SELECT *
FROM STUDENT
WHERE NOT(
    (BIRTHDAY ='10/03/1980' OR STIPEND>100)
    AND STUDENT_ID > = 1003
);