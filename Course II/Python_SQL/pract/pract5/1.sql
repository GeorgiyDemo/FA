/*
Упражение 1 стр 41
*/

SELECT student_id || ";" || UPPER(surname) || ";" || UPPER(name) || ";" || stipend || ";"|| UPPER(city) || ";" || strftime('%d/%m/%Y',birthday) || ";" || univ_id  AS  result  FROM  student;