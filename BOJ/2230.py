# 2023-02-20 15:04:58
# https://www.acmicpc.net/problem/2230

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n) :
    a.append(int(input()))

sorted(a)
ans = a[-1] - a[0]
for i in range(n) :
    for j in range(i, n) :
        diff = a[j] - a[i]
        if diff > m :
            ans = min(diff, ans)
        elif diff == m :
            ans = m
            break
print(ans)