# 2023-02-21 14:00:21
# https://www.acmicpc.net/problem/1004

import sys
input = sys.stdin.readline

t = int(input())  # 테스트 수
for _ in range(t) :
    x1, y1, x2, y2 = map(int, input().split())  # 출발지(x1, y1) -> 도착지(x2, y2)
    n = int(input())  # 행성의 개수
    planets = []
    for _ in range(n) :
        cx, cy, r = map(int, input().split())  # 행성계의 중점과 반지름 (cx, cy, r)
        planets.append([cx, cy, r])

    cnt = 0
    for i in range(n) :
        cx, cy, r = planets[i]
        if ((cx-x1)**2+(cy-y1)**2 < r**2 and (cx-x2)**2+(cy-y2)**2 > r**2) or ((cx-x1)**2+(cy-y1)**2 > r**2 and (cx-x2)**2+(cy-y2)**2 < r**2)  :
            cnt += 1
    print(cnt)