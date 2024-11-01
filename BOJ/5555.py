# 2024-11-01 14:27:39
# https://www.acmicpc.net/problem/5555

import sys
input = sys.stdin.readline

want = input().rstrip()
n = int(input())
answer = 0
for _ in range(n) :
    ring = input().rstrip()
    if want in ring*2 :
        answer += 1 
print(answer)