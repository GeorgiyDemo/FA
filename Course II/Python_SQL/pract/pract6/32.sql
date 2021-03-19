SELECT name, student_id FROM student s
WHERE city NOT IN (
    SELECT city
    FROM university u
    WHERE ((s.univ_id = u.univ_id) AND (s.city = u.city)) OR (s.city IS NULL)
)

SELECT student.name, student.student_id
FROM student 
INNER JOIN university ON student.univ_id=university.univ_id
WHERE student.city != university.city;