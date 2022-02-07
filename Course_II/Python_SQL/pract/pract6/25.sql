SELECT exam_date, AVG(mark) AS result
FROM exam_marks
GROUP BY exam_date ORDER BY result DESC;

SELECT exam_date, MIN(mark) AS result
FROM exam_marks
GROUP BY exam_date ORDER BY result DESC;

SELECT exam_date, MAX(mark) AS result
FROM exam_marks
GROUP BY exam_date ORDER BY result DESC;