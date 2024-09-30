# 2024-09-30 14:10:02
# https://www.acmicpc.net/problem/3474

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    answer = 0
    while n >= 5 :
        n //= 5
        answer += n
    print(answer)