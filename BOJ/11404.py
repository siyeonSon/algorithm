# 2024-10-12 10:27:32
# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[1E8]*n for _ in range(n)]
for _ in range(m) :
    a, b, c = map(int, input().split())
    bus[a-1][b-1] = min(c, bus[a-1][b-1])

for k in range(n) :  # 중간
    for i in range(n) :  # 시작
        for j in range(n) :  # 도착
            if i == j : continue
            bus[i][j] = min(bus[i][j], bus[i][k]+bus[k][j])

for i in range(n) :
    for j in range(n) :
        if bus[i][j] == 1E8 :
            print("0", end=" ")
        else :
            print(bus[i][j], end=" ")
    print()