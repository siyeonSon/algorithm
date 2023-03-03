# 2023-03-03 13:54:52
# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 테두리 그리기    
    field = make_edge(rectangle)
    
    # 경로 탐색
    answer = bfs(characterX*2, characterY*2, itemX*2, itemY*2, field)
    
    return answer


# 테두리 그리기  
def make_edge(rectangle) :
    MAX = 102  # 좌표값은 1 이상 50 이하인 자연수
    field = [[0]*MAX for _ in range(MAX)]
    
    # 내부 + 테두리 그리기
    for rec in rectangle :
        lx, ly, rx, ry = rec
        for i in range(lx*2, rx*2+1) :
            for j in range(ly*2, ry*2+1) :
                field[i][j] = 1

    # 내부 삭제
    for rec in rectangle :
        lx, ly, rx, ry = rec
        for i in range(lx*2+1, rx*2) :
            for j in range(ly*2+1, ry*2) :
                field[i][j] = 0
    return field


# 경로 탐색
def bfs(characterX, characterY, itemX, itemY, field) :
    MAX = 102
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([characterX, characterY])
    
    while queue :
        x, y = queue.popleft()
        if x == itemX and y == itemY :
            return field[x][y] // 2
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < MAX and 0 <= ny < MAX :
                if field[nx][ny] == 1 :
                    queue.append([nx, ny])
                    field[nx][ny] += field[x][y]