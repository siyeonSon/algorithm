# 2024-11-15 10:48:18
# https://www.acmicpc.net/problem/16500

import re
import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
a = [input().strip() for _ in range(n)]
dp = [False for _ in range(len(s) + 1)]

dp[0] = True
for i in range(len(s)) :
    if not dp[i] :
        continue
    for t in a :
        if s[i:i+len(t)] == t :
            dp[i+len(t)] = True

print(int(dp[len(s)]))