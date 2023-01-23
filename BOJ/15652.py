# 2023-01-23 23:07:55
# https://www.acmicpc.net/problem/15652

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
        dfs(i)
        s.pop()

dfs(1)