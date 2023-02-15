# 2023-02-15 20:25:49
# https://www.acmicpc.net/problem/4963

import sys
input = sys.stdin.readline

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def dfs(x, y) :
    land[x][y] = "*"  # 방문함
    for i in range(8) :  # 상하좌우대각선 탐색
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w :  # 범위 내부에 있는 경우에만
            if land[nx][ny] == 1 :
                dfs(nx, ny)
    return 1

while True :
    w, h = map(int, input().split())
    if w==0 and h==0 :
        break
    land = [list(map(int, input().split())) for _ in range(h)]

    # 탐색
    answer = 0
    for i in range(h) :  # h가 x좌표를 의미
        for j in range(w) :  # w가 y좌표를 의미
            if land[i][j] == 1 :
                answer += dfs(i, j)
    print(answer)