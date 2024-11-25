# 2024-11-25 21:07:52
# https://www.acmicpc.net/problem/10610

import sys
input = sys.stdin.readline

n = input().rstrip()

if '0' in n and sum(map(int, n)) % 3 == 0 :  # 30의 배수가 될 조건
    print(''.join(sorted(n, reverse=True)))
else :
    print(-1)