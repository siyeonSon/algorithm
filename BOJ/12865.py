# 2025-03-24 14:48:48
# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k+1)  # dp[i]: i 무게 만큼 담을 수 있는 최대 가치
items = []
for _ in range(n) :
    items.append(list(map(int, input().split())))

for w, v in items :
    for weight in range(k, w-1, -1) :
        dp[weight] = max(dp[weight], dp[weight-w] + v)
print(dp[k])