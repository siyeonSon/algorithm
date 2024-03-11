# 2024-03-11 23:15:52
# https://www.acmicpc.net/problem/2141

import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n) :
    people.append(list(map(int, input().split())))

people.sort()

sum = 0
for i in range(n) :
    sum += people[i][1]
mid = sum / 2

ans, tmp = 0, 0
for i in range(n) :
    tmp += people[i][1]
    if tmp >= mid :
        ans = people[i][0]
        break

print(ans)