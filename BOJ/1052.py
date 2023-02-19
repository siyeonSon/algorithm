# 2023-02-19 19:34:34
# https://www.acmicpc.net/problem/1052

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ans = 0
while True :
    if bin(n).count('1') <= k :
        break
    n += 1
    ans += 1

print(ans)