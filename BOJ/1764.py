# 2025-12-29 23:09:26
# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = set(), set()
for _ in range(n) :
    a.add(input().rstrip())
for _ in range(m) :
    b.add(input().rstrip())

answer = list(a.intersection(b))
answer.sort()

print(len(answer))
for a in answer :
    print(a)