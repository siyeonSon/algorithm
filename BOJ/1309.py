# 2023-01-09 15:39:00
# https://www.acmicpc.net/problem/1309

n = int(input())
dp = [1, 3]
for i in range(n-1) :
    dp[0], dp[1] = dp[1], 2 * dp[1] + dp[0]
print(dp[1] % 9901)