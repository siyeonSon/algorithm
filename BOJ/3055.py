# 2023-04-29 07:53:30
# https://www.acmicpc.net/problem/3055

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

distance = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()


def bfs(Dx,Dy):
    while queue:
        x, y = queue.popleft()
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS"


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            queue.append([i,j])
        elif graph[i][j] == 'D':
            Dx, Dy = i, j

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            queue.append([i, j])

print(bfs(Dx, Dy))