# 2023-03-27 18:23:26
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1 for i in range(n)]
for i in range(1, n) :
    for j in range(i) :
        if a[i] > a[j] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))