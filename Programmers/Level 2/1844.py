# 2023-02-23 18:46:30
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    answer = 0
    
    x_len = len(maps)
    y_len = len(maps[0])
    
    visited = [[0] * y_len for _ in range(x_len)]  # 방문하지 않은 경우 == 0
    visited[0][0] = 1  # 시작점은 무조건 방문함
    
    # 동서남북 좌표
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    queue.append([0,0])

    while queue :
        x, y = queue.popleft()    
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < x_len and 0 <= ny < y_len :
                if maps[nx][ny] == 1 and visited[nx][ny] == 0 :  # 벽이 아니고 방문하지 않은 노드
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
    
    if visited[-1][-1] == 0 :  # 상대방 진영에 도착하지 못한 경우
        answer = -1
    else :
        answer = visited[-1][-1]
    return answer