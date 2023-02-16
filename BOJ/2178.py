# 2023-01-21 19:45:20
# https://www.acmicpc.net/problem/2178

'''
DFS 풀이
DFS로 최단 거리를 찾을 수 없다.
깊이 탐색 알고리즘(DFS)는 처음에 운이 좋게 찾으면 최단거리가 되지만, 운이 안 좋으면 모든 최장 거리도 될 수 있기 때문이다.
모든 깊이를 탐색하고 성공 유무를 결정해야 하기 때문에, DFS가 어울리지 않는다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

answer = 1
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def dfs(x, y) :
    global answer
    if 0 <= x < n and 0 <= y < m :
        if maze[x][y] == 1 and visited[x][y] == False :
            answer += 1
            visited[x][y] = True
        for k in range(4) :
            nx, ny = x+dx[k], y+dy[k]
            dfs(nx, ny)
        if x == n-1 and y == m-1 :
            return

dfs(0, 0)