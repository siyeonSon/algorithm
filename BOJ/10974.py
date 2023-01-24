# 2023-01-24 21:12:50
# https://www.acmicpc.net/problem/10974

import sys
input = sys.stdin.readline

n = int(input())

s = []
def dfs() :
    if len(s) == n :
        print(*s)
        return 

    for i in range(1, n+1):
        if not i in s :
            s.append(i)
            dfs()
            s.pop()

dfs()