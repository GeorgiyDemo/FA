/*
Упражение 14 стр 45
*/

SELECT subj_name, MAX(semester) AS max_semester FROM subject GROUP BY subj_name;