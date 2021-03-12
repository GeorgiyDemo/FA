/*
Упражение 3 стр 41
*/

SELECT LOWER(SUBSTR(NAME, 1, 1) || "."|| SURNAME)  ||  "; место жительства-"  || LOWER(city) || "; родился - " || strftime('%d/%m/%Y',birthday)   AS  result  FROM  student;