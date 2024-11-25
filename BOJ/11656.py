# 2024-11-25 21:02:54
# https://www.acmicpc.net/problem/11656

import sys
input = sys.stdin.readline

s = input().rstrip()
answer = []

for i in range(len(s)) :
    answer.append(s[i:])

answer.sort()
print('\n'.join(answer))