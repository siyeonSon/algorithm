# 2023-02-21 21:51:42
# https://www.acmicpc.net/problem/1260

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m, v = map(int, input().split())
nodes = []
for _ in range(m) :
    nodes.append(list(map(int, input().split())))

visited = [False] * n
graph = [[] * n for _ in range(n)]

for node in sorted(nodes) :
    a, b = node
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for i in range(n) :
    graph[i] = sorted(graph[i])

def dfs(x) :
    visited[x] = True
    print(x+1, end=' ')
    for nx in graph[x] :
        if not visited[nx] :
            dfs(nx)

def bfs(x) :
    visited = [False] * n
    queue = deque()
    queue.append(x)

    while queue :
        x = queue.popleft()
        if not visited[x] :
            visited[x] = True
            print(x+1, end=' ')
        for nx in graph[x] :
            if not visited[nx] :
                queue.append(nx)

dfs(v-1)
print()
bfs(v-1)