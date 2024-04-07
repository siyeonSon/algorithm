# 2024-04-07 16:51:20
# https://www.acmicpc.net/problem/1987

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = []
for _ in range(r) :
    board.append(list(input().strip()))

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

answer = 0

## DFS 활용
visited = set()
def dfs(x, y, cnt) :
    global answer
    answer = max(answer, cnt)
    for i in range(4) :
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx < r and 0 <= ny < c :
            if board[nx][ny] not in visited :
                visited.add(board[nx][ny])
                dfs(nx, ny, cnt+1)
                visited.remove(board[nx][ny])  # 방문에서 제거해 주는 것이 핵심임
visited.add(board[0][0])
# dfs(0, 0, 1)
# print(answer)

## DFS 활용2
def dfs2(x, y, visited) :
    global answer
    answer = max(answer, len(visited))
    for i in range(4) :
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx < r and 0 <= ny < c :
            if board[nx][ny] not in visited :
                dfs2(nx, ny, visited+board[nx][ny])

# dfs2(0, 0, board[0][0])
# print(answer)

## BFS 활용
def bfs(x, y) :
    global answer
    queue = set([(x, y, board[x][y])])  # 시간 초과 발생 -> deque는 O(n)이므로 O(1)인 set을 활용하는 것이 핵심임
    while queue :
        x, y, visited = queue.pop()
        answer = max(len(visited), answer)
        for i in range(4) :
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < r and 0 <= ny < c :
                if board[nx][ny] not in visited :
                    queue.add((nx, ny, visited+board[nx][ny]))
    return answer
# print(bfs(0, 0))