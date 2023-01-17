# python 문법 정리

## 🐰list
- `list(str(num))` : 숫자 → 리스트
- `array.count(str(0))` : 리스트에서 특정 값 갯수
- `array.append` VS `array.extend()`
    - `array = [1, 2, 3] ; array.append([4, 5])` → **[1, 2, 3, [4, 5]]**
    - `array = [1, 2, 3]; array.extend([4, 5])`  → **[1, 2, 3, 4, 5]**

<br>

## 🐰2차원 배열
`a = "*" ; print(a[0][0])` → **"*"**

<br>

## 🐰연산
- 반올림 : `round()`
- 올림 : `math.ceil()`
- 내림 : `math.floor()`
- 절댓값 : `abs()`

<br>

## 🐰정렬
### 🥕sort()
**1. 리스트 정렬**
- `sorted()` : 새로운 정렬된 리스트를 반환하는 함수
- `sort()` : 리스트 자체를 정렬하는 함수
- `a.sort(reverse=True)` : 내림차순 정렬


**2. 리스트 중복 제거**
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


### 🥕reversed()
- `reversed()` : 문자를 역순으로 접근
- 단점 : 반복자 타입을 반환함
    - `print(reversed(s))`하면 **<reversed object at 0x1050ca1d0>**가 출력됨
```python
print("".join(reversed(s))
```

<br>

## 🐰I/O
`import sys`

`input = int(sys.stdin.readline())`

`n, m = map(int, input().split())`

`numbers = list(map(int, input().split()))`