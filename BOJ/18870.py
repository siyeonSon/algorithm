# 2023-03-28 22:51:07
# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

xx = sorted(list(set(x)))

for i in x :
    print(xx.index(i), end=' ')