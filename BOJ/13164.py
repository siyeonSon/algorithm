# 2024-03-04 23:48:11
# https://www.acmicpc.net/problem/13164

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h = list(map(int, input().split()))

diff = []
for i in range(n-1) :
    diff.append(h[i+1]-h[i])

diff.sort()
ans = sum(diff[:n-k])
print(ans)