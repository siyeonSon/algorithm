# 2024-04-18 00:44:40
# https://www.acmicpc.net/problem/2012

import sys
input = sys.stdin.readline

n = int(input())
expect = [int(input()) for _ in range(n)] 
expect.sort()

answer = 0
for i in range(n) :
    answer += abs(i + 1 - expect[i])

print(answer)