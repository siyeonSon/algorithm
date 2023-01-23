# 2023-01-23 23:20:00
# https://www.acmicpc.net/problem/15649

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
 
s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()