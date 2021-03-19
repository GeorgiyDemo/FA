SELECT name FROM student WHERE student_id IN 
	(SELECT  student_id  FROM exam_marks WHERE subj_id = 102
		AND mark <  (
			SELECT AVG(mark) FROM exam_marks)
	);