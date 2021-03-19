SELECT student.name, student.student_id
FROM student
INNER JOIN university ON student.univ_id=university.univ_id
WHERE rating > 300