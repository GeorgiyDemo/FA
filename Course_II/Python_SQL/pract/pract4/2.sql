/*
Упражение 2 стр 41
*/

SELECT SUBSTR(NAME, 1, 1) || "."|| SURNAME  ||  "; место жительства-"  || UPPER(city) || "; родился - " || strftime('%d.%m.%Y.',birthday)  AS  result  FROM  student;