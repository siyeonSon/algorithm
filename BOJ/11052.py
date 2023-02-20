# 2023-01-16 17:09:35
# https://www.acmicpc.net/problem/11052

import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

for i in range(n) :
    cost = []
    for j in range(i//2 + 1) :
        cost.append(p[j] + p[i-j-1])  # 1+a, 2+b, 3+c ...
    cost.append(p[i])  # 0+z
    p[i] = max(cost)

print(p[n-1])