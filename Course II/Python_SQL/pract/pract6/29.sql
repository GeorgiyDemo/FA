SELECT COUNT(subj_id) AS result FROM subject WHERE subj_id IN (
    SELECT subj_id FROM exam_marks WHERE student_id IN (
        SELECT student_id FROM (
            SELECT student_id, COUNT(subj_id)
            FROM exam_marks
            GROUP BY student_id
            HAVING COUNT(subj_id) > 20
        )
    )
)