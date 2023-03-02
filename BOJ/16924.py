# 2023-03-02 15:41:01
# https://www.acmicpc.net/problem/16924

import sys
input = sys.stdin.readline

answer = []
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

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
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '*' :
            cnt += 1
            continue
        return cnt-1


# 동서남북 십자가가 되는가?
def cross(x, y) :
    compass = []
    for i in range(4) :
        compass.append(count_star(x, y, dx[i], dy[i], 1))
    
    s = min(compass)  # 십자가의 길이

    # * 사용 여부 체크
    if s > 0 :
        for i in range(s+1) :
            for j in range(4) :
                visited[x+i*dx[j]][y+i*dy[j]] = 0
    
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