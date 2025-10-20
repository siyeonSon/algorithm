# 2025-10-20 21:49:12
# https://www.acmicpc.net/problem/2583

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

m, n, k = map(int, input().split())
empty = [[True] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2) :
        for j in range(y1, y2) :
            empty[i][j] = False

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
def dfs(x, y, area):
    for i in range(4) :
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx < n and 0 <= ny < m :
            if empty[nx][ny] and not visited[nx][ny] :
                visited[nx][ny] = True
                area = dfs(nx, ny, area+1)

    return area

def bfs(x, y, area) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny < m :
                if empty[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True   # 큐에 넣기 전에 방문 체크를 해야 중복 방문을 방지할 수 있음
                    queue.append((nx, ny))
                    area += 1
    return area

answer = []
for i in range(n) :
    for j in range(m) :
        if empty[i][j] and not visited[i][j] :
            visited[i][j] = True
            answer.append(bfs(i, j, 1))

answer.sort()
print(len(answer))
print(*answer)