## 회전
### 1) zip()
```python
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 시계 방향 90 (= 반시계 방향 270)
# [[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]
arr_90 = list(map(list, zip(*arr[::-1])))

# 시계 방향 180 (= 반시계 방향 180)
# [[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
arr_180 = [a[::-1] for a in arr[::-1]]

# 시계 방향 270 (= 반시계 방향 90)
# [[4, 8, 12], [3, 7, 11], [2, 6, 10], [1, 5, 9]]
arr_270 = list(map(list, zip(*arr)))[::-1]
```

### 2) 인덱스 규칙을 찾아서 회전
- 정사각형
```python
n = 3
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 시계 방향 90 (= 반시계 방향 270)
arr_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_90[j][n-i-1] = arr[i][j]

# 시계 180 & 반시계 180
arr_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_180[n-i-1][n-j-1] = arr[i][j]

# 시계 270 & 반시계 90
arr_270 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_270[n-j-1][i] = arr[i][j]
```

- 직사각형
```python
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n, m = len(arr), len(arr[0])

# 시계 방향 90 (= 반시계 방향 270)
arr_90 = [[0]* n for _ in range(m)]  # 배열의 가로 세로 길이가 뒤바뀌는 것 주의
for i in range(n) :
    for j in range(m) :
        arr_90[j][n-i-1] = arr[i][j]

# 시계 180 & 반시계 180
arr_180 = [[0]* m for _ in range(n)] 
for i in range(n) :
    for j in range(m) :
        arr_180[n-i-1][m-j-1] = arr[i][j]

# 시계 270 & 반시계 90
arr_270 = [[0]* n for _ in range(m)]  # 배열의 가로 세로 길이가 뒤바뀌는 것 주의
for i in range(n) :
    for j in range(m) :
      arr_270[m-1-j][i] = arr[i][j]
```

## 부분 회전
```python
n = 7
arr = [[n * j + i for i in range(1, n+1)] for j in range(n)]
result = [[0] * n for _ in range(n)]
x, y = 2, 2  # 시작 지점
length = 3  # 부분 배열의 길이

def rotate_90(x, y, length) :
    # 부분 배열 회전
    rotated = [[0] * length for _ in range(length)]
    for i in range(length) :
        for j in range(length) :
            rotated[j][length-i-1] = arr[x+i][y+j]
    # 현재 값에 옮겨줌
    for i in range(length):
        for j in range(length):
            arr[x+i][y+j] = rotated[i][j]

rotate_90(x, y, length)

'''
# Before
[1, 2, 3, 4, 5, 6, 7]
[8, 9, 10, 11, 12, 13, 14]
[15, 16, 17, 18, 19, 20, 21]
[22, 23, 24, 25, 26, 27, 28]
[29, 30, 31, 32, 33, 34, 35]
[36, 37, 38, 39, 40, 41, 42]
[43, 44, 45, 46, 47, 48, 49]

# After
[1, 2, 3, 4, 5, 6, 7]
[8, 9, 10, 11, 12, 13, 14]
[15, 16, 31, 24, 17, 20, 21]
[22, 23, 32, 25, 18, 27, 28]
[29, 30, 33, 26, 19, 34, 35]
[36, 37, 38, 39, 40, 41, 42]
[43, 44, 45, 46, 47, 48, 49]
'''
```

## itertools 라이브러리 구현
- 순열(permutations)
```python
def permutations(arr, r):
    n = len(arr)
    result = []
    visited = [False] * n

    def backtrack(path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                backtrack(path + [arr[i]])
                visited[i] = False
    backtrack([])
    return result

arr = [1, 2, 3]
permutations(arr, 2)
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
```

- 조합 (combinations)
```python
def combinations(arr, r):
    n = len(arr)
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(start, n):
            backtrack(i + 1, path + [arr[i]])
    backtrack(0, [])
    return result

arr = [1, 2, 3]
combinations(arr, 2)
# [[1, 2], [1, 3], [2, 3]]
```

## 나선형 배열
### 안에서 밖으로
```python
n = 5
board = [[0] * N for _ in range(n)]

# 방향: ← ↓ → ↑
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def tornado():
    x = y = N // 2  # 중심 좌표
    direction = 0  # 동서남북 순서
    move_count = 0  # 같은 거리로 몇 번 이동했는지
    dist = 1  # 현재 방향으로 몇 칸 이동할지

    number = 1  # 현재 숫자
    board[x][y] = number

    while True:
        move_count += 1

        for _ in range(dist):
            x = x + dx[direction]
            y = y + dy[direction]

            # 나선형을 다 그린 경우
            if (x, y) == (0, -1):
                return

            number += 1
            board[x][y] = number

        # 같은 거리로 2번 이동한 후에 거리(dist)를 1 증가시켜야 함
        # 시작 → 1칸 → 1칸 → 2칸 → 2칸 → 3칸 → 3칸 → ...
        if move_count == 2:
            dist += 1
            move_count = 0

        direction = (direction + 1) % 4

tornado()
'''
[25, 24, 23, 22, 21]
[10, 9, 8, 7, 20]
[11, 2, 1, 6, 19]
[12, 3, 4, 5, 18]
[13, 14, 15, 16, 17]
'''
```

### 밖에서 안으로
```python
n = 5
board = [[0] * n for _ in range(n)]

# 시계방향: → ↓ ← ↑
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def tornado():
    x = y = 0  # 시작 위치
    direction = 0  # 동서남북 순서

    for number in range(1, n*n+1):
        board[x][y] = number

        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 다음 위치가 유효하지 않으면 방향 전환
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        x, y = nx, ny

tornado()
'''
[1, 2, 3, 4, 5]
[16, 17, 18, 19, 6]
[15, 24, 25, 20, 7]
[14, 23, 22, 21, 8]
[13, 12, 11, 10, 9]
'''
```

## 중력
- 바닥까지 하강
```python
arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

def gravity(arr) :
    n, m = len(arr), len(arr[0])
    for i in range(n-1) :
        for j in range(m) :
            p = i
            # 현재 칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸 씩 연쇄적으로 내려와야 함
            while p >= 0 and arr[p][j] == 1 and arr[p + 1][j] == 0:
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                p -= 1
gravity(arr)

'''
# Before
[0, 1, 0]
[1, 0, 1]
[0, 1, 0]
[0, 0, 1]
[0, 1, 0]

# After
[0, 0, 0]
[0, 0, 0]
[0, 1, 0]
[0, 1, 1]
[1, 1, 1]
'''
```