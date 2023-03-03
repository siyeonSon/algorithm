# 2023-03-03 22:24:35
# https://www.acmicpc.net/problem/1525

from collections import deque
import sys
input = sys.stdin.readline

# 퍼즐을 문자열 123456780로 정렬시킨다고 생각하자
puzzle = ''
for _ in range(3) :
    puzzle += ''.join(list(input().split()))

# 현재 puzzle의 모습을 key로, 움직인 횟수를 value로 저장
visited = {puzzle:0}

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(puzzle) :
    queue = deque()
    queue.append(puzzle)

    while queue :
        puzzle = queue.popleft()
        cnt = visited[puzzle]
        z = puzzle.index('0')  # 0(빈칸)의 위치
        
        if puzzle == '123456780' :
            return cnt

        x = z // 3  # 2차원 배열의 행
        y = z % 3  # 2차원 배열의 열

        cnt += 1
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3 :
                nz = nx*3 + ny
                puz = list(puzzle)
                puz[z], puz[nz] = puz[nz], puz[z]
                npuzzle = ''.join(puz)

                # 방문하지 않았다면
                if visited.get(npuzzle, 0) == 0 :
                    visited[npuzzle] = cnt
                    queue.append(npuzzle)
    return -1

print(bfs(puzzle))