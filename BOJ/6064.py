# 2023-01-21 17:41:23
# https://www.acmicpc.net/problem/6064

import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    m, n, x, y = map(int, input().split())
    lcm = m*n//math.gcd(m,n)
    
    answer = x
    while(True) :
        if (answer-y)%n == 0 :
            break
        if (answer > lcm) :
            answer = -1
            break
        answer += m

    print(answer)