# 2024-03-10 14:48:57
# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
node = [[i] for i in range(n)]
for _ in range(m) :
    u, v = map(int, input().split())
    node[u-1].append(v-1)
    node[v-1].append(u-1)

visited = [False] * n

def search(x) :
    visited[x] = True
    for nx in node[x] :
        if not visited[nx] :
            search(nx)

ans = 0
for i in range(n) :
    for nx in node[i] :
        if not visited[nx] :
            search(nx)
            ans += 1

print(ans)