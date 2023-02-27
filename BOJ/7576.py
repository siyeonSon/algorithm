# 2023-02-27 20:02:10
# https://www.acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

# 모두 익은 토마토인 경우
def rippen(tomato) :
    for i in range(n) :
        for j in range(m) :
            if tomato[i][j] == 0 :
                return False
    return True

# 정답 출력 - 이미 모두 익은 토마토인 경우 0을 출력
if rippen(tomato) :
    print(0)
    exit()

# 그래프 탐색
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs() :
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny < m :
                if tomato[nx][ny] == 0 :  # (nx, ny) 자리에 토마토가 존재하고, 아직 익지 않은 경우
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append([nx, ny])

queue = deque()
for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 1 :
            queue.append([i, j])
bfs()


# 정답 출력 - 최소 하루 이상 지난 경우
print(max(map(max, tomato))-1 if rippen(tomato) else -1)