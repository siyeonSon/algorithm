# 2023-01-18 19:51:05
# https://www.acmicpc.net/problem/16194

import math
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

for i in range(n) :
    cost = []
    for j in range(math.ceil(i/2)) :
        cost.append(p[j] + p[i-j-1])  # 1+a, 2+b, 3+c ...
    cost.append(p[i])  # 0+z
    p[i] = min(cost)

print(p[n-1])