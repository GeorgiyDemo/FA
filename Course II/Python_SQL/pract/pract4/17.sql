/*
Упражение 17 стр 45
*/

SELECT student_id,AVG(mark)
FROM exam_marks
GROUP BY student_id;