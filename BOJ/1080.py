# 2023-02-26 14:19:41
# https://www.acmicpc.net/problem/1080

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
b = [list(input().strip()) for _ in range(n)]

# (i,j) 위치가 서로 같은지 비교
same = [[False]*m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if a[i][j] == b[i][j] :
            same[i][j] = True

# 그래프 탐색 - '섬의 개수(4963)' 문제와 유사
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y) :
    global visited
    visited[x][y] = True
    for i in range(4) :
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if not same[nx][ny] and not visited[nx][ny] :
                dfs(nx, ny)
    return 1

def bfs(x, y) :
    global visited
    queue = deque()
    queue.append([x,y])
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if not same[nx][ny] and not visited[nx][ny] :
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    return 1

# DFS로 탐색
ans = 0
visited = [[False]*m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if not same[i][j] and not visited[i][j] :
            ans += dfs(i, j)

# BFS로 탐색
ans = 0
visited = [[False]*m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if not same[i][j] and not visited[i][j] :
            ans += bfs(i, j)

print(ans)