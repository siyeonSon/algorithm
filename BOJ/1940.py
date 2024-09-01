# 2024-09-01 21:03:54
# https://www.acmicpc.net/problem/1940

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
armor = list(map(int, input().split()))

armor.sort()
left, right = 0, n-1
answer = 0

while left < right :
    sum = armor[left] + armor[right]
    if sum < m :
        left += 1
    elif sum > m :
        right -= 1
    else :
        answer += 1
        left += 1
        right -= 1

print(answer)