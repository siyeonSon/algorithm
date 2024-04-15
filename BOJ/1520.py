# 2024-04-15 21:21:22
# https://www.acmicpc.net/problem/1520

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

answer = 0
dp = [[-1]*n for _ in range(m)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y) :
    global dp
    if x == m-1 and y == n-1 : 
        return 1
    if dp[x][y] != -1 :
        return dp[x][y]
    way = 0
    for i in range(4) :
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx < m and 0 <= ny < n :
            if board[x][y] > board[nx][ny] :
                way += dfs(nx, ny)
    dp[x][y] = way
    return dp[x][y]

dfs(0, 0)
print(dp[0][0])