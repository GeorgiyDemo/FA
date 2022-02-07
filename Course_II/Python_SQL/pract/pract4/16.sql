/*
Упражение 16 стр 45
*/

SELECT 
student.kurs,
AVG(exam_marks.mark),
exam_marks.subj_id
FROM student 
INNER JOIN exam_marks ON student.student_id=exam_marks.student_id
GROUP BY student.kurs, exam_marks.subj_id