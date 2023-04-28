# 2023-04-22 21:02:19
# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

def check(mid) :
    slice = 0
    for l in line :
        slice += l//mid
    return slice >= n

lo, hi = 0, max(line)+1
while lo + 1 < hi :
    mid = (lo+hi)//2
    if check(mid) :
        lo = mid
    else :
        hi = mid

print(lo)