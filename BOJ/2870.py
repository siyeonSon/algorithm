# 2024-09-29 13:38:36
# https://www.acmicpc.net/problem/2870

import sys
input = sys.stdin.readline

n = int(input())

number = "0123456789"
answer = []
for _ in range(n) :
    stack = ""
    str = input().strip()
    for s in str :
        if s in number :
            stack += s
            continue
        if stack :
            answer.append(int(stack))
            stack = ""
    if stack :
        answer.append(int(stack))

answer.sort()
for a in answer :
    print(a)