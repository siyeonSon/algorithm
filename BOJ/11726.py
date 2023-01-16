# 2023-01-16 15:46:01
# https://www.acmicpc.net/problem/11726

import sys
input = sys.stdin.readline

n = int(input())
tile = [1, 2]
for i in range(2, n) :
    tile.append(tile[i-1] + tile[i-2])
print(tile[n-1] % 10007)