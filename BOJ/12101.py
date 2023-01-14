# 2023-01-14 13:17:55
# https://www.acmicpc.net/problem/12101
import sys
input = sys.stdin.readline
    
n, k = map(int, input().split())

dp = [['1'], ['1+1', '2'], ['1+1+1', '1+2', '2+1', '3']]

calculations = []
for i in range(4, n+1) :
    for j in range(1, 4) :  # '1+', '2+', '3+'
        for num in dp[i-j-1] :  # 'j+num'
            calculations.append(str(j) + "+" + num)
    dp.append(calculations)

if k <= len(dp[n-1]) :
    print(dp[n-1][k-1])
else : 
    print(-1)