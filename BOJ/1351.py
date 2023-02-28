# 2023-02-28 14:30:37
# https://www.acmicpc.net/problem/1351

import sys
input = sys.stdin.readline

ans = 0
n, p, q = map(int, input().split())

def dfs(x) :
    global ans
    if x == 0 :
        ans += 1
        return
    dfs(x//p)
    dfs(x//q)

dfs(n)
print(ans)