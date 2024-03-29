-- 2023-02-24 18:41:26
-- https://school.programmers.co.kr/learn/courses/30/lessons/133027

-- 정답 1
SELECT A.FLAVOR FROM FIRST_HALF A
JOIN JULY B ON A.FLAVOR = B.FLAVOR
GROUP BY A.FLAVOR
ORDER BY (A.TOTAL_ORDER + SUM(B.TOTAL_ORDER)) DESC
LIMIT 3

-- 정답 2
SELECT FLAVOR FROM 
(SELECT * FROM FIRST_HALF 
UNION
SELECT * FROM JULY) C
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3