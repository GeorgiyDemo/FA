SELECT * FROM student
WHERE EXISTS (
    SELECT * FROM university
    WHERE rating>300 AND student.univ_id=university.univ_id
);