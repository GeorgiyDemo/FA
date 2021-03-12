/*
Упражение 6 стр 42
*/
SELECT UPPER(NAME || " " || SURNAME)  || " родился в " || strftime('%Y',birthday) || " году"   AS  result
FROM  student
WHERE kurs IN (1,2,4)