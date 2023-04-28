# 2023-04-27 22:32:47
# https://www.acmicpc.net/problem/1012

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

'''
t : 테스트 케이스의 개수
m : 배추 밭의 가로 길이
n : 배추 밭의 세로 길이
k : 배추가 심어져 있는 위치의 개수
'''

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y) :
    field[x][y] = False
    for i in range(4) :
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < m and 0 <= ny < n :
            if field[nx][ny] :
                dfs(nx, ny)
    return 1

t = int(input())
for _ in range(t) :
    ans = 0
    m, n, k = map(int, input().split())
    field = [[False] * n for _ in range(m)]

    for _ in range(k) :
        a, b = map(int, input().split())
        field[a][b] = True

    for i in range(m) :
        for j in range(n) :
            if field[i][j] :
                ans += dfs(i, j)

    print(ans)