# 2025-01-22 19:05:58
# https://www.acmicpc.net/problem/2607

import sys
input = sys.stdin.readline

n = int(input())
target = list(input().strip())

answer = 0
for _ in range(n-1) :
    compare = target[:]
    word = input().rstrip()
    cnt = 0
    for w in word :
        if w in compare :
            compare.remove(w)
        else :
            cnt += 1
    if cnt <= 1 and len(compare) <= 1 :
        answer += 1

print(answer)