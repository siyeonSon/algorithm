# 2023-03-13 19:57:12
# https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

# 1 a b -> find
def find(x) :
    if parent[x] == x :
        return x
    parent[x] = find(parent[x])  ## 경로압축(https://www.acmicpc.net/board/view/98382)
    return parent[x]

# 0 a b -> union
def union(a, b) :
    pa, pb = find(a), find(b)
    if pa < pb :
        parent[pb] = pa
    else :
        parent[pa] = pb

for _ in range(m) :
    command, a , b = map(int, input().split())
    if command == 0 :
        union(a, b)
    else :
        if find(a) == find(b) :
            print("YES")
        else :
            print("NO")