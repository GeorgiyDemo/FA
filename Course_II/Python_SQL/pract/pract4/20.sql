/*
Упражение 20 стр 45
*/

SELECT (semester + 1) / 2 as kurs, count(*) as  "Кол-во предметов'"
FROM subject 
GROUP BY kurs;