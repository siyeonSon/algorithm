-- 2023-02-19 19:55:48
-- https://school.programmers.co.kr/learn/courses/30/lessons/59408

SELECT COUNT(DISTINCT NAME) AS COUNT FROM ANIMAL_INS
WHERE NAME <> 'NULL'