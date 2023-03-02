# 2023-03-02 15:41:01
# https://www.acmicpc.net/problem/16924

import sys
input = sys.stdin.readline

answer = []
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# * 사용 여부 확인
visited = [[0]*m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if board[i][j] == '*' :
            visited[i][j] = 1


# @return 방향에 따른 *의 개수
def count_star(x, y, dx, dy, cnt) :  # 중심(x, y), 탐색 방향(dx, dy), 증가값(cnt)
    while True :
        nx, ny = x+cnt*dx, y+cnt*dy
        if nx >= n or nx < 0 or ny >= m or ny <0  or board[nx][ny] == '.' :
            return cnt-1
        cnt += 1


# 동서남북 십자가가 되는가?
def cross(x, y) :
    east = count_star(x, y, 0, 1, 1)  # 동(0, 1)
    south = count_star(x, y, 1, 0, 1)  # 남(1, 0)
    west = count_star(x, y, 0, -1, 1)  # 서(0, -1)
    north = count_star(x, y, -1, 0, 1)  # 북(-1, 0)

    # 십자가의 길이
    s = min(east, south, west, north)

    if s > 0 :
        # * 사용 여부 체크
        for i in range(s+1) :
            visited[x][y+i], visited[x+i][y], visited[x][y-i], visited[x-i][y] = 0, 0, 0, 0
    
    # 정답에 추가
    for j in range(s, 0, -1) :
        answer.append([x+1, y+1, j])


# @return 사용하지 않은 *의 개수
def left_star(visited) :
    cnt = 0
    for v in visited :
        cnt += sum(v)
    return cnt


# (i, j)를 중심으로 하는 십자가 찾기
for i in range(1, n-1) :
    for j in range(1, m-1) :
        if board[i][j] == '*' :
            cross(i, j)

# 정답 출력
if answer and left_star(visited) == 0 :
    print(len(answer))
    for ans in answer :
        print(*ans)
else :
    print(-1)