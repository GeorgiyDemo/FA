/*
Упражение 8 стр 42
*/
SELECT  "Код-"||univ_id || "; " || univ_name || "-г." || UPPER(city )|| "; Рейтинг=" || ROUND(rating,-2) || "."  AS result FROM university;