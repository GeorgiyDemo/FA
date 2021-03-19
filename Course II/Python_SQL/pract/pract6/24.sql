SELECT exam_date, SUM(mark) AS marks_count
FROM exam_marks
GROUP BY exam_date ORDER BY marks_count DESC;