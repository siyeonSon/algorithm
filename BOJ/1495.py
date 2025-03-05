# 2025-03-04 20:32:42
# https://www.acmicpc.net/problem/1495

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, s, m = map(int, input().split())
volums = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = True

for i in range(n) :
    for p in range(m+1) :
        if dp[i][p] :
            if 0 <= p + volums[i] <= m :
                dp[i+1][p + volums[i]] = True
            if 0 <= p - volums[i] <= m :
                dp[i+1][p - volums[i]] = True

answer = -1
for i in range(m, -1, -1) :
    if dp[-1][i] :
        answer = i
        break
print(answer)

## 문제풀이 아이디어
# dp[i][j] : i번째 곡을 연주할 때 j 볼륨 연주 가능
# i번째 원소가 j를 만들 수 있으면 dp[i][j]에 True로 저장
# i가 만들 수 있는 모든 경우의 수는 j를 순환하면 알 수 있음