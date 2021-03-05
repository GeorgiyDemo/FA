/*
Упражение 3 стр 41
*/

SELECT LOWER(SUBSTR(NAME, 1, 1) || "."|| SURNAME)  ||  "; место жительства-"  || LOWER(city) || "; родился - " || TO_CHAR(birthday, 'DD.MM.YY')  AS  result  FROM  student;