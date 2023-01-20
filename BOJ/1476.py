# 2023-01-20 12:03:13
# https://www.acmicpc.net/problem/1476

import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

answer = 1
while not((answer-e)%15==0 and (answer-s)%28==0 and (answer-m)%19==0) :
    answer += 1

print(answer)