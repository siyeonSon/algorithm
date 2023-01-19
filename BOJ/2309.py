# 2023-01-19 22:22:01
# https://www.acmicpc.net/problem/2309

from itertools import combinations
import sys
input = sys.stdin.readline

dwarfs = []
for _ in range(9) :
    dwarfs.append(int(input()))

for dw in combinations(dwarfs, 7) :
    if sum(dw) == 100 :
        for s in sorted(dw) :
            print(s)
        break