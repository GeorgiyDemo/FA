SELECT * FROM subject s
WHERE EXISTS (
    SELECT subj_id, COUNT(student_id)
    FROM exam_marks em
    WHERE s.subj_id=en.subj_id
    GROUP BY subj_id
    HAVING COUNT(student_id) > 1
)