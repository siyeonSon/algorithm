# 2023-11-23 22:44:54
# https://www.acmicpc.net/problem/2583

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

m, n, k = map(int, input().split())

visited = list([False]*m for _ in range(n))
for _ in range(k) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            visited[i][j] = True

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y) :
    global area_count
    visited[x][y] = True
    area_count += 1
    for i in range(4) :
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if not visited[nx][ny] :
                dfs(nx, ny)

count = 0
areas = []
for i in range(n) :
    for j in range(m) :
        if not visited[i][j] :
            count += 1
            area_count = 0
            dfs(i, j)
            areas.append(area_count)

print(count)
print(*sorted(areas))