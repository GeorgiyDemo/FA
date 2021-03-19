SELECT mark
FROM exam_marks 
WHERE student_id =(
		SELECT  student_id 
		FROM student
		WHERE surname = 'Иванов'
	)
