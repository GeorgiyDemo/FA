/*
Упражение 7 стр 42
*/
SELECT  "Код-"||univ_id || "; " || univ_name || "-г." || UPPER(city )|| "; Рейтинг=" || rating || "."  AS result FROM university;