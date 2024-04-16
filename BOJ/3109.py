# 2024-04-16 16:06:51
# https://www.acmicpc.net/problem/3109

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dx = (-1, 0, 1)  # 우상향으로 먼저 접근해야 최대한 많은 파이프라인을 둘 수 있음

def dfs(x, y) :
    global answer
    board[x][y] = "x"
    if y == c-1 :
        return True
    for i in range(3) :
            nx, ny = dx[i]+x, 1+y
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == "." :
                if dfs(nx, ny) :  # 끝까지 설치 가능한 경우
                    return True
    return False

answer = 0
for x in range(r) :
    answer += dfs(x, 0)
print(answer)


## 참고) 실패하는 경우
def fail_case(x, y) :
    global answer
    board[x][y] = "x"
    for i in range(3) :
            nx, ny = dx[i]+x, 1+y
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == "." :
                board[nx][ny] = "x"
                if ny == c-1 :  # 빵집에 도달한 경우 탐색을 종료함
                    return True  # 그러나 재귀가 아직 끝나지 않았으므로 중간에 더 돌게 됨 -> 오답
                dfs(nx, ny)
    return False