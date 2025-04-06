# 2025-04-06 22:23:29
# https://www.acmicpc.net/problem/2193

import sys
input = sys.stdin.readline

n = int(input())

def fib(n) :
    a = 1
    b = 1
    for i in range(n) :
        yield a
        a, b = b, a+b

print(list(fib(n))[-1])