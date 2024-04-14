# 2024-04-14 23:32:44
# https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline

n = int(input())
fib = [0, 1]
for i in range(1, n) :
    fib.append(fib[i-1] + fib[i])
print(fib[n])