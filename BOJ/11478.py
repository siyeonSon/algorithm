# 2024-12-02 15:45:30
# https://www.acmicpc.net/problem/11478

import sys
input = sys.stdin.readline

s = input().rstrip()
answer = set()
for i in range(len(s)) :
    for j in range(i+1, len(s)+1) :
        answer.add(s[i:j])

print(len(answer))