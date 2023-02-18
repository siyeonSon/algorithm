# 2023-02-18 15:04:06
# https://www.acmicpc.net/problem/1484

import sys
input = sys.stdin.readline

g = int(input())
left, right = 1, 1
answer = []

while True :
    diff = right**2 - left**2

    if right + left > g :
        break
    if diff < g :
        right += 1
    elif diff > g :
        left += 1
    else :
        answer.append(right)
        right += 1

if answer :
    print(*answer, sep='\n')
else :
    print(-1)