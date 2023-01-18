# 2023-01-18 19:08:58
# https://www.acmicpc.net/problem/1463

import sys
input = sys.stdin.readline

n = int(input())

d = [0, 1, 1, 1]  # 0 1 2 3
for i in range(4, n+1) :
    compare = []
    if i%3 == 0 :
        compare.append(d[i//3])
    if i%2 == 0 :
        compare.append(d[i//2])
    compare.append(d[i-1])
    d.append(min(compare) + 1)

print(d[n])