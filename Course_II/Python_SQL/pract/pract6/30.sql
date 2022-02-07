SELECT name, student_id
FROM student
WHERE student_id IN (
    SELECT student_id FROM (
        SELECT MAX(stipend), student_id
        FROM student
        GROUP BY city
    )
)