# 2023-03-21 10:53:29
# https://www.acmicpc.net/problem/1072

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x

if z >= 99 :
    print(-1)
    exit()

# z와 mid번 더했을 때 새로운 z 비교
def check(mid) :
    nz = (y+mid) * 100 // (x+mid)
    return nz <= z

# mid는 몇 번 더 게임을 해야하는가
lo, hi = 0, x
while lo + 1 < hi :
    mid = (lo+hi)//2
    if check(mid) :
        lo = mid
    else :
        hi = mid

print(hi)