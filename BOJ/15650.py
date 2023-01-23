# 2023-01-23 23:59:38
# https://www.acmicpc.net/problem/15650

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
 
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()

dfs(1)