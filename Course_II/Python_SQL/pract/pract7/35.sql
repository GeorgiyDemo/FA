SELECT * FROM student s1
WHERE EXISTS (
    SELECT * FROM university u1 WHERE s1.city = u1.city AND u1.univ_id != s1.univ_id
) 