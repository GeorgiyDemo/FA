/*
Упражение 4 стр 42
*/
SELECT NAME || " " || SURNAME  || " родился в " || strftime('%Y',birthday) || " году"   AS  result
FROM  student
WHERE student_id=10;