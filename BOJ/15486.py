# 2024-03-06 15:18:38
# https://www.acmicpc.net/problem/15486

import sys
input = sys.stdin.readline

n = int(input())
tp = [[0,0]]
for _ in range(n) :
    tp.append(list(map(int, input().split())))

dp = [0] * (n+1)
for i in range(1, n+1) : 
    t, p = tp[i][0], tp[i][1]
    dp[i] = max(dp[i], dp[i-1])
    fin_date = t + i - 1
    if fin_date <= n :
        dp[fin_date] = max(dp[fin_date], dp[i-1]+p)

print(dp[n])