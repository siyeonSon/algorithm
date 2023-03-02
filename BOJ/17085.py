# 2023-03-02 19:20:05
# https://www.acmicpc.net/problem/17085

from itertools import combinations
import sys
input = sys.stdin.readline

answer = []  # x, y, 십자가의 길이
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 동서남북 십자가가 되는가?
def cross(x, y) :
    compass = []

    # @return 방향에 따른 #의 개수
    def count_star(x, y, xx, yy, cnt) :  # 중심(x, y), 탐색 방향(xx, yy), 증가값(cnt)
        while True :
            nx, ny = x+cnt*xx, y+cnt*yy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '#' :
                cnt += 1
                continue
            return cnt-1

    # 동서남북 길이로 #의 개수 구하기
    for i in range(4) :
        compass.append(count_star(x, y, dx[i], dy[i], 1))
    
    s = min(compass)  # 십자가의 길이
    for j in range(s, 0, -1) :
        answer.append([x, y, j])


# 두 십자가의 중첩 여부 확인
def duplicate(cross1, cross2) :
    visited = [[False]*m for _ in range(n)]

    # @return 십자가를 올바르게 그리면 True, 그리던 중 중첩되는 부분이 발견되면 False
    def visit_cross(cross, visited) :
        x, y, s = cross
        visited[x][y] = True
        for i in range(1, s+1) :
            for j in range(4) :
                nx, ny = x+i*dx[j], y+i*dy[j]
                if visited[nx][ny] :
                    return False  # 재방문하는 경우 False 반환 -> 중첩되는 경우
                visited[nx][ny] = True
        return True

    if visit_cross(cross1, visited) and visit_cross(cross2, visited) :  # 중첩되지 않는 경우
        s1, s2 = cross1[2], cross2[2]
        return (4*s1+1) * (4*s2+1)
    else :
        return 1


# (i, j)를 중심으로 하는 십자가 찾기
for i in range(1, n-1) :
    for j in range(1, m-1) :
        if board[i][j] == '#' :
            cross(i, j)

# 정답 출력
if len(answer) == 0 :
    print(1)
elif len(answer) == 1 :
    print(4*answer[0][2]+1)
else :
    answer.sort(key = lambda x:x[2], reverse=True)
    ans = 4*answer[0][2]+1
    for com in combinations(answer, 2) :
        ans = max(ans, duplicate(com[0], com[1]))
    print(ans)


'''
- 반례(십자가 찾기(https://www.acmicpc.net/problem/16924) 예제 입력1 참고)
```
input
6 8
....#...
...##...
..#####.
...##...
....#...
........

answer
9
```
'''