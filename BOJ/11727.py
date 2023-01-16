# 2023-01-16 15:53:52
# https://www.acmicpc.net/problem/11727

import sys
input = sys.stdin.readline

n = int(input())
tile = [1, 3]
for i in range(2, n) :
    tile.append(tile[i-1] + 2 * tile[i-2])
print(tile[n-1] % 10007)