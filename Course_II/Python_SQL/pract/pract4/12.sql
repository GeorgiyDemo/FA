/*
Упражение 12 стр 45
*/
SELECT student_id, MAX(mark) FROM exam_marks
GROUP BY student_id;