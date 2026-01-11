# 2026-01-11 16:44:59
# https://www.acmicpc.net/problem/10101

import sys
input = sys.stdin.readline

t = []
for _ in range(3) :
    t.append(int(input()))

t.sort()

answer = ''
if sum(t) == 180 :
    if t[0] == t[1] == t[2] :
        answer = 'Equilateral'
    elif t[0] == t[1] or t[1] == t[2]:
        answer = 'Isosceles'
    else :
        answer = 'Scalene'
else :
    answer = 'Error'
print(answer)