# 2023-02-19 14:02:10
# https://www.acmicpc.net/problem/1010

import sys
input = sys.stdin.readline

# 점화식 : d[n][m] = d[n-1][m-1] + d[n-1][m-2] + ... d[n-1][n-1]
# 0 < N ≤ M < 30

t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    d = [[0] * (m+1) for _ in range(n+1)]
    d[1] = [i for i in range(m+1)]  # n == 1 일 때
    for i in range(2, n+1) :
        for j in range(i, m+1) :
            for k in range(j) :
                d[i][j] += d[i-1][k]
    print(d[n][m])