# 2024-08-16 00:12:16
# https://www.acmicpc.net/problem/2812

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = input().strip()

stack = []

k = K
for n in number:
    while len(stack) > 0 and k > 0 and stack[-1] < n :
        k -= 1
        stack.pop()
    stack.append(n)

print("".join(stack[:N-K]))