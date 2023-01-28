# 2023-01-28 19:26:29
# https://www.acmicpc.net/problem/6603

import itertools
import sys
input = sys.stdin.readline

while True :
    li = list(map(int, input().split()))
    if li == [0] : break

    k = li[0]
    nums = li[1:]
    for com in itertools.combinations(nums, 6) :
        print(*com)
    print()