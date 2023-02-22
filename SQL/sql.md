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
    - `ROUND(1)` : 소수 두번째 자리에서 반올림
- `MAX()` : 최댓값
- `MIN()` : 최솟값
- `SUM()` : 합계

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


## 그룹화하여 조건 찾기
- 그룹화
    -  COUNT 함수로 데이터를 조회하면 전체 갯수만을 가져옴
    - 유형별로 갯수를 알고 싶을 때는 컬럼에 데이터를 그룹화 할 수 있는 GROUP BY를 사용함
- `GROUP BY column_name HAVING (조건)`
    - `WEHRE` vs `GROUP BY` :  WHERE는 그룹화 하기 전이고, HAVING은 그룹화 후에 조건
- 예: `GROUP BY a.id HAVING a.address LIKE '서울%'`

<br>

## 조건문
- `IFNULL()`
    - `IFNULL(num, 'NONE')` : num이 null일 경우 'NONE'으로 출력

<br>

## limit
- `LIMIT 1` : 1개만 출력

## count
- `COUNT(*)` : 수 세기

## 중복 제거
- `DISTINCT column_name`

## IS NULL
- NULL 인 값 출력
    - `WHERE NAME IS NULL`
    - `WHERE NAME = 'NULL'`