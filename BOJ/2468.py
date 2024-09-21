# 2024-09-21 22:07:11
# https://www.acmicpc.net/problem/2468

import sys
sys.setrecursionlimit(100000)
import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y) :
    visited[x][y] = True
    for i in range(4) :
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if not visited[nx][ny] and board[nx][ny] >= height :
                dfs(nx, ny)
    return 1

answer = 0
min_b = min(map(min, board))  # 최저 높이
max_b = max(map(max, board))  # 최대 높이

for height in range(min_b, max_b+1) :
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] and board[i][j] >= height :
                cnt += dfs(i, j)

    if cnt > answer :
        answer = cnt

print(answer)