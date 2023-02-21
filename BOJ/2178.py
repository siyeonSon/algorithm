# 2023-01-21 19:45:20
# https://www.acmicpc.net/problem/2178

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1000000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

queue = deque()
queue.append([0, 0])

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1 :  # 끝점이 나오면 끝냄
        print(maze[n-1][m-1])  # 마지막에 누적된 합을 print
        break
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if maze[nx][ny] == 1 and not visited[nx][ny] :
                maze[nx][ny] = maze[x][y] + 1  # 이동할 자리에 현재 누적된 값 + 1
                visited[nx][ny] = True
                queue.append([nx, ny])