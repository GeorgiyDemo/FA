/*
Упражение 15 стр 45
*/

SELECT count(DISTINCT student_id) AS "Кол-во студентов" , exam_date AS "Дата экзамена", exam_id AS "id экзамена"
FROM exam_marks
GROUP BY exam_date