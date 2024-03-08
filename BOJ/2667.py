# 2024-03-08 12:58:04
# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1000000)

n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int, input().strip())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
visited = [[False] * n for _ in range(n)]

def pprint(visited) :
    for v in visited :
        print(v)

answer = []
def dfs(x, y, cnt) :
    visited[x][y] = True
    for i in range(4) :
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx < n and 0 <= ny < n :
            if board[nx][ny] == 1 and not visited[nx][ny]:
                cnt = dfs(nx, ny, cnt+1)
    return cnt

def bfs(x, y) :
    global visited
    queue = deque()
    queue.append([x, y])
    cnt = 0
    while queue :
        x, y = queue.popleft()
        if visited[x][y] :
            continue
        visited[x][y] = True
        cnt += 1
        for i in range(4) :
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny < n :
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
    return cnt


for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1 and not visited[i][j] :
            # answer.append(bfs(i, j, 1))
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for a in answer :
    print(a)