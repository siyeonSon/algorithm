# 2023-02-22 14:44:17
# https://www.acmicpc.net/problem/1263

import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n) :
    time.append(list(map(int, input().split())))  # t, s
time.sort(key=lambda x:x[1], reverse=True)

ans = time[0][1] - time[0][0]
for i in range(1, n) :
    if time[i][1] < ans :
        ans = time[i][1] - time[i][0]
    else :
        ans -= time[i][0]

if ans < 0 :
    print(-1)
else :
    print(ans)