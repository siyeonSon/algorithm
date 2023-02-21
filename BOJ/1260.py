# 2023-02-21 12:39:04
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
v = int(input())

graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(v) :
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = 0

def dfs(x) :
    global ans
    visited[x] = True
    for nx in graph[x] :
        if not visited[nx] :
            dfs(nx)
            ans += 1

def bfs(v) :
    global ans
    queue = deque()
    queue.append(v)

    while queue :
        x = queue.popleft()
        visited[x] = True
        for nx in graph[x] :
            if nx not in queue and not visited[nx] :
                queue.append(nx)
                ans += 1

dfs(0)
# bfs(0)
print(ans)