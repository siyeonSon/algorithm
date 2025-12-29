# 2025-12-29 22:55:51
# https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

answer = 0
for i in range(n) :
    answer += a[i] * b[i]

print(answer)