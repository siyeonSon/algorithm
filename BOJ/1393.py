# 2023-03-01 14:39:09
# https://www.acmicpc.net/problem/1393

import math
import sys
input = sys.stdin.readline

xs, ys = map(int, input().split())  # 정류장의 위치
xe, ye, dx, dy = map(int, input().split())  # 현재 위치, 열차의 거리 증가 값
dx, dy = dx//math.gcd(dx, dy), dy//math.gcd(dx, dy)

ans = 80000
i = 0  # 증가값
while True :
    dis = (dx*i+xe-xs)**2 + (dy*i+ye-ys)**2
    if dis >= ans :
        i -= 1
        break
    ans = dis
    i += 1

print(dx*i+xe, dy*i+ye)

# 가까워 지다가 -> 멀어지거나
# 계속 멀어짐