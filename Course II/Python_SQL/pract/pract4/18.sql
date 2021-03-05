/*
Упражение 18 стр 45
*/

SELECT exam_id, AVG(mark)
FROM exam_marks
GROUP BY exam_id;