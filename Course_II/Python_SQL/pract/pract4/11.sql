/*
Упражение 11 стр 44
*/
SELECT student_id, MIN(mark) FROM exam_marks
GROUP BY student_id;