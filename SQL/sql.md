# 🔢SQL 문법 정리

## 기본 형태
```SQL
SELECT (column_name ...) AS (column_name) FROM (table_name)
WHERE (조건) AND (조건) ...
ORDER BY (column_name)
```

<br>

## JOIN ON
```SQL
SELECT * FROM table1 A
JOIN table2 B ON A.id = B.id
```

<br>

## 숫자
- `AVG()` : 평균
- `ROUND()` : 소수 첫번째 자리에서 반올림
    - `ROUND(1.25, 1)` : **1.3** -> 소수 두번째 자리에서 반올림
- `TRUNCATE( , 0)` : 소수점을 버림(입력 파라미터가 무조건 2개)
    - `TRUNCATE(1.25, 1)` : **1.2** -> 소수 첫째 자리까지 나타냄
- `MAX()` : 최댓값
- `MIN()` : 최솟값
- `SUM()` : 합계
- `COUNT(*)` : 수 세기 (GROUP BY 와 함께 쓰임)

<br>

## 날짜
- 년/월/일 출력
    - `YEAR(date)`
    - `MONTH(date)`
    - `DAY(date)`
- `DATE_FORMAT()`
    - `DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')` : **2029-02-09** 형식으로 출력

<br>

## 정렬
- `ORDER BY column_name ASC` : 오름차순 정렬 (ASC 생략 가능)
- `ORDER BY column_name DESC` : 내림차순 정렬
- `ORDER BY column1, column2` : column1 순으로 정렬 후, 다시 column2 순으로 정렬

<br>

## 비교
- `=` 같음
    - `WHERE AGE = 3` (⭕)
    - `WHERE AGE == 3` (❌)
- `<>` 같지 않음
    - `!=` 은 사용가능하지만, ISO 표준이 아님
- `BETWEEN a AND b`
    - a <= _ <= b 일 때
    - 예: `WHERE HOUR(DATETIME) BETWEEN 9 AND 19`

<br>

## 나열
- 컬럼 명이나 테이블 명을 나열할 때 : `,`
    - 예: `SELECT column1, column2 FROM table_name`
- 조건을 나열할 때 : `AND`
    - 예: `WHERE (조건) AND (조건) ...`

<br>

## 문자열 부분 일치
- `WHERE column_name LIKE '패턴'`
	- `%` : 모든 문자
	- `_` : 한 글자
- 예
    - `LIKE '%라면%'` : 삼양라면, 신라면, 진라면 큰컵 등
    - `LIKE '_라면'` : 신라면, 진라면 등
    - `LIKE '라면'` : 라면


## 문자열 일치
- `WHERE 라면 = '신라면'`
- `WHERE 라면 IN ('진라면', '신라면')`

<br>

## 조건문
- `IFNULL()`
    - `IFNULL(num, 'NONE')` : num이 null일 경우 'NONE'으로 출력

<br>

## limit
- `LIMIT 1` : 1개만 출력

## 중복 제거
- `DISTINCT column_name`

## IS NULL
- NULL 인 값 출력
    - `WHERE NAME IS NULL`
    - `WHERE NAME = 'NULL'`

## 특정 순서대로 출력
- 예: `ORDER BY FIELD(STRING, 'C', 'B', 'A')`
    - C, B, A 순으로 출력

<br>

## GROUP BY
- 그룹화
    - 유형별로 갯수 등을 알고 싶을 때는 컬럼에 데이터를 그룹화 할 수 있는 GROUP BY를 사용함
    - 해당 컬럼의 카테고리로 반복문을 돈다고 생각할 것
        - 예를 들어 `GROUP BY DATE`를 하면 DATE에 따른 `MIN(PRICE)`(최소가격), `COUNT(*)`(개수) 등을 반복문 돌려서 DATE를 기준으로 표를 출력한다고 생각할 것
- `GROUP BY column_name HAVING (조건)`
    - `WEHRE` vs `HAVING` :  WHERE는 그룹화 하기 전이고, HAVING은 그룹화 후에 조건
    - 예: `SELECT ORDER_DATE FROM ORDER WHERE ORDER_DATE > DATE('1996-12-31') GROUP BY ORDERDATE HAVING COUNT(ORDER_DATE) >= 2`
    - 1996-12-31 이후의 데이터 중 주문 개수가 2개 이상인 주문 날짜들을 조회
- GROUP BY와 DISTINCT 함께 활용하기
    - `SELECT COUNTRY, COUNT(DISTINCT CITY) FROM CUSTOMERS GROUP BY COUNTRY`
    - COUNTRY에서 중복되지 않는 CITY 개수 출력

<br>

## 서브 쿼리
- 다른 테이블로부터 정보를 가져오고 싶을 때 사용함
- `SUM()`, `MAX()`, `AVG()` 등과 같은 수학 함수 활용
- 예: 가격이 50 이상인 상품의 카테고리 정보를 출력하기
```sql
SELECT CategoryID, CategoryName, Description FROM Categories
WHERE
  CategoryID IN
  (SELECT CategoryID FROM Products
  WHERE Price > 50)
```
- 예: 상품 정보를 출력할 때 카테고리 이름도 출력하기
```sql
SELECT
  ProductID, ProductName,
  (
    SELECT CategoryName FROM Categories C
    WHERE C.CategoryID = P.CategoryID
  ) AS CategoryName
FROM Products P
```
- 예: 평균 가격보다 낮은 상품들 출력하기
```sql
SELECT
  ProductID, ProductName, CategoryID, Price
FROM Products P1
WHERE Price < AVG(Price) (
  SELECT AVG(Price) FROM Products P2
  WHERE P2.CategoryID = P1.CategoryID)
```

<br>

## JOIN ON
- TABLE끼리 합칠 때
- 내부 조인
```sql
SELECT * FROM Categories C
JOIN Products P ON C.CategoryID = P.CategoryID
```
- 외부 조인(LEFT/RIGHT JOIN)
    - 내부 조인의 경우는 일치하지 않는 데이터는 검색하지 않았지만, 외부 조인의 경우 일치하지 않는 경우도 데이터로 받아옴
    ![image](https://user-images.githubusercontent.com/87802191/220915388-94a706a0-7216-4767-a6f2-9d0fa4667f99.png)
- 교차 조인(CROSS JOIN)
    - 조건 없이 모든 조합 반환(A * B)
    ```sql
    SELECT E1.LastName, E2.FirstName FROM Employees E1
    CROSS JOIN Employees E2
    ```

<br>

## 집합
- 합집합
    - `UNION` : 중복을 제거한 집합
    - `UNION ALL` : 중복을 제거하지 않은 집합
- 공급자와 수요자를 함께 이름 순으로 출력
```sql
SELECT CustomerName AS Name, City, Country, 'CUSTOMER' FROM Customers
UNION
SELECT SupplierName, City, Country, 'SUPPLIER' FROM Suppliers
ORDER BY Name;
```
- 합집합(UNION)
```sql
SELECT CategoryID AS ID FROM Categories
WHERE CategoryID > 4
UNION
SELECT EmployeeID AS ID FROM Employees
WHERE EmployeeID % 2 = 0;
```
- 교집합(WHERE AND)
```sql
SELECT CategoryID AS ID FROM Categories C, Employees E
WHERE
  C.CategoryID > 4
  AND E.EmployeeID % 2 = 0
  AND C.CategoryID = E.EmployeeID
```
- 차집합(NOT IN)
```sql
SELECT CategoryID AS ID FROM Categories
WHERE 
  CategoryID > 4
  AND CategoryID NOT IN (
    SELECT EmployeeID
    FROM Employees
    WHERE EmployeeID % 2 = 0)
```
- 대칭차집합(UNION ALL)
```sql
SELECT ID FROM (
  SELECT CategoryID AS ID FROM Categories
  WHERE CategoryID > 4
  UNION ALL
  SELECT EmployeeID AS ID FROM Employees
  WHERE EmployeeID % 2 = 0
) AS Temp 
GROUP BY ID HAVING COUNT(*) = 1  -- 중복되는 데이터들 제거
```

<br>

## CASE WHEN ~ THEN ~ ELSE ~ END
```sql
CASE
    WHEN '조건' THEN '출력할 데이터'
    ELSE '출력할 데이터'
END
```

```sql
CASE 
    WHEN OUT_DATE <= DATE('2022-05-01') THEN '출고완료'
    ELSE CASE WHEN OUT_DATE IS NULL THEN '출고미정'
    ELSE '출고대기' 
    END
END
```

<br>

## 문자열
### 합치기 - CONCAT(A, B, C)
- `SELECT CONCAT("1","-","2")` -> '1-2'
- `SELECT CONCAT(fist_name, last_name)` -> 'GildongHong'
- `SELECT CONCAT(first_name, " ", last_name)` -> 'Gildong Hong'

### 자르기 - SUBSTR(str, pos), SUBSTR(str, pos, len), SUBSTRING(str, pos), SUBSTRING(str, pos, len), LEFT(str, len), RIGHT(str, len), MID(str, pos, len)
- `SELECT SUBSTRING('Quadratically', 5)` -> 'ratically'
- `SELECT SUBSTRING('foobarbar' FROM 4)` -> 'barbar'
- `SELECT SUBSTRING('Quadratically', 5, 6)` -> 'ratica'
- `SELECT SUBSTRING('Sakila', -3)` -> 'ila'
- `SELECT SUBSTRING('Sakila', -5, 3)` -> 'aki'
- `SELECT SUBSTRING('Sakila' FROM -4 FOR 2)` -> 'ki'
- `SELECT LEFT('abcdefg', 3)` -> 'abc'
- `SELECT MID('abcdefg', 2, 4)` -> 'bcde'
- `SELECT RIGHT('abcdefg', 3)` -> 'efg'

### 대체하기 - REPLACE(str, from_str, to_str)
- `ELECT REPLACE('www.mysql.com', 'com', 'kr')` -> www.mysql.kr

### 길이 - LENGTH(str), CHAR_LENGTH(str)
- 