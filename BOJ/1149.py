# 2023-01-15 22:49:23
# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

house = []
n = int(input())
for _ in range(n) :
    house.append(list(map(int, input().split())))

for i in range(1, n) :
    house[i][0] = house[i][0] + min(house[i-1][1], house[i-1][2])  # R
    house[i][1] = house[i][1] + min(house[i-1][0], house[i-1][2])  # G
    house[i][2] = house[i][2] + min(house[i-1][0], house[i-1][1])  # B

print(min(house[n-1]))