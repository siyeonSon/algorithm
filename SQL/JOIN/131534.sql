-- 2023-02-24 20:54:44
-- https://school.programmers.co.kr/learn/courses/30/lessons/131534

SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, COUNT(DISTINCT O.USER_ID) AS PUCHASED_USERS, ROUND(COUNT(DISTINCT O.USER_ID)/(SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) LIKE '2021'), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE O
JOIN USER_INFO U ON O.USER_ID = U.USER_ID
WHERE YEAR(U.JOINED) LIKE '2021'
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH