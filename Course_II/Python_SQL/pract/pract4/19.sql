/*
Упражение 19 стр 45
*/

SELECT exam_id, COUNT(student_id) AS "Кол-во студентов"
FROM exam_marks
GROUP BY exam_id;