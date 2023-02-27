# 2023-02-20 15:04:58
# https://www.acmicpc.net/problem/2230

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n) :
    a.append(int(input()))
a.sort()

ans = []
left, right = 0, 1
while True :
    if right >= n or left > right :
        break
    diff = a[right] - a[left]
    if diff >= m :
        ans.append(diff)
        left += 1
    else :
        right += 1

print(min(ans))