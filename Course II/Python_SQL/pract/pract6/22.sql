SELECT student_id, 
MAX(mark) AS max_mark
FROM exam_marks
GROUP BY student_id;

SELECT student_id,
MIN(mark) AS min_mark
FROM exam_marks
GROUP BY student_id;