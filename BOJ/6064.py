# 2023-01-21 17:41:23
# https://www.acmicpc.net/problem/6064

import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    answer = 0
    m, n, x, y = map(int, input().split())
    lcm = m*n//math.gcd(m,n)

    while(True) :
        answer += 1
        if (answer-x)%m == 0 and (answer-y)%n == 0 :
            break
        if (answer > lcm) :
            answer = -1
            break

    print(answer)