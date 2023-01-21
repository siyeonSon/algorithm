# python 문법 정리

## 🐰list
- `list(str(num))` : 숫자 → 리스트
- `array.count(str(0))` : 리스트에서 특정 값 갯수
- `array.append` VS `array.extend()`
    - `array = [1, 2, 3] ; array.append([4, 5])` → **[1, 2, 3, [4, 5]]**
    - `array = [1, 2, 3]; array.extend([4, 5])`  → **[1, 2, 3, 4, 5]**

- 배열 초기화
    - `[[0]] * 3` → **[[0], [0], [0]]**
    - `[0] * 3`  → **[0, 0, 0]**

<br>

## 🐰2차원 배열
`a = "*" ; print(a[0][0])` → **"*"**

<br>

## 🐰수학
### 🥕순열(P), 조합(C)
- `from itertools import permutations, combinations`
    - `permutations(nums ,2)` → nP2
    - `combinations(nums ,2)` → nC2

<br>

### 🥕최대공약수(GCD), 최대공배수(LCM)
- `import math`
    - `math.gcd(n, m)` → 최대공약수
    - `(n*m)//math.gcd(n,m)` → 최대공배수

<br>

## 🐰연산
- 반올림 : `round()`
- 절댓값 : `abs()`

- `import math`
    - 올림 : `math.ceil()`
    - 내림 : `math.floor()`

<br>

## 🐰정렬
### 🥕리스트 정렬
- `sorted(a)`
    - 파이썬 내장 함수
    - 리스트, 튜플, 문자열 등 가능
    - 내림차순 정렬 : `sorted(a, reverse=True)`
    - 활용 : `''.join(sorted("35214"))` → **12345**
- `a.sort()`
    - 파이썬 리스트는 `sort()` 메소드를 가지고 있음
    - 내림차순 정렬 : `a.sort(reverse=True)`

<br>

### 🥕역순O 내림차순X 
- `reversed(a)` : 문자를 역순으로 접근
    - 단점 : 반복자 타입을 반환함
    - `print(reversed(a))`하면 **<reversed object at 0x1050ca1d0>** 가 출력됨
    ```python
    print("".join(reversed(s))
    ```
- `a.reverse()` : 리스트를 거꾸로 뒤집음

<br>

### 🥕리스트 중복 제거
1. list -> set -> list
    - 단점 : 순서 뒤죽박죽
    ```python
    list(set(a))
    ```

2. for문
    ```python
    nums = [10, 22, 19, 22, 1, 10, 5]
    result = []

    for n in nums:
        if n not in result:
            result.append(n)

    print(result)
    ```

3. list comprehension
    ```python
    nums = [10, 22, 19, 22, 1, 10, 5]
    result = []

    [result.append(n) for n in nums if n not in result]

    print(result)
    ```

<br>

## 🐰I/O
`import sys`

`input = int(sys.stdin.readline())`

`n, m = map(int, input().split())`

`numbers = list(map(int, input().split()))`