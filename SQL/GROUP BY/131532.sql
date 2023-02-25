-- 2023-02-25 09:11:30
-- https://school.programmers.co.kr/learn/courses/30/lessons/131532

SELECT YEAR(A.SALES_DATE) AS YEAR, MONTH(A.SALES_DATE) AS MONTH, B.GENDER, COUNT(DISTINCT A.USER_ID) AS USERS
FROM ONLINE_SALE A
JOIN USER_INFO B ON A.USER_ID = B.USER_ID
WHERE B.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, B.GENDER
ORDER BY YEAR, MONTH, B.GENDER