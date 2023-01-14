# 2023-01-14 12:41:03
# https://www.acmicpc.net/problem/9095
import sys
input = sys.stdin.readline

def plus123(num) :
    dp = [0, 1, 2, 4]
    for i in range(4, num + 1) :
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[num]

n = int(input())
for _ in range(n) :
    num = int(input())
    print(plus123(num))