# 2024-11-03 01:00:41
# https://www.acmicpc.net/problem/2204

import sys
input = sys.stdin.readline

while True :
    n = int(input())
    if n == 0 :
        break
    answer = input().rstrip()
    for _ in range(n-1) :
        word = input().rstrip()
        if answer.upper() > word.upper() :
            answer = word
    print(answer)