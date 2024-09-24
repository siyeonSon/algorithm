# 2024-09-22 00:23:31
# https://www.acmicpc.net/problem/3986

import sys
input = sys.stdin.readline

n = int(input())

answer = 0
for _ in range(n) :
    word = input().strip()
    stack = []
    for w in word :
        if len(stack) > 0 and stack[-1] == w :
            stack.pop()
            continue
        stack.append(w)
    if len(stack) == 0 :
        answer += 1

print(answer)